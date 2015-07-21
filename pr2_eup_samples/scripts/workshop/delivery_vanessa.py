#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

#############################################

def main_loop(robot):

    robot.display_message(message="Please place item on me", duration=3)
    choice = robot.ask_choice(message="where do you want me to take it?", choices=['A', 'B', 'C'])
    if choice == 'A':
        robot.turn_right(duration=1)
        robot.move_forward(duration=1)
        robot.turn_left(duration=1)
        robot.move_forward(duration=1)

        choice1 = robot.ask_choice(message="Please take delivery", choices=["ok"])
        if choice1 == "ok":
            robot.turn_left(duration=1)
            robot.move_backward(duration=1)
            robot.turn_right(duration=1)
            robot.move_backward(duration=1)
        robot.display_message(message='please take item')

    elif choice == 'B':
        robot.turn_left(duration=1)
        robot.move_forward(duration=1)
        robot.turn_right(duration=1)
        robot.move_forward(duration=1)

        choice1 = robot.ask_choice(message="Please take delivery", choices=["ok"])
        if choice1 == "ok":
            robot.turn_right(duration=1)
            robot.move_backward(duration=1)
            robot.turn_left(duration=1)
            robot.move_backward(duration=1)
        robot.display_message(message='please take item')

    elif choice == 'C':
        robot.turn_right(duration=2)
        robot.move_forward(duration=2)
        robot.turn_left(duration=2)
        robot.move_forward(duration=2)

        choice1 = robot.ask_choice(message="Please take delivery", choices=["ok"])
        if choice1 == "ok":
            robot.turn_left(duration=2)
            robot.move_backward(duration=2)
            robot.turn_right(duration=2)
            robot.move_backward(duration=2)
        robot.display_message(message='please take item')
    else:
        robot.play_sound(sound_name='sound1')


#############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_delivery')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
