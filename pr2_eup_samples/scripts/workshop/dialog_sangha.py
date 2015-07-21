#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

#############################################

def main_loop(robot):

    robot.display_message(
        message='Hello, my name is Chester. Welcome to French restaurant',
        duration=3)

    choice = robot.ask_choice(
        message= 'Tell me your favorite menu, please?',
        choices=['Chocolate-Hazelnut', 'Creme Brulee',
        'Dark Roux', 'Creole Remoulade'])

    robot.say(text='Please wait until your order comes.')
    
    if choice == 'Chocolate-Hazelnut':
        robot.move(x=5, y=5, theta=5, duration=4)
        robot.say(text='Rosie the chief, cook Chocolate-Hazelnut.')
    elif choice == 'Creme Brulee':
        robot.move(x=5, y=5, theta=5, duration=4)
        robot.say(text='Rosie the chief, cook Creme Brulee.')
    elif choice == 'Dark Roux':
        robot.move(x=5, y=5, theta=5, duration=4)
        robot.say(text='Rosie the chief, cook Dark Roux.')
    elif choice == 'Creole Remoulade':
        robot.move(x=5, y=5, theta=5, duration=4)
        robot.say(text='Rosie the chief, cook Creole Remoulade.')


#############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
