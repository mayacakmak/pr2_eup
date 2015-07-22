#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########

def main_loop(robot):
	#display_message("Would you like me to deliver something?")
	#wait_for_speech
    #robot.sleep(duration=5)

	i = 1
	while(i==1):
		choice = robot.ask_choice(
        	message='Would you like me to deliver something?',
        	choices=['Yes', 'No'])

    	if choice == 'Yes':
    		choice = robot.ask_choice(
        	message='Are you ready for me to go?',
        	choices=['Yes', 'No'])
        	if choice == 'Yes'
        		robot.go_to(location_name='Table1')
        		i = i + 1
        	else:
        		robot.sleep(duration=2)		
    	if choice == 'No':
    		robot.sleep(duration=4)
    	else:
    		robot.display_message(message='I did not hear that')

    while(i==2):
    	choice = robot.ask_choice(
        	message='Would you like me to go to the kitchen or the door?',
        	choices=['kitchen', 'door'])	
    		if choice == 'kitchen'
        		robot.go_to(location_name='kitchen')
        		i = i + 1
        	if choice == 'door':
        		robot.go_to(location_name='door')
        		i = i + 1

#############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
