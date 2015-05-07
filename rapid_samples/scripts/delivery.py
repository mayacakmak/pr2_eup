#!/usr/bin/env python
import rospy
import rapid_robot as robot

def main():
    location_db = robot.navigation.LocationDb('/home/jstn/data/rapid_robot/test.db')
    location_names = [name for name, location in location_db.get_all_locations()]
    location = robot.interface.ask_choice('Please choose a location.', location_names)
    robot.interface.ask_choice('Load the items and press "Ready".', ['Ready'])
    pose_stamped = location_db.get_location(location)
    robot.navigation.go_to(pose_stamped)

    robot.interface.display_message('Going home now.', seconds=10)
    pose_stamped = location_db.get_location('start')
    robot.navigation.go_to(pose_stamped)
    #def items_collected():
    #    robot.interface.ask_choice('Here are your items. Press "Done" once you have your items.', ['Done'])
    #result = robot.wait_for_event(items_collected, 10)
    #if result == 'timeout':
    #    robot.interface.display_message('Timed out.', time=10)
    #    robot.navigation.go_to('home')
    #else:
    #    robot.interface.display_message('Going home now.', time=10)
    #    robot.navigation.go_to('home')


if __name__ == '__main__':
    rospy.init_node('delivery')
    robot.init()
    main()
