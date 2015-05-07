import rospy
from rapid_robot.srv import GetCurrentPose

def get_current_pose():
    get_current_pose = rospy.ServiceProxy('rapid_robot/navigation/get_current_pose', GetCurrentPose)
    get_current_pose.wait_for_service()
    response = get_current_pose()
    return response.pose_stamped
