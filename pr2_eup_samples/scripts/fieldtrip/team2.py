#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########

def main_loop(robot):

    robot.sleep(duration=5)
    #This is the definition for the choosing the color and the response for the fortune
def color_choice(robot):
    robot.ask.choice(
            message = "Choose a color: red, blue, green or yellow",
            choices = ["red","blue","green","yellow"])
                if choice == "red":
                    robot.say(text = "Good luck will come your way!")
                elif choice == "blue":
                    robot.say (text = "Happiness is the key to life, you will soon unlock your true potential ")
                elif choice == "green":
                    robot.say (text = "Go buy a lottery ticket")
                else:
                    robot.say (text = "Nope.")
#We are going to make a fortune telling robot that hopefully spins (if we have time).

#start script here

choice = robot.ask_choice(
    message = 'Choose a number between one and four',
    choices=["1", "2", "3", "4"])
    if choice == "1":
        color_choice(robot)
        #robot.ask.choice(
            #message = "Choose a color: red, blue, green or yellow",
            #choices = ["red","blue","green","yellow"])
             #   if choice == "red":
              #      robot.say("Good luck will come your way!")
               # elif choice == "blue":
                #    robot.say ("Happiness is the key to life, you will soon unlock your true potential ")
                #elif choice == "green":
                 #   robot.say ("Go buy a lottery ticket")
                #else:
                 #   robot.say ("Nope.")
    if choice == "2":
        color_choice(robot)
       # robot.ask.choice(
           # message = "Choose a color: red, blue, green or yellow",
            #choices = ["red","blue","green","yellow"])
             #   if choice == "red":
              #      robot.say("Good luck will come your way!")
               # elif choice == "blue":
                #    robot.say ("Happiness is the key to life, you will soon unlock your true potential ")
                #elif choice == "green":
                 #   robot.say ("Go buy a lottery ticket")
                #else:
                 #   robot.say ("Nope.")
    if choice == "3":
        color_choice(robot)
        #robot.ask.choice(
            #message = "Choose a color: red, blue, green or yellow",
            #choices = ["red","blue","green","yellow"])
                #if choice == "red":
                    #robot.say("Good luck will come your way!")
               # elif choice == "blue":
                   # robot.say ("Happiness is the key to life, you will soon unlock your true potential ")
                #elif choice == "green":
                   # robot.say ("Go buy a lottery ticket")
                #else:
                   # robot.say ("Nope.")
                
    if choice == "4":
        color_choice(robot)
        #robot.ask.choice(
            #message = "Choose a color: red, blue, green or yellow",
            #choices = ["red","blue","green","yellow"])
                #if choice == "red":
                    #robot.say("Good luck will come your way!")
                #elif choice == "blue":
                   # robot.say ("Happiness is the key to life, you will soon unlock your true potential ")
               # elif choice == "green":
                    #robot.say ("Go buy a lottery ticket")
                #else:
                    #robot.say ("Nope.")

def color_choice(robot):
    robot.ask.choice(
            message = "Choose a color: red, blue, green or yellow",
            choices = ["red","blue","green","yellow"])
                if choice == "red":
                    robot.say("Good luck will come your way!")
                elif choice == "blue":
                    robot.say ("Happiness is the key to life, you will soon unlock your true potential ")
                elif choice == "green":
                    robot.say ("Go buy a lottery ticket")
                else:
                    robot.say ("Nope.")
#############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot) 
    
