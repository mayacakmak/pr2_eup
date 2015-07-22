#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########

def main_loop(robot):
    robot.display_message(
        message='Welcome to the restaurant. How many people?',
        duration=3)
        command = robot.wait_for_speech()
    robot.sleep(duration=5)


############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
