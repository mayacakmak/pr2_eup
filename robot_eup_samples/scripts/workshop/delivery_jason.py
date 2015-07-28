#!/usr/bin/env python
import rospy
import robot_eup
from robot_eup.msg import RobotType

#############################################

def main_loop(robot):

    robot.display_message(
        message="My name is Chester, where do I deliver my package?",
        duration=3)
    choice = robot.ask_choice(
        message="Should I go to location:",
        choices=['A: Dorms', 'B: Lecture Hall', 'C: The Hub'])
    if choice == 'A: Dorms':
        robot.turn_right(duration=3)
        robot.move_forward(duration=3)
        robot.turn_left(duration=3)
        robot.move_forward(duration=3)

        choice1 = robot.ask_choice(
            message="Please take your delivery",
            choices=["ok"])
        if choice1 == "ok":
            robot.turn_left(duration=3)
            robot.move_backward(duration=3)
            robot.turn_right(duration=3)
            robot.move_backward(duration=3)

    elif choice == 'B: Lecture Hall':
        robot.turn_left(duration=1)
        robot.move_forward(duration=1)
        robot.turn_right(duration=1)
        robot.move_forward(duration=1)

        choice1 = robot.ask_choice(
            message="Please take your delivery",
            choices=["ok"])
        if choice1 == "ok":
            robot.turn_right(duration=1)
            robot.move_backward(duration=1)
            robot.turn_left(duration=1)
            robot.move_backward(duration=1)

    elif choice == 'C: The Hub':
        robot.turn_right(duration=2)
        robot.move_forward(duration=2)
        robot.turn_left(duration=2)
        robot.move_forward(duration=2)

        choice1 = robot.ask_choice(
            message="Please take your delivery",
            choices=["ok"])
        if choice1 == "ok":
            robot.turn_left(duration=2)
            robot.move_backward(duration=2)
            robot.turn_right(duration=2)
            robot.move_backward(duration=2)
    else:
        robot.play_sound(sound_name='sound1')

#############################################

if __name__ == '__main__':
    rospy.init_node('robot_eup_delivery')
    robot = robot_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)