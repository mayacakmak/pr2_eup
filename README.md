# rapid_robot
High-level APIs for controlling mobile ROS robots.

![Build status](https://travis-ci.org/jstnhuang/rapid_robot.svg "Build status")

## Package overview
- `rapid_robot` contains the library itself.
- `rapid_samples` contains examples of how the interface can be used.
- `rapid_turtlebot` contains supporting files for running a delivery demo on a Turtlebot.

## Installation
You need to install [meteor](https://www.meteor.com/).

## Running the delivery demo
To run the delivery demo, you need:

1. A map of the environment ([see tutorial](http://wiki.ros.org/turtlebot_navigation/Tutorials/Build%20a%20map%20with%20SLAM))
2. A database of locations on the map

### Building a database of locations
A location database is a Python [shelve](https://docs.python.org/2/library/shelve.html) file mapping strings to PoseStamped messages. You can generate one with `save_locations.py` in rapid_samples.

Run save_locations.py with the name of a database file. If it doesn't exist, it will be created:
```
python save_locations.py ~/data/locations.db
```

Type `set Home` to save the current position as "Home". Drive the robot around using teleop, and save as many locations as you like.

### Delivery demo
On the Turtlebot, run:
```
roslaunch turtlebot_bringup minimal.launch
roslaunch rapid_turtlebot turtlebot.launch map_file:=/your/map/file.yaml
```

On the Turtlebot, go to `rapid_robot/web/rapid_web_interface` and type `meteor`. Visit `localhost:3000` in a web browser and full-screen it.

On your workstation, run:
```
roslaunch rapid_turtlebot visualize_turtlebot.launch
python delivery.py ~/data/locations.db
```

## Generated documentation
- [Code API](http://jstnhuang.github.io/rapid_robot/namespaces.html)
- [Message documentation](http://jstnhuang.github.io/rapid_robot/index-msg.html) (not part of the API)
