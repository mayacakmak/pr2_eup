import actionlib
from move_base_msgs.msg import MoveBaseAction
from move_base_msgs.msg import MoveBaseGoal

def go_to(pose_stamped):
    """Simple version of go_to, which blocks until the robot arrives
    """
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()
    goal = MoveBaseGoal()
    goal.target_pose = pose_stamped
    client.send_goal(goal)
    client.wait_for_result()
