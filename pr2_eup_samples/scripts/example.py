#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType
from pr2_eup.robot import Robot

#############################################

def main_loop(robot):
    Robot.do(robot.interface.display_message,
        message='Hello, my name is Chester.',
        duration=3)
    
    choice = Robot.do(robot.interface.ask_choice, 
        message='What should I do?',
        choices=['Dance', 'Sing'])

    if choice == 'Dance':
        Robot.do(robot.navigation.turn_right,
            duration=1)
        Robot.do(robot.navigation.turn_left,
            duration=1)
        Robot.do(robot.navigation.turn_right,
            duration=1)
        Robot.do(robot.navigation.turn_left,
            duration=1)
    else:
        Robot.do(robot.voice.play_sound,
            sound_name='sound1')
        Robot.do(robot.voice.play_sound,
            sound_name='sound2')
        Robot.do(robot.voice.play_sound,
            sound_name='sound3')

    Robot.do(robot.voice.say,
        text='Now, lets speak. What should I do?')
    
    command = Robot.wait(robot.speech_monitor)
        
    if command == 'command1':
        Robot.do(robot.navigation.move,
            x=0.5,
            y=0.0,
            theta=0.75,
            duration=4)
    elif command == 'command2':
        Robot.do(robot.navigation.move,
            x=0.0,
            y=0.5,
            theta=-0.75,
            duration=4)
    else:
        Robot.do(robot.voice.say,
            text='I could not hear you.')

    #choice = Robot.do(robot.interface.ask_choice,
    #    message='What should the head do?',
    #    choices=['NOD', 'SHAKE'])
    #Robot.do(robot.head.do_gaze_action,
    #    command=choice)        

#############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_example')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
