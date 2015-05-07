from .. import rapid_ros
from geometry_msgs.msg import PoseStamped
import rospy
import tf


def get_current_pose():
    try:
        pose_stamped = PoseStamped()
        pose_stamped.header.frame_id = 'base_footprint'
        pose_stamped.header.stamp = rospy.Time(0)
        pose_stamped.pose.position.x = 0
        pose_stamped.pose.position.y = 0
        pose_stamped.pose.position.z = 0
        pose_stamped.pose.orientation.w = 1
        pose_stamped.pose.orientation.x = 0
        pose_stamped.pose.orientation.y = 0
        pose_stamped.pose.orientation.z = 0
        current_location = rapid_ros.tf_listener.transformPose('/map',
                                                               pose_stamped)
        return current_location
    except Exception as e:
        rospy.logerr('Failed to get current pose in /map frame.')
        rospy.logerr(e)
        return None
