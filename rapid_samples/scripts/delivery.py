#!/usr/bin/env python
import rapid_robot as robot

def main():
    location_db = robot.navigation.LocationDb('~/data/rapid_robot/test.db')
    location = robot.interface.ask_choice('Please choose a location.', location_db.get_all_locations())
    robot.interface.ask_choice('Load the items and press "Ready".', ['Ready'])
    robot.navigation.go_to(location)

    def items_collected():
        robot.interface.ask_choice('Here are your items. Press "Done" once you have your items.', ['Done'])
    result = robot.wait_for_event(items_collected, 10)
    if result == 'timeout':
        robot.interface.display_message('Timed out.', time=10)
        robot.navigation.go_to('home')
    else:
        robot.interface.display_message('Going home now.', time=10)
        robot.navigation.go_to('home')


if __name__ == '__main__':
    main()
