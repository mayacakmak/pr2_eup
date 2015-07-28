#!/usr/bin/env python
import rospy
import robot_eup
from robot_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########
def main_loop(robot):

    robot.say(
        text="Should I go in a square or a circle or a triangle?")
    command = robot.wait_for_speech(
        commands=['square', 'circle', 'triangle', 'no-thank-you'])
    for i in range(3):
        if command == 'circle':
            robot.say(text="swag")
            for i in range (36):
                robot.move_forward (duration=1)
                robot.turn_right(duration=0.5)
                i= i+3
        elif command == 'square':
            robot.say(text="squares are for squares")
            for i in range (36):
                robot.move_forward(duration=1)
                robot.turn_right(duration=0.5)
                i = i+3
        elif command == 'triangle':
            robot.say(text='illuminati, so do you have a password? ha ha')
            for i in range (3):
                robot.move_forward(duration=2)
                robot.turn_right(duration=6)
                i = i+3
        else:
            robot.say(
                text="I speak in rhymes, these times, crimes, mimes, I am a rapping winna, what's for dinna")

        robot.sleep(duration=5)


#############################################

if __name__ == '__main__':
    rospy.init_node('robot_eup_dialog')
    robot = robot_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
