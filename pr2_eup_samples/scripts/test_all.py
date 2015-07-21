#!/usr/bin/env python
import argparse
import rospy
import pr2_eup
from pr2_eup.robot import Robot
from pr2_eup.msg import RobotType


def test_all(robot):

    Robot.do(robot.interface.display_message,
        message='Say test microphone')

    command = Robot.wait(robot.speech_monitor)

    Robot.do(robot.interface.display_message,
        message='you said:' + command,
        duration=3)
    
    Robot.do(robot.interface.ask_choice,
        message='Press Start when you are ready:',
        choices=['Start'])
    Robot.do(robot.voice.play_sound,
        sound_name='sound2')
    Robot.do(robot.interface.display_message,
        message='Robot moving forward')
    Robot.do(robot.navigation.move_forward,
        duration=3)
    Robot.do(robot.interface.display_message,
        message='Robot will move in circle.',
        duration=4,
        has_countdown=True)
    Robot.do(robot.navigation.move,
        x=0.5,
        y=0.0,
        theta=0.75,
        duration=4)
    Robot.do(robot.voice.say,
        text='Done moving.')
    choice = Robot.do(robot.interface.ask_choice,
        message='What should the head do?',
        choices=['NOD', 'SHAKE'])
    #Robot.do(robot.head.do_gaze_action,
    #    command=choice)


if __name__ == '__main__':

    rospy.init_node('test_pr2_eup')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        test_all(robot)