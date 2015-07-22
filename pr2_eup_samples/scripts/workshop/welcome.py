#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########

def main_loop(robot):
	choice = ask_choice(message='Welcome to CyberFood! Please click okay when you are ready to be seated.', choices=['Okay'])
		if choice == 'Okay':
			choice = ask_choice(message='How many people are in your party?', choices=['1', '2', 'Other'])
				if choice == '1':
					say(text='Okay. Party of one, are you ready to be seated?')
					choice = ask_choice(message='Okay. Party of one, are you ready to be seated?', choices=['Yes', 'Not yet', 'Cancel')
						if choice == 'Yes':
							say(text='please follow me')
							display_message(message='Please follow me.', duration=8)
							go_to(location_name='Table1')
							say(text='please follow me')
							display_message(message='Please follow me.', duration=8)
							go_to(location_name='Table2')
					    		say(text='You may be seated')
							display_message(message='You may be seated. Your server will be with you shortly.', duration=8)
							say(text='Your sever will be with you shortly. Thank you')
							display_message(message='Thank you', duration=5)
							go_to(location_name='Door')
						else if choice == 'Not yet'
							say(text='Okay, I will wait. Press okay when you are ready to be seated')
							choice = ask_choice(message=''Okay, I will wait. Press okay when you are ready to be seated', choices=['Okay'])
								if choice == 'Okay'
									say(text='please follow me')
							    		display_message(message='Please follow me.', duration=8)
							    		go_to(location_name='Table1')
							    		say(text='please follow me')
							    		display_message(message='Please follow me.', duration=8)
							    		go_to(location_name='Table2')
							    		say(text='You may be seated')
									display_message(message='You may be seated. Your server will be with you shortly.', duration=8)
									say(text='Your sever will be with you shortly. Thank you')
									display_message(message='Thank you', duration=5)
									go_to(location_name='Door')
						else:
						    say(text='Restarting seating program, please wait.')
							display_message(message='Restarting seating program, please wait.', duration=8)
				else if choice == '2':
				    say(text='Okay. Party of two, are you ready to be seated?')
					choice = ask_choice(message='Okay. Party of two, are you ready to be seated?', choices=['Yes', 'Not yet', 'cancel')
						if choice == 'Yes':
							say(text='please follow me')
							display_message(message='Please follow me.', duration=8)
							go_to(location_name='Table2')
								say(text='please follow me')
							    	display_message(message='Please follow me.', duration=8)
								go_to(location_name='Table2')
						    		say(text='You may be seated')
								display_message(message='You may be seated. Your server will be with you shortly.', duration=8)
								say(text='Your sever will be with you shortly. Thank you')
								display_message(message='Thank you', duration=5)
								go_to(location_name='Door')
						else if choice == 'Not yet'
							say(text='Okay, I will wait. Press okay when you are ready to be seated')
							choice = ask_choice(message=''Okay, I will wait. Press okay when you are ready to be seated', choices=['Okay'])
								if choice == 'Okay'
									say(text='please follow me')
							    		display_message(message='Please follow me.', duration=8)
							    		go_to(location_name='Table2')
							    		say(text='You may be seated')
									display_message(message='You may be seated. Your server will be with you shortly.', duration=8)
									say(text='Your sever will be with you shortly. Thank you')
									display_message(message='Thank you', duration=5)
									go_to(location_name='Door')

						else:
						    say(text='Restarting seating program, please wait.')
							display_message(message='Restarting seating program, please wait.', duration=8)
				else:
				    say(text='I am sorry, but we only seat parties of one and two.')
					display_message(message='I am sorry, but we only seat parties of one and two.', duration=8)
					say(text='Restarting seating program, please wait.')
					display_message(message='Restarting seating program, please wait.', duration=8)

    robot.sleep(duration=5)


############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
