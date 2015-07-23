#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########

def main_loop(robot):
	choice = robot.ask_choice(message='Welcome to CyberFood! '+
		'Please click okay to be seated.',
		choices=['Okay'])
	if choice == 'Okay':
		robot_line = 'How many people are in your party?'
		robot.say(text=robot_line)
		party_size = robot.ask_choice_display_and_voice(
			message=robot_line,
			choices=['two', 'three', 'other'])
		if party_size == 'two' or party_size == 'three':
			robot_line = ('Okay. Party of '+ party_size +
			', are you ready to be seated?')
			robot.say(text=robot_line)
			choice = robot.ask_choice_display_and_voice(
				message=robot_line,
				choices=['yes', 'not-yet', 'cancel'])

			if choice == 'yes':
				take_person_to_table(robot, party_size)

			elif choice == 'not-yet':
				robot_line = ('Okay, I will wait. ' +
					'Press okay when you are ready to be seated')
				robot.say(text=robot_line)
				robot.ask_choice(
					message=robot_line, choices=['Okay'])
				if choice == 'Okay':
					take_person_to_table(robot, party_size)

			else:
				robot_line = 'Restarting seating program, please wait.'
				robot.say(text=robot_line)
				robot.display_message(
					message=robot_line, duration=8)
		else:
			robot_line = 'I am sorry, but we only seat parties of two and three.'
			robot.say(text=robot_line)
			robot.display_message(message=robot_line, duration=8)
			robot_line = 'Restarting seating program, please wait.'
			robot.say(text=robot_line)
			robot.display_message(message=robot_line, duration=8)

	robot.sleep(duration=5)


def take_person_to_table(robot, party_size):

	robot_line = 'please follow me'
	robot.say(text=robot_line)
	robot.display_message(message=robot_line,
		duration=8)
	if party_size == 'two':
		robot.go_to(location_name='Table2')
	else:
		robot.go_to(location_name='Table1')

	robot.say(text='You may be seated')
	robot.display_message(
		message='You may be seated. ' +
		'Your server will be with you shortly.',
		duration=8)
	robot.say(text='Your server will be with you shortly. ' +
		'Thank you')
	robot.display_message(message='Thank you',
		duration=5)
	robot.go_to(location_name='Door')


############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
