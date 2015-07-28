#!/usr/bin/env python
import rospy
import robot_eup
from robot_eup.msg import RobotType

#############################################

def main_loop(robot):

    robot.display_message(
        message='place item',
        duration=3)
    choice=robot.ask_choice(message='what should I do ',
        choices=['A','B', 'C'])

    if choice =='A':
        robot.move_forward (duration=1)
        choice = robot.ask_choice(
            message= 'take delivery, press ok',
            choices=['ok'])
        robot.move_backward(duration=1)

    elif choice == 'B':
        robot.turn_left(duration=2)
        choice = robot.ask_choice(
            message= 'take delivery, press ok',
            choices=['ok'])
        robot.turn_right (duration=2)

    elif choice=='C':
        robot.move_forward(duration=3)
        choice = robot.ask_choice(
            message= 'take delivery, press ok',
            choices=['ok'])
        robot.move_backward(duration=3)


#############################################

if __name__ == '__main__':
    rospy.init_node('robot_eup_delivery')
    robot = robot_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
