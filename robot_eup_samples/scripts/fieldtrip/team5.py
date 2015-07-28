#!/usr/bin/env python
import rospy
import robot_eup
from robot_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########

def main_loop(robot):

    
    choice = robot.ask_choice(
        message = 'are we going on a trip?',
        choices = ['yes', 'no'])
    if choice == 'yes':
        robot.say(text="let's go!")
        robot.go_to(location_name = 'Kitchen')
    elif choice == 'no':
        robot.say(text="you don't have a choice")
        robot.sleep(duration=2)
        robot.say(text="I don't take no for an answer")
        robot.move(x=0.4, y=0, theta=0.63, duration=3.1)
    else:
        robot.say(text="I don't understand you.")
        robot.play_sound(sound_name = 'sound5')
        
        

    robot.sleep(duration=5)


#############################################

if __name__ == '__main__':
    rospy.init_node('robot_eup_dialog')
    robot = robot_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
