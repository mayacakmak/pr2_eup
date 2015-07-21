#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

#############################################

def main_loop(robot):

    robot.say(text='Welcome to the restaurant. How many people?')
    robot.display_message(
        message='Welcome to the restaurant. How many people?',
        duration=3)
    command = robot.wait_for_speech()
    robot.say(text='Okay, come with me')
    robot.move(x=0.5, y= 0.0, theta=0.5, duration=4)


#############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
