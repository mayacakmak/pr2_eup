#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

#############################################

def main_loop(robot):

    robot.display_message(
        message = 'Hello, my name is Chester and I am a transport robot.',
        duration = 5)
    choice = robot.ask_choice(
        message = 'Please place your delivery on top of me and click OK',
        choices = ['OK'])
    choice2 = robot.ask_choice(
        message = 'Please choose a location',
        choices =  ['A', 'B', 'C'])
    if choice2 == 'A':
        robot.move(x = -2, y=0, theta = 0, duration = 1)
        choice3 = robot.ask_choice(
            message = 'Please take your delivery and press OK',
            choices = ['OK'])
        robot.say(text = 'Thank you. Have a nice day')
        robot.move(x=2,  y=0, theta = 0, duration = 1)
    elif choice2 == 'B':
        robot.move(x = -3, y = 1, theta = 0, duration= 1)
        choice4 = robot.ask_choice(
            message = 'Please take your delivery and press OK',
            choices = ['OK'])
        robot.say(text = 'Thank you. Have a nice day')
        robot.move(x = 3, y = -1, theta = 0, duration = 1)
    else:
        robot.move(x = 5, y = -3, theta = 1, duration = 1)
        choice5 = robot.ask_choice(
            message = 'Please take your delivery and press OK',
            choices = ['OK'])
        robot.say(text = 'Thank you. Have a nice day')
        robot.move(x=-5, y =3, theta = -1, duration = 1)


#############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_example1')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)