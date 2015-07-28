#!/usr/bin/env python
import rospy
import robot_eup
from robot_eup.msg import RobotType

#############################################

def main_loop(robot):

    robot.say(text = 'Are you finished with your meal?')
    command = robot.wait_for_speech(
        commands=['yes', 'no', 'almost'])
    
    if command == 'yes':
        robot.say(text = 'Great. Please give me your plate.')
        robot.display_message(message='Waiting', duration = 5)
        robot.say(text = 'Did you enjoy your meal?')
        answer = robot.wait_for_speech()
        if answer == 'yes':
            robot.say(text = 'Good, I am glad')
        elif answer == 'no':
            robot.say(text = 'Oh no. I am sorry')
            robot.turn_right(duration = 1)
            robot.turn_left(duration = 1)
            robot.turn_right(duration =1)
            robot.turn_left(duration = 1)
        else:
            robot.say(text = 'I am sorry, I did not hear you')

        robot.say(text = 'Please scan your card by holding it in front of the camera. Press OK when done.')
        choice = robot.ask_choice(
            message='Press OK when done scanning card',
            choices=['OK'])
        robot.say(text = 'Thank you. Have a nice day.')
        robot.move(x = -2, y = 0, theta = 0, duration = 2)
    
    elif command == 'no' or command == 'almost':
        robot.say(text = 'Okay, I will be back later')
        robot.move_backward(duration = 3)
        robot.sleep(duration=10)
        robot.move_forward(duration = 3)
    else:
        robot.say(text = 'I could not hear you.')

    robot.sleep(duration=5)


#############################################

if __name__ == '__main__':
    rospy.init_node('robot_eup_dialog')
    robot = robot_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
