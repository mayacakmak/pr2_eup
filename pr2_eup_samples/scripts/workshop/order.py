#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########

def main_loop(robot):
    robot.sleep(duration=5)
    choice = ask_choice(message='How many people are ordering?', choices=['1', '2'])
    if choice == '1':
        choice = ask_choice(message='What would you like to eat?', choices=['sandwich', 'spaghetti', 'hamburger''])
        if choice == 'sandwich':
            display_message(message='OK.', duration=1)
        else if choice == 'spaghetti':
            display_message(message='OK.', duration=1)
        else if choice == 'hamburger':
            display_message(message='OK.', duration=1)
    if choice =='2':
        choice="ask_choice(message='Which person is ordering?', choices=['1', '2'])
        if choice == '1':
            choice = ask_choice(message='What would you like to eat?', choices=['sandwich', 'spaghetti', 'hamburger'])
            if choice == 'sandwich':
                display_message(message='OK.', duration=1)
                choice="ask_choice(message='Which person is ordering?', choices=['2])
                if choice == '2':
                    choice = ask_choice(message='What would you like to eat?', choices=['sandwich', 'spaghetti', 'hamburger'])
                    if choice = = 'sandwich':
                        display_message(message='OK.', duration=1)
                    else if choice = = 'spaghetti':
                        display_message(message='OK.', duration=1)
                    else if choice == 'hamburger':
                        display_message(message='OK.', duration=1)
            if choice == 'spaghetti':
                display_message(message='OK.', duration=1)
                choice="ask_choice(message='Which person is ordering?', choices=['2])
                if choice == '2':
                    choice = ask_choice(message='What would you like to eat?', choices=['sandwich', 'spaghetti', 'hamburger'])
                    if choice = = 'sandwich':
                        display_message(message='OK.', duration=1)
                    else if choice = = 'spaghetti':
                        display_message(message='OK.', duration=1)
                    else if choice == 'hamburger':
                        display_message(message='OK.', duration=1)
            if choice == 'hamburger':
                display_message(message='OK.', duration=1)
                choice="ask_choice(message='Which person is ordering?', choices=['2])
                if choice == '2':
                    choice = ask_choice(message='What would you like to eat?', choices=['sandwich', 'spaghetti', 'hamburger'])
                    if choice = = 'sandwich':
                        display_message(message='OK.', duration=1)
                    else if choice = = 'spaghetti':
                        display_message(message='OK.', duration=1)
                    else if choice == 'hamburger':
                        display_message(message='OK.', duration=1)



############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
