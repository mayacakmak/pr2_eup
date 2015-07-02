#!/usr/bin/env python
import argparse
import rospy
import pr2_eup

def main(robot, location_db):
    while True:
      do_delivery(robot, location_db)

def do_delivery(robot, location_db):
    location_names = [name for name, location in location_db.get_all_locations()]
    location = robot.interface.ask_choice('Please choose a location.', location_names)
    rospy.loginfo('Delivering item to {}'.format(location))
    choice = robot.interface.ask_choice('Load the items and press "Ready".', ['Ready'])
    pose_stamped = location_db.get_location(location)
    robot.navigation.go_to(pose_stamped)

    def items_collected():
        robot.interface.ask_choice('Here are your items. Press "Done" once you have your items.', ['Done'])
    rospy.loginfo('Waiting for items to be picked up.')
    delivery_complete, result = robot.wait_for_event(items_collected, 10)
    home_pose = location_db.get_location('Home')
    if not delivery_complete:
        rospy.loginfo('Timed out, heading home.')
        robot.interface.say_message('Timed out.', timeout=10)
        robot.navigation.go_to(home_pose)
    else:
        rospy.loginfo('Delivery complete. Heading home.')
        robot.interface.say_message('Going home now.', timeout=10)
        robot.navigation.go_to(home_pose)


if __name__ == '__main__':
    rospy.init_node('delivery')
    robot = pr2_eup.RobotFactory().build()
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        metavar='FILE',
                        type=str,
                        help='Python shelve DB containing locations.')
    args = parser.parse_args(args=rospy.myargv()[1:])
    location_db = robot.location_db(args.filename)
    main(robot, location_db)
