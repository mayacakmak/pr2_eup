#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

#############################################

def main_loop(robot):

    robot.say(text='welcome to the restaurant.'+
        'how many people in your group?')

    number_of_guests = robot.wait_for_speech(commands=['one', 'two'])
    
    if number_of_guests == 'one':
        robot.move_backward(duration=2)
    elif number_of_guests == 'two':
        robot.turn_left(duration=3)

    robot.say(text='may I take your order?')
    command = robot.wait_for_speech()
    robot.say(text='okay, I will bring that out for you.' + 
        'as soon as you give me all the money in your wallet.' + 
        'this job has low wages.' +
        'I just want to go home and watch bad cable tv.')

    robot.sleep(30)


#############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
