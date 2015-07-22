#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

#############################################

def main_loop(robot):

    choice = robot.ask_choice(
        message='Welcome to CyberFood! Please click okay when you are ready to be seated.',
        choices=['Okay'])
    if choice == 'Okay':
        choice = robot.ask_choice(
            message='How many people are in your party?',
            choices=['1', '2', '3', '4', '5', '6'])
        if choice == '1':
            robot.say(text='please follow me')
            robot.display_message(
                message='Please follow me.',
                duration=8)
            robot.move_forward(duration=5)
            robot.turn_right(duration=1)
            robot.move_forward(duration=5)
            robot.turn_right(duration=1)
            robot.move_forward(duration=10)
            robot.say(text='You may be seated')
            robot.display_message(message='You may be seated. Your server will be with you shortly.', duration=8)
            robot.say(text='Your sever will be with you shortly')
            robot.display_message(message=':D', duration=5)
            robot.move_backward(duration=10)
            robot.turn_left(duration=1)
            robot.move_backward(duration=5)
            robot.turn_left(duration=1)
            robot.move_backward(duration=5)
        elif choice == '2':
            robot.say(text='please follow me')
            robot.display_message(message='Please follow me.', duration=8)
            robot.move_forward(duration=5)                
            robot.turn_left(duration=1)
            robot.move_forward(duration=5)
            robot.turn_left(duration=1)
            robot.move_forward(duration=10)
            robot.say(text='You may be seated')
            robot.display_message(message='You may be seated. Your server will be with you shortly.', duration=8)
            robot.say(text='Your sever will be with you shortly')
            robot.display_message(message=':D', duration=5)
            robot.move_backward(duration=10)
            robot.turn_right(duration=1)
            robot.move_backward(duration=5)
            robot.turn_right(duration=1)
            robot.move_backward(duration=5)
        elif choice == '3':
            robot.say(text='please follow me')
            robot.display_message(message='Please follow me.', duration=8)
            robot.move_forward(duration=10)
            robot.turn_left(duration=1)
            robot.move_forward(duration=5)
            robot.say(text='You may be seated')
            robot.display_message(message='You may be seated. Your server will be with you shortly.', duration=8)
            robot.say(text='Your sever will be with you shortly')
            robot.display_message(message=':D', duration=5)
            robot.move_backward(duration=5)
            robot.turn_right(duration=1)
            robot.move_backward(duration=10)
        elif choice == '4':
            robot.say(text='please follow me')
            robot.display_message(
                message='Please follow me.', duration=8)
            robot.move_forward(duration=10)
            robot.turn_right(duration=1)
            robot.move_forward(duration=5)
            robot.say(text='You may be seated')
            robot.display_message(
                message='You may be seated. Your server will be with you shortly.',
                duration=8)
            robot.say(text='Your sever will be with you shortly')
            robot.display_message(message=':D',
                duration=5)
            robot.move_backward(duration=5)
            robot.turn_left(duration=1)
            robot.move_backward(duration=10)
        elif choice == '5':
            robot.say(text='please follow me')
            robot.display_message(message='Please follow me.', duration=8)
            robot.move_forward(duration=5)
            robot.turn_left(duration=1)
            robot.move_forward(duration=10)
            robot.say(text='You may be seated')
            robot.display_message(message='You may be seated. Your server will be with you shortly.', duration=8)
            robot.say(text='Your sever will be with you shortly')
            robot.display_message(message=':D', duration=5)
            robot.move_backward(duration=10)
            robot.turn_right(duration=1)
            robot.move_backward(duration=5)
        else:
            robot.say(text='please follow me')
            robot.display_message(message='Please follow me.', duration=8)
            robot.move_forward(duration=5)
            robot.turn_right(duration=1)
            robot.move_forward(duration=10)
            robot.say(text='You may be seated')
            robot.display_message(message='You may be seated. Your server will be with you shortly.', duration=8)
            robot.say(text='Your sever will be with you shortly')
            robot.display_message(message=':D', duration=5)
            robot.move_backward(duration=10)
            robot.turn_left(duration=1)
            robot.move_backward(duration=5)


#############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
