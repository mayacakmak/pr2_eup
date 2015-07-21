#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

#############################################

def main_loop(robot):

    robot.display_message(
        message='Please place item on me.',
        duration=4)
    choice = robot.ask_choice(
        message='Where should I bring it?',
        choices=['A', 'B', 'C'])
    if choice == 'A':
        robot.turn_right(duration=1)
        robot.move_forward(duration=2)
        robot.play_sound(sound_name='sound1')
        choice = robot.ask_choice(
            message='Please take item and then press okay.',
            choices=['Okay'])
        if choice == 'Okay':
            robot.move_backward(duration=2)
            robot.turn_left(duration=1)
            robot.play_sound(sound_name='sound2')
    elif choice == 'B':
        robot.move_forward(duration=1)
        robot.turn_left(duration=1)
        robot.move_forward(duration=1)
        robot.play_sound(sound_name='sound1')
        choice = robot.ask_choice(
            message='Please take item and then press okay.',
            choices=['Okay'])
        if choice == 'Okay':
            robot.move_backward(duration=1)
            robot.turn_right(duration=1)
            robot.move_backward(duration=1)
            robot.play_sound(sound_name='sound2')
    else:
        robot.turn_left(duration=1)
        robot.move_forward(duration=2)
        robot.play_sound(sound_name='sound1')
        choice = robot.ask_choice(
            message='Please take item and then press okay.',
            choices=['Okay'])
        if choice == 'Okay':
            robot.move_backward(duration=2)
            robot.turn_right(duration=1)
            robot.play_sound(sound_name='sound2')

#############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_delivery')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
        