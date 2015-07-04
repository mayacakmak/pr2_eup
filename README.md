# pr2_eup
High-level APIs for end-user programming of the PR2 robot. 
Based on Justin Huang's [rapid_robot](https://github.com/jstnhuang/rapid_robot).

## Package overview
- `pr2_eup` contains the library itself.
- `pr2_eup_samples` contains examples of how the interface can be used.

## Installation
You need to install [meteor](https://www.meteor.com/).

## Running the test demo
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

### Test demo
On the PR2, run:
```
robot start
roslaunch todo_todo todo.launch map_file:=/your/map/file.yaml
```

On the PR2, go to `pr2_eup/web/rapid_web_interface` and type `meteor`. Visit `localhost:3000` in a web browser and full-screen it.

On your workstation, run:
```
rosrun pr2_eup_samples test_all.py
```

