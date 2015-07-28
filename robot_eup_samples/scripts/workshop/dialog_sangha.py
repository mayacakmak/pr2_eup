#!/usr/bin/env python
import rospy
import robot_eup
from robot_eup.msg import RobotType

#############################################

def main_loop(robot):

    go_to (location_name='Door')
    robot.display_message(
        message='Hello, my name is Chester. Welcome to French restaurant',
        duration=3)

    choice = robot.ask_choice(
        message= 'Tell me your favorite French Dessert, please?',
        choices=['Chocolate-Hazelnut', 'Creme Brulee',
        'Dark Roux', 'Creole Remoulade'])

    robot.say(text='Please wait until your order comes.')
    
    if choice == 'Chocolate-Hazelnut':
        robot.move(x=.8, y=.8, theta=.8, duration=5)
        robot.say(text='Rosie the chief, cook Chocolate-Hazelnut.')
    elif choice == 'Creme Brulee':
        robot.move(x=.8, y=.8, theta=.8, duration=5)
        robot.say(text='Rosie the chief, cook Creme Brulee.')
    elif choice == 'Dark Roux':
        robot.move(x=.8, y=.8, theta=.8, duration=5)
        robot.say(text='Rosie the chief, cook Dark Roux.')
    elif choice == 'Creole Remoulade':
        robot.move(x=.8, y=.8, theta=.8, duration=5)
        robot.say(text='Rosie the chief, cook Creole Remoulade.')
        
    robot.sleep(duration=20)
    robot.move(x=0, y=0, theta=0, duration=5)
    robot.say(text='Have you finish your meal?')
    command=wait_for_speech()
    
    if command=='command 1':
        robot.say(text='Please place your plates on me.')
    else if command =='command 2':
        move(x=.8, y=.8, theta=.8, duration=5)


#############################################

if __name__ == '__main__':
    rospy.init_node('robot_eup_dialog')
    robot = robot_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
