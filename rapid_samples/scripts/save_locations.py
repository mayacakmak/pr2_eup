#!/usr/bin/env python
from geometry_msgs.msg import PoseStamped
import argparse
import rapid_robot as robot
import rospy
import tf


def parse_command(command_input):
    command_parts = command_input.split(' ')
    if len(command_parts) == 0:
        return None, None
    command = command_parts[0]
    name = None
    if len(command_parts) >= 2:
        name = ' '.join(command_parts[1:])
    return command, name


def ask_command():
    print 'Set current location as {name}: set {name}'
    print 'Get location {name}:            get {name}'
    print 'List locations:                 list'
    print 'Remove location {name}:         remove {name}'
    print 'Go to location {name}:          goto {name}'
    print 'Quit:                           quit'
    command_input = raw_input('Enter command: ')
    return parse_command(command_input)


def set_location(db, name, location):
    db.set_location(name, location)


def print_location(db, name):
    location = db.get_location(name)
    if location is None:
        rospy.logerr('Failed to get location {}'.format(name))
    print location


def list_locations(db):
    locations = db.get_all_locations()
    for name, pose_stamped in locations:
        print name


def remove_location(db, name):
    db.remove_location(name)


def go_to_location(pose_stamped):
    robot.navigation.go_to(pose_stamped)


if __name__ == '__main__':
    rospy.init_node('save_locations')
    robot.init()

    parser = argparse.ArgumentParser()                                                                                              
    parser.add_argument('filename',
                        metavar='FILE',                                                                                             
                        type=str,
                        help='Python shelve DB containing locations.')                                                              
    args = parser.parse_args(args=rospy.myargv()[1:])

    db = robot.navigation.LocationDb(args.filename)

    while True:
        command, name = ask_command()
        if command == 'set':
            location = robot.navigation.get_current_pose()
            if location is None:
                continue
            set_location(db, name, location)
        elif command == 'get':
            print_location(db, name)
        elif command == 'list':
            list_locations(db)
        elif command == 'remove':
            remove_location(db, name)
        elif command == 'goto':
            pose_stamped = db.get_location(name)
            go_to_location(pose_stamped)
        elif command == 'quit':
            break
        else:
            print
            continue
        print
