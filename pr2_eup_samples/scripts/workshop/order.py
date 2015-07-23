#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########

number_of_people = {'Table1':2, 'Table2':3}
orders = {'Table1':None, 'Table2':None}
delivered = {'Table1':False, 'Table2':False}

def main_loop(robot):

    robot.go_to(location_name='Kitchen')
    
    if orders['Table1'] is None or orders['Table2'] is None:

        robot.say(text='I am ready to take orders.')
        table_choice = robot.ask_choice(
            message='Which table should I take the order from?',
            choices=['Table1', 'Table2'])

        if orders[table_choice] is None:
            robot.go_to(location_name=table_choice)
            robot_line = 'Are you ready to order?'
            robot.say(text=robot_line)
            choice = robot.ask_choice_display_and_voice(message=robot_line,
                choices=['yes', 'no'])
            if choice == 'no':
                robot_line = 'Okay, I will come back later.'
                robot.say(text=robot_line)
                robot.display_message(message=robot_line)
                robot.go_to(location_name='Kitchen')
            else:
                robot_line = 'Okay, great.'
                robot.display_message(message=robot_line)
                robot.say(text=robot_line)
                robot.turn_right(duration=2)
                orders[table_choice] = 'one ' + take_order(robot)
                robot.turn_left(duration=2)
                if number_of_people[table_choice] == 2:
                    robot.turn_left(duration=2)
                orders[table_choice] = (orders[table_choice]
                    + ', one ' + take_order(robot))
                if number_of_people[table_choice] == 3:
                    robot.turn_left(duration=2)
                    orders[table_choice] = orders[table_choice] + ', one ' + take_order(robot)
                robot.turn_right(duration=2)
                robot_line = 'Great! You ordered ' + orders[table_choice] + '. Is that correct?'
                robot.say(text=robot_line)
                choice = robot.ask_choice_display_and_voice(message=robot_line,
                    choices=['yes', 'no'])
                if choice == 'no':
                    robot_line = 'Well, too bad because that is what I will bring.'
                else:
                    robot_line = 'Great.'
                robot.say(text=robot_line)
                robot.display_message(message=robot_line, duration=3)
                robot.display_message(message='Going to kitchen')
                robot.go_to(location_name='Kitchen')
                robot_line = 'Rosie the chef, we need ' + orders[table_choice] + ' for ' + table_choice
                robot.say(text=robot_line)
                robot.display_message(message=robot_line)
                robot.sleep(duration=5)
        else:
            robot_line = table_choice + ' already ordered.'
            robot.display_message(message=robot_line)
            robot.say(text=robot_line)
            robot.sleep(3)


    ## DELIVERY

    else:
        if delivered['Table1'] and delivered['Table2']:
            robot.say(text='Everything was delivered.')
            robot.sleep(duration = 30)
        else:
            robot.say(text='I am ready to deliver orders.')
            robot.sleep(duration=2)
            if not delivered['Table1']:
                robot.say(text='Table1 ordered: ' + orders['Table1'])
                robot.sleep(duration=3)
            if not delivered['Table2']:
                robot.say(text='Table2 ordered: ' + orders['Table2'])
                robot.sleep(duration=3)

            table_choice = robot.ask_choice(
                message='Which table should I deliver this?',
                choices=['Table1', 'Table2'])

            if not delivered[table_choice]:
                robot.go_to(location_name=table_choice)
                robot_line = 'Here is your food: ' + orders[table_choice] + '. Please take your plates and press okay.'
                robot.say(text=robot_line)
                robot.ask_choice(message=robot_line, choices=['OK'])
                robot_line = 'Enjoy your food!'
                robot.say(text=robot_line)
                robot.display_message(message=robot_line)
                delivered[table_choice] = True
                robot.go_to(location_name='Kitchen')
            else:
                robot.say(text='I have already delivered to ' + table_choice)
                robot.sleep(duration=2)


def take_order(robot):
    robot_line = 'What would you like to eat?'
    robot.say(text=robot_line)
    choice = robot.ask_choice_display_and_voice(message=robot_line,
                choices=['sandwich', 'spaghetti', 'hamburger', 'soup', 'salad'])
    robot_line = 'Okay'
    robot.say(text=robot_line)
    robot.display_message(message=robot_line)
    robot.sleep(duration=1)
    return choice

############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
