#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########

def main_loop(robot):

    robot.sleep(duration=5)
#We are going to make a fortune telling robot that hopefully spins (if we have time).

#start script here

choice = robot.ask_choice(
    message = 'What is your favorite color?',
    choices=["red", "blue", "green", "yellow"])
   
   
   
    if choice == "red":
        say("Good luck will come your way!")
    elif choice == "blue":
        say ("hggkhadowhlasgnv")
    elif choice == "green":
        say ("khahofbwocn")
    else:
        say ("haosdfofd")


#############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot) 
    
