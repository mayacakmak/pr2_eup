#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

#############################################

def main_loop(robot):

    robot.display_message(
        message='Please place the item you want to deliver.',
        duration=5)

    choice = robot.ask_choice(
        message='Where should I go?',
        choices=['A', 'B', 'C'])

    if choice == 'A':
        robot.move(x=0.5, y=0.0, theta=0.75, duration=3)
    elif choice == 'B':
        robot.move(x=0.0, y=0.5, theta=-0.25, duration=3)
    else:
        robot.move(x=0.25, y=0.25, theta=0.75, duration=3)

    robot.say(text='Here is your delivery.')


#############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_example1')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
