#!/usr/bin/env python
import rospy
import robot_eup
from robot_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########

def main_loop(robot):
    robot.say(
        text = 'Do you have more than 5 people in your party?')
    numPeople = robot.wait_for_speech(commands=['yes', 'no'])
    if numPeople == 'yes':
    	robot.say(text = 'Okay, follow me')
    	robot.sleep(duration=3)
    	robot.go_to(location_name = 'Table1')
    else:
    	robot.say(text = 'Okay, follow me')
    	robot.sleep(duration=3)
    	robot.go_to(location_name = 'Table2')
    robot.say(text = 'Would you like soup or salad?')
    appetizerChoice = robot.wait_for_speech(commands=['soup','salad'])
    robot.go_to(location_name = 'Kitchen')
    robot.say(text = 'They ordered' + appetizerChoice)
    robot.sleep(duration=20)
    if numPeople == 'yes':
        robot.go_to(location_name = 'Table1')
    else:
        robot.go_to(location_name = 'Table2')
    robot.say(text = 'Enjoy your meal!')

#############################################

if __name__ == '__main__':
    rospy.init_node('robot_eup_dialog')
    robot = robot_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
