#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########

def main_loop(robot):
    choice = robot.ask_choice(
        message = 'are we going on a trip?'
        choices = ['yes', 'no'])
    if choice == 'yes':
        robot.go_to(location_name = 'Door')
        robot.say("Let's go")
    elif choice == 'no':
        robot.say("you don't have a choice")
        robot.say("I don't take no for an answer")
        robot.move(5, 0, 6.3, 3)
    else:
        robot.say("I don't understand")
        robot.play_sound(sound_name = 'sound5')

    robot.sleep(duration=5)


#############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
