#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########

number_of_people = {'Table1':2, 'Table2':3}
has_table_paid = {'Table1':False, 'Table2':False}
dessert_orders = {'Table1':None, 'Table2':None}

def main_loop(robot):
	
	if has_table_paid['Table1'] and has_table_paid['Table2']:
		robot.say(text='Both tables have paid. We are done for today Rosie.')
		robot.sleep(duration=10)
	else:
		robot.display_message(message='Going to kitchen')
		robot.go_to(location_name='Kitchen')
		robot.say(text='I am ready to take payments.')
		table_choice = robot.ask_choice(
			message='Which table should I take payments from?',
			choices=['Table1', 'Table2'])
		robot.display_message(message='Going to ' + table_choice)
		robot.go_to(location_name=table_choice)

		if dessert_orders[table_choice] is None:
		# Ask only if desert was not previously ordered
			robot_line = 'Would you like some dessert?'
			robot.say(text=robot_line)
			dessert = robot.ask_choice_display_and_voice(message=robot_line,
				choices=['yes', 'no'])
			if dessert == 'yes':
				dessert_orders[table_choice] = take_dessert_order(robot)
				robot_line = 'Great! One ' + dessert_orders[table_choice] + ' coming up.'
				robot.say(text=robot_line)
				robot.display_message(message=robot_line)
				robot.go_to(location_name='Kitchen')
				robot.say(text=robot_line)
				robot_line = 'Rosie the chef, we need one ' + dessert_orders[table_choice] + ' for ' + table_choice
				robot.say(text=robot_line)
				robot.display_message(message=robot_line)
				robot.sleep(duration=5)
				robot.ask_choice(message='Press OK when desert is ready.', choices=['OK'])
				robot.go_to(location_name=table_choice)
				robot_line = 'Here is your ' + dessert_orders[table_choice] + '. Please take your plates and press OK.'
				robot.say(text=robot_line)
				robot.ask_choice(message=robot_line, choices=['OK'])
				robot_line = 'Enjoy your dessert!'
				robot.say(text=robot_line)
				robot.display_message(message=robot_line)
				robot.go_to(location_name='Kitchen')
				return
		
		if dessert_orders[table_choice] is not None or dessert == 'no':
			# Start payment process
			
			got_response1 =  False
			while not got_response1:
				robot_line = 'Are you finished with your meal? Answers are, yes, no, or, almost.'
				robot.say(text=robot_line)
				finished_meal = robot.ask_choice_display_and_voice(message=robot_line,
					choices = ['yes', 'no', 'almost'])
				if finished_meal == 'yes':
					robot.say(text = 'Great!')
					robot.sleep(duration = 5)
					got_response = False
					while not got_response:
						robot_line = 'Did you enjoy your meal? Answers are yes or no.'
						robot.say(text = robot_line)
						enjoy_answer = robot.ask_choice_display_and_voice(message=robot_line,
							choices = ['yes', 'no'])
						if enjoy_answer == 'yes':
							robot.say(text = 'Good, I am glad.')
							robot.sleep(duration=1)
							got_response = True
						elif enjoy_answer == 'no':
							robot.say(text = 'Oh no. I am sorry')
							got_response = True
							robot.turn_right(duration = 1)
							robot.turn_left(duration = 1)
							robot.turn_right(duration =1)
							robot.turn_left(duration = 1)
						else:
							robot.say(text = 'I am sorry, I did not hear you. ' +
								'Please speak loudly and quickly.')
							robot.sleep(duration=3)

					got_response2 = False
					while not got_response2:
						robot_line = 'Are you ready to pay? Answers are, yes, or, no'
						robot.say(text = robot_line)
						ready_answer = robot.ask_choice_display_and_voice(message=robot_line,
							choices = ['yes', 'no'])

						if ready_answer == 'yes':
							if dessert_orders[table_choice] is not None:
								total = '$15'
							else:
								total = '$10'

							robot.say(text = 'Okay, your total will be displayed on the screen. ' +
								'Please scan your card by holding it in front of the camera and press OK.')
							
							robot.ask_choice(message='Your total is ' + str(total) + 
								'. Please scan your card by holding it in front of the camera and press OK.',
								choices=['OK'])
							has_table_paid[table_choice] = True
							robot.say(text = 'Thank you. Tips are appreciated. ' +
								'Use the screen to leave a tip.')
							tip_amount = robot.ask_choice(message='Select a tip amount', 
								choices = ['$0', '$1', '$2'])
							robot.say(text = 'Thank you. Please follow me to the door')
							robot.sleep(2)
							robot.go_to(location_name = 'Door')
							robot.say(text = 'Please leave now. If you are not out in 10 seconds ' +
								'I will self-destruct. Good bye.')
							robot.sleep(duration=2)
							robot.display_message(message='Going back to kitchen.')
							robot.go_to(location_name='Kitchen')
							got_response2 = True
							got_response1 = True
						elif ready_answer == 'no'
							robot.say(text = 'Okay, but you will have to pay sometime. I will stay here until you do.')
							robot.sleep(duration = 7)
						else:
							robot.sleep(duration=5)

				elif finished_meal == 'no':
					robot.say(text='Okay, I will be back soon. Please do not leave the restaurant.')
					robot.sleep(duration=3)
					robot.go_to(location_name = 'Kitchen')
					robot.sleep(duration = 5)
					robot.go_to(location_name = table_choice)
				elif finished_meal == 'almost':
					robot.sleep(duration=5)
		else:
			robot.say(text = 'Sorry, I did not hear you. Please speak loudly and quickly')
			robot.sleep(duration=3)

	robot.display_message(message='Restarting payment process.', duration=5)


def take_dessert_order(robot):
    robot_line = ('What would you like for dessert? We have chocolate hazelnut, ' +
    	'creme brulee, dark roux, and creole remoulade.')
    robot.say(text=robot_line)
    choice = robot.ask_choice_display_and_voice(message=robot_line,
    	choices=['chocolate-hazelnut', 'creme-brulee', 'dark-roux', 'creole-remoulade'])
    robot_line = 'Okay'
    robot.say(text=robot_line)
    robot.display_message(message=robot_line)
    robot.sleep(duration=1)
    return choice


############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
