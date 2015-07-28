#!/usr/bin/env python
import rospy
import robot_eup
from robot_eup.msg import RobotType

#############################################

def main_loop(robot):

 	choice = robot.ask_choice(message='How many people are ordering?', choices=['1', '2'])
 	if choice == '1':
 		choice = robot.ask_choice(
      		message='What would you like to eat?',
      		choices=['sandwich', 'spaghetti', 'hamburger'])
      	if choice == 'sandwich':
           	robot.display_message(message='OK.', duration=1)
           	robot.move_backward(duration=2)
      	elif choice == 'spaghetti':
           	robot.display_message(message='OK.', duration=1)
           	robot.move_backward(duration=2)
      	else:
           	robot.display_message(message='OK.', duration=1)
           	robot.move_backward(duration=2)

 	if choice =='2':
 		choice=robot.ask_choice(
      		message='Which person is ordering?',
      		choices=['1', '2'])
      	if choice == '1':
           	choice = robot.ask_choice(
           		message='What would you like to eat?',
           		choices=['sandwich', 'spaghetti', 'hamburger'])
           	if choice == 'sandwich':
           		robot.display_message(
                	message='OK.', duration=1)
                choice=robot.ask_choice(
                	message='Which person is ordering?',
                	choices=['2'])
                if choice == '2':
                    choice = robot.ask_choice(
                     	message='What would you like to eat?',
                     	choices=['sandwich', 'spaghetti', 'hamburger'])
                    if choice == 'sandwich':
                        robot.display_message(message='OK.', duration=1)
                        robot.move_backward(duration=2)
                    elif choice == 'spaghetti':
                        robot.display_message(message='OK.', duration=1)
                        robot.move_backward(duration=2)
                    else:
                        robot.display_message(message='OK.', duration=1)
                        robot.move_backward(duration=2)
	  	if choice =='2':
	  		choice = robot.ask_choice(
	    		message='What would you like to eat?',
	    		choices=['sandwich', 'spaghetti', 'hamburger'])
	        if choice == 'sandwich':
	            robot.display_message(message='OK.', duration=1)
	        elif choice == 'spaghetti':
	            robot.display_message(message='OK.', duration=1)
	        else:
	            robot.display_message(message='OK.', duration=1)


#############################################

if __name__ == '__main__':
    rospy.init_node('robot_eup_dialog')
    robot = robot_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
