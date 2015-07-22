#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########
ask_choice "Should I go in a square or a circle?", yes = 
#sleep(3)
wait_for_speech()
    if raw_input() = "circles"
        say "swag"
        for i in range (36):
            move_forward (1)
            turn_right(0.5)
    else 
        say "squares are for squares"
        for i in range (36):
            move_forward(1)
            turn_right(0.5)
        
def main_loop(robot):

    robot.sleep(duration=5)


#############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
