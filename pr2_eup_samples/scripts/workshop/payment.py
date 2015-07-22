#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########

#!/List
#!/•	Payment
#!/o	Are you done?
#!/	Yes take plate
#!/o	Did you enjoy your meal
#!/o	Anything else
#!/o	Okay, please pay—credit only
#!/o	Show total on screen
#!/o	Scan card
#!/o	Thank you. Tips are appreciated. This job doesn’t pay me enough.
#!/o	Screen for tips
#!/o	Please follow me to the door
#!/o	Go to door
#!/o	Have a nice day… get out. 

def main_loop(robot):
    if dessert == ‘Yes’
	robot.go_to(location_name = ‘Table1’)
else
	robot.say(text = ‘Are you finished with your meal? Answers are, yes, no, or, almost’)
	finished_meal = robot.wait_for_speech(commands = [‘Yes’, ‘No’, ‘Almost’])
	while not got_response1:
if finished_meal = ‘Yes’
		robot.say(text = ‘Great. Please give me your plate.’)
		robot.sleep(duration = 5)
		robot.say(text = “Did you enjoy your meal? Answers are, yes, or, no.’)
		enjoy_answer = robot.wait_for_speech(commands = [‘Yes’, ‘No’])
			while not got_response; 
			if enjoy_answer == ‘Yes’
				robot.say(text = ‘Good, I’m glad.’)	
				got_response = True
			else if enjoy_answer == ‘No’
				robot.say(text = “Oh no. I’m sorry’)
				got_response = True
			robot.turn_right(duration = 1)
			robot.turn_left(duration = 1)
			robot.turn_right(duration =1)
			robot.turn_left(duration = 1)
		else
robot.say(text = ‘I’m sorry, I didn’t hear you. Please speak loudly and slowly.’)
			got_response = False
	robot.say(text = ‘Are you ready to pay? Answers are, yes, or, no’)
	y = robot.wait_for_speech([‘Yes’, ‘No’])
		while not got_response2
		if y == ‘Yes’
			robot.say(text = ‘Okay, your total will be displayed on the screen.’)
			if dessert == ‘Yes’
				robot.display_message(‘$15’, duration = 8)
			if dessert == ‘No’
				robot.display_message(‘$10’, duration = 8)
robot.say(text = ‘Please scan your card by holding it in front of the camera’)
robot.sleep(duration = 3)
robot.say(text = ‘Thank you. Tips are appreciated. Use the screen to leave a tip’)
			c = robot.ask_choice(‘Select a tip amount’, choices = [‘$0’, ‘$1’, ‘$2’])
			robot.say(text = ‘Thank you. Please follow me to the door’)
			robot.go_to(location_name = ‘Door’)
robot.say(text = ‘Please leave now. If you are not out in 10 seconds I will self-destruct)
			got_response2 = True
		else if  y== ‘No’
			robot.say(‘Okay, I will be back soon. Please do not leave the restaurant.’)
			robot.go_to(location_name = ‘Kitchen’)
			robot.sleep(duration = 5)
			robot.go_to(location_name = ‘Table1’)
			got_response2 = False
		else
robot.say(text = ‘Sorry, I didn’t hear you. Please speak loudly and slowly’)
			got_response2 = False
	got_response1 = ‘true’
	
	else if finished_meal == ‘No’
		robot.say(text = ‘Okay, I’ll be back later’)
		robot.go_to(location_name = ‘Kitchen’)
		robot.sleep(duration = 10)
		robot.go_to(location_name = ‘Table’)
		got_response1 = False
	else
		say(text = “Sorry, I didn’t hear you. Please speak loudly and slowly)
		got_response1 = False

    robot.sleep(duration=5)


############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
