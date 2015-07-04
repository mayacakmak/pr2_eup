#!/usr/bin/env python
import argparse
import rospy
import pr2_eup
from pr2_eup.robot import Robot

def test_everything(robot):
    
    Robot.do(robot.interface.ask_choice,
        message='Press Start when you are ready:',
        choices=['Start']);
    Robot.do(robot.interface.display_message,
        message='Moving forward')
    Robot.do(robot.navigation.move_forward,
        duration=3)
    Robot.do(robot.interface.display_message,
        message='Next will move in ..',
        duration=4,
        has_countdown=True)

    choice = Robot.do(robot.interface.ask_choice, message='Press Start when you are ready:', choices=['continue'])

    navigation_monitor = Robot.start(robot.navigation.move_forward, duration=2)
    
    Robot.wait(navigation_monitor)
    robot.navigation.turn_left, {'duration':'2'}
    robot.interface.display_message('Moved forward..', duration=1)

    #robot.navigation.move_forward(2)

    #robot.navigation.turn_right(2)
    #robot.interface.display_message('Turned right..', timeout=1)

    #robot.navigation.turn_left(2)
    #robot.interface.display_message('Turned left..', timeout=1)

    #choice = robot.interface.ask_choice('Which direction should the robot move?.', ['forward', 'backward'])


if __name__ == '__main__':

    rospy.init_node('test_pr2_eup')
    robot = pr2_eup.RobotFactory().build()
    while not rospy.is_shutdown():
        test_everything(robot)