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
    print 'Quit:                           quit'
    command_input = raw_input('Enter command: ')
    return parse_command(command_input)


def get_current_location(tf_listener):
    try:
        pose_stamped = PoseStamped()
        pose_stamped.header.frame_id = 'base_footprint'
        pose_stamped.header.stamp = rospy.Time(0)
        pose_stamped.pose.position.x = 0
        pose_stamped.pose.position.y = 0
        pose_stamped.pose.position.z = 0
        pose_stamped.pose.orientation.w = 1
        pose_stamped.pose.orientation.x = 0
        pose_stamped.pose.orientation.y = 0
        pose_stamped.pose.orientation.z = 0
        current_location = tf_listener.transformPose('/map', pose_stamped)
        return current_location
    except:
        rospy.logerr('Failed to get current location.')
        return None


def set_location(db, name, location):
    db.set_location(name, location)


def print_location(db, name):
    location = db.get_location(name)
    if location is None:
        rospy.logerr('Failed to get location {}'.format(name))
    print location


def list_locations(db):
    locations = db.get_all_locations()
    for location in locations:
        print location.name, location.pose_stamped


def remove_location(db, name):
    db.remove_location(name)


if __name__ == '__main__':
    rospy.init_node('save_locations')
    parser = argparse.ArgumentParser()                                                                                              
    parser.add_argument('filename',
                        metavar='FILE',                                                                                             
                        type=str,
                        help='Python shelve DB containing locations.')                                                              
    args = parser.parse_args(args=rospy.myargv()[1:])

    tf_listener = tf.TransformListener()
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
        elif command == 'quit':
            break
        else:
            print
            continue
        print
