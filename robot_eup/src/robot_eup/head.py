import rospy
from std_msgs.msg import String
import time, sys
from numpy import *
from timeit import Timer
import numpy.linalg
import actionlib
from scipy.ndimage.filters import *
from std_srvs.srv import Empty, EmptyResponse
from actionlib_msgs.msg import GoalStatus
from actionlib_msgs.msg import *
from pr2_mechanism_msgs.msg import *
from pr2_mechanism_msgs.srv import *
from pr2_controllers_msgs.msg import *
from trajectory_msgs.msg import *
from sensor_msgs.msg import JointState
from actionlib import SimpleActionClient
from pr2_controllers_msgs.msg import PointHeadAction, PointHeadGoal
from geometry_msgs.msg import *
from tf import TransformListener

class Head:

        # 'LOOK_FORWARD: 'LOOK_FORWARD',
        # 'FOLLOW_RIGHT_EE: 'FOLLOW_RIGHT_EE',
        # 'FOLLOW_LEFT_EE: 'FOLLOW_LEFT_EE',
        # 'GLANCE_RIGHT_EE: 'GLANCE_RIGHT_EE',
        # 'GLANCE_LEFT_EE: 'GLANCE_LEFT_EE',
        # 'NOD: 'NOD',
        # 'SHAKE: 'SHAKE',
        # 'FOLLOW_FACE: 'FOLLOW_FACE',
        # 'LOOK_AT_POINT: 'LOOK_AT_POINT',
        # 'LOOK_DOWN: 'LOOK_DOWN',
        # 'NOD_ONCE : 'NOD_ONCE ',
        # 'SHAKE_ONCE: 'SHAKE_ONCE',

    def __init__(self):
        self.defaultLookatPoint = Point(1,0,1.35)
        self.downLookatPoint = Point(0.5,0,0.5)
        self.targetLookatPoint = Point(1,0,1.35)
        self.currentLookatPoint = Point(1,0,1.35)

        self.currentGazeAction = 'LOOK_FORWARD';
        self.prevGazeAction = self.currentGazeAction
        self.prevTargetLookatPoint = array(self.defaultLookatPoint);

        # Some constants
        self.doNotInterrupt = ['GLANCE_RIGHT_EE', 'GLANCE_LEFT_EE', 'NOD', 'SHAKE'];
        self.nodPositions = [Point(1,0,1.05), Point(1,0,1.55)]
        self.shakePositions = [Point(1,0.2,1.35), Point(1,-0.2,1.35)]
        self.nNods = 5
        self.nShakes = 5

        self.nodCounter = 5
        self.shakeCounter = 5
        self.facePos = None

        ## Action client for sending commands to the head.
        self.headActionClient = SimpleActionClient('/head_traj_controller/point_head_action', PointHeadAction)
        self.headActionClient.wait_for_server()
        rospy.loginfo('Head action client has responded.')

        self.headGoal = PointHeadGoal()
        self.headGoal.target.header.frame_id = 'base_link'
        self.headGoal.min_duration = rospy.Duration(1.0)
        self.headGoal.target.point = Point(1,0,1)

        ## Client for receiving detected faces
        #self.faceClient = SimpleActionClient('face_detector_action', FaceDetectorAction)

        ## Service client for arm states
        self.tfListener = TransformListener()


    ## Callback function to receive ee states and face location
    def getEEPos(self, armIndex):

        fromFrame = '/base_link'
        if (armIndex == 0):
            toFrame = '/r_wrist_roll_link'
        else:
            toFrame = '/l_wrist_roll_link'

        try:
            t = self.tfListener.getLatestCommonTime(fromFrame, toFrame)
            (position, rotation) = self.tfListener.lookupTransform(fromFrame, toFrame, t)
        except:
            rospy.logerr('Could not get the end-effector pose.')
        #objPoseStamped = PoseStamped()
        #objPoseStamped.header.stamp = t
        #objPoseStamped.header.frame_id = '/base_link'
        #objPoseStamped.pose = Pose()
        #relEEPose = self.tfListener.transformPose(toFrame, objPoseStamped)
        return Point(position[0], position[1], position[2])

    def getFaceLocation(self):
        connected = self.faceClient.wait_for_server(rospy.Duration(1.0))
        if connected:
            fgoal = FaceDetectorGoal()
            self.faceClient.send_goal(fgoal)
            self.faceClient.wait_for_result()
            f = self.faceClient.get_result()
            ## If there is one face follow that one, if there are more than one, follow the closest one
            closest = -1
            if len(f.face_positions) == 1:
                closest = 0
            elif len(f.face_positions) > 0:
                closest_dist = 1000

            for i in range(len(f.face_positions)):
                dist = f.face_positions[i].pos.x*f.face_positions[i].pos.x + f.face_positions[i].pos.y*f.face_positions[i].pos.y + f.face_positions[i].pos.z*f.face_positions[i].pos.z
                if dist < closest_dist:
                    closest = i
                    closest_dist = dist

            if closest > -1:
                self.facePos = array([f.face_positions[closest].pos.x, f.face_positions[closest].pos.y, f.face_positions[closest].pos.z])
            else:
                rospy.logwarn('No faces were detected.')
                self.facePos = self.defaultLookatPoint
        else:
            rospy.logwarn('Not connected to the face server, cannot follow faces.')
            self.facePos = self.defaultLookatPoint

    ## Callback function for receiving gaze commands
    def do_gaze_action(self, command):
        #command = goal.action;
        if (self.doNotInterrupt.count(self.currentGazeAction) == 0):
            if (self.currentGazeAction != command or command == 'LOOK_AT_POINT'):
                self.isActionComplete = False
                if (command == 'LOOK_FORWARD'):
                    self.targetLookatPoint = self.defaultLookatPoint
                elif (command == 'LOOK_DOWN'):
                    self.targetLookatPoint = self.downLookatPoint
                elif (command == 'NOD'):
                    self.nNods = 5
                    self.startNod()
                elif (command == 'SHAKE'):
                    self.nShakes = 5
                    self.startShake()
                elif (command == 'NOD_ONCE'):
                    self.nNods = 5
                    self.startNod()
                elif (command == 'SHAKE_ONCE'):
                    self.nShakes = 5
                    self.startShake()
                elif (command == 'GLANCE_RIGHT_EE'):
                    self.startGlance(0)
                elif (command == 'GLANCE_LEFT_EE'):
                    self.startGlance(1)
                elif (command == 'LOOK_AT_POINT'):
                    self.targetLookatPoint = goal.point
                rospy.loginfo('\tSetting gaze action to: ' +
                        command)
                self.currentGazeAction = command

                while (not self.isActionComplete):
                    time.sleep(0.1)

    def isTheSame(self, current, target):
        diff = target - current
        dist = linalg.norm(diff)
        return (dist<0.0001)

    def filterLookatPosition(self, current, target):
        speed = 0.02
        diff = self.point2array(target) - self.point2array(current)
        dist = linalg.norm(diff)
        if (dist>speed):
            step = dist/speed
            return self.array2point(self.point2array(current) + diff/step)
        else:
            return target

    def startNod(self):
        self.prevTargetLookatPoint = self.targetLookatPoint
        self.prevGazeAction = str(self.currentGazeAction)
        self.nodCounter = 0
        self.targetLookatPoint = self.nodPositions[0]

    def startGlance(self, armIndex):
        self.prevTargetLookatPoint = self.targetLookatPoint
        self.prevGazeAction = str(self.currentGazeAction)
        self.glanceCounter = 0
        self.targetLookatPoint = self.getEEPos(armIndex)

    def startShake(self):
        self.prevTargetLookatPoint = self.targetLookatPoint
        self.prevGazeAction = str(self.currentGazeAction)
        self.shakeCounter = 0
        self.targetLookatPoint = self.shakePositions[0]

    def point2array(self, p):
        return array((p.x, p.y, p.z))

    def array2point(self, a):
        return Point(a[0], a[1], a[2])

    def getNextNodPoint(self, current, target):
        if (self.isTheSame(self.point2array(current), self.point2array(target))):
            self.nodCounter += 1
            if (self.nodCounter == self.nNods):
                self.currentGazeAction = self.prevGazeAction
                return self.prevTargetLookatPoint
            else:
                return self.nodPositions[self.nodCounter%2]
        else:
            return target

    def getNextGlancePoint(self, current, target):
        if (self.isTheSame(self.point2array(current), self.point2array(target))):
            self.glanceCounter = 1
            self.currentGazeAction = self.prevGazeAction
            return self.prevTargetLookatPoint
        else:
            return target

    def getNextShakePoint(self, current, target):
        if (self.isTheSame(self.point2array(current), self.point2array(target))):
            self.shakeCounter += 1
            if (self.shakeCounter == self.nNods):
                self.currentGazeAction = self.prevGazeAction
                return self.prevTargetLookatPoint
            else:
                return self.shakePositions[self.shakeCounter%2]
        else:
            return target

    def update(self):

        isActionPossiblyComplete = True
        if (self.currentGazeAction == 'FOLLOW_RIGHT_EE'):
            self.targetLookatPoint = self.getEEPos(0)

        elif (self.currentGazeAction == 'FOLLOW_LEFT_EE'):
            self.targetLookatPoint = self.getEEPos(1)

        elif (self.currentGazeAction == 'FOLLOW_FACE'):
            self.getFaceLocation()
            self.targetLookatPoint = self.facePos

        elif (self.currentGazeAction == 'NOD'):
            self.targetLookatPoint = self.getNextNodPoint(self.currentLookatPoint, self.targetLookatPoint)
            self.headGoal.min_duration = rospy.Duration(0.5)
            isActionPossiblyComplete = False;

        elif (self.currentGazeAction == 'SHAKE'):
            self.targetLookatPoint = self.getNextShakePoint(self.currentLookatPoint, self.targetLookatPoint)
            self.headGoal.min_duration = rospy.Duration(0.5)
            isActionPossiblyComplete = False;

        elif (self.currentGazeAction == 'GLANCE_RIGHT_EE' or self.currentGazeAction == 'GLANCE_LEFT_EE'):
            self.targetLookatPoint = self.getNextGlancePoint(self.currentLookatPoint, self.targetLookatPoint)
            isActionPossiblyComplete = False;

        self.currentLookatPoint = self.filterLookatPosition(self.currentLookatPoint, self.targetLookatPoint)
        if (self.isTheSame(self.point2array(self.headGoal.target.point), self.point2array(self.currentLookatPoint))):
            if (isActionPossiblyComplete):
                if (self.headActionClient.get_state() == GoalStatus.SUCCEEDED):
                    self.isActionComplete = True
        else:
            self.headGoal.target.point = self.currentLookatPoint
            self.headActionClient.send_goal(self.headGoal)

        time.sleep(0.02)

