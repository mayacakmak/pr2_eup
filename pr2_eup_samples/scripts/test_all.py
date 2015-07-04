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



if __name__ == '__main__':

    rospy.init_node('test_pr2_eup')
    robot = pr2_eup.RobotFactory().build()
    while not rospy.is_shutdown():
        test_everything(robot)