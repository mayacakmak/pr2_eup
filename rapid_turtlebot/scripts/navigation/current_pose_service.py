#!/usr/bin/env python
from rapid_robot.srv import GetCurrentPose, GetCurrentPoseResponse
import rapid_turtlebot
import rospy
import tf

def get_current_pose(request, tf_listener):
    pose_stamped = rapid_turtlebot.navigation.get_current_pose(tf_listener)
    response = GetCurrentPoseResponse()
    response.pose_stamped = pose_stamped
    return response

if __name__ == '__main__':
    rospy.init_node('location_db')
    tf_listener = tf.TransformListener()
    def handle_request(request):
        return get_current_pose(request, tf_listener)
    rospy.Service('get_current_pose', GetCurrentPose, handle_request)
    rospy.spin()
