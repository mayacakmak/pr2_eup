#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########

def main_loop(robot):
    robot.say(
        text = 'Do you have more than 5 people in your party?')
    numPeople = robot.wait_for_speech(['yes', 'no'])
    if numPeople == 'yes':
    	robot.say(text = 'Okay, follow me')
    	robot.sleep(3)
    	go_to(location_name = 'Table1')
    else:
    	robot.say(text = 'Okay, follow me')
    	robot.sleep(3)
    	go_to(location_name = 'Table2')
    robot.say(text = 'Would you like soup or salad?')
    appetizerChoice = robot.wait_for_speech(['soup','salad'])
    robot.go_to(location_name = 'Kitchen')
    robot.say(text = 'They ordered' + appetizerChoice)
    robot.sleep(20)
    if numPeople == 'yes':
        go_to(location_name = 'Table1')
    else:
        go_to(location_name = 'Table2')
    robot.say(text = 'Enjoy your meal!')

#############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
