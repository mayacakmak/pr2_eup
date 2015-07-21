#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

#############################################

def main_loop(robot):

    robot.display_message(
        message='Hello, my name is Chester. Please put A, B, and C.',
        duration=3)
    choice = robot.ask_choice(
        message='Where should I deliver?',
        choices=['A', 'B', 'C',])
    robot.say(text='Now, I will deliver to you.')
    if choice == 'A':
        robot.move(x=0.5, y=0.0, theta=0.75, duration=4)
        robot.say(text='Take delivery.')
        robot.move(x=0.0, y=0.0, theta=0.0, duration=4)
    elif choice == 'B':
        robot.move(x=1.0, y=2.0, theta=-0.75, duration=4)
        robot.say(text='Take delivery.')
        robot.move(x=0.0, y=0.0, theta=0.0, duration=4)
    elif choice == 'C':
        robot.move(x=0.0, y=-2.0, theta=2.0, duration=4)
        robot.say(text='Take delivery.')
        robot.move(x=0.0, y=0.0,  theta=0.0, duration=4)
    else:
        robot.say('I could not hear you.')


#############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_delivery')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
