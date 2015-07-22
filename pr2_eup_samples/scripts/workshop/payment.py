#!/usr/bin/env python
import rospy
import pr2_eup
from pr2_eup.msg import RobotType

######### ADD YOUR PROGRAM BELOW ###########

#!/List
#!/•	Payment
#!/o	Are you done?
#!/	Yes take plate
#!/o	Did you enjoy your meal
#!/o	Anything else
#!/o	Okay, please pay—credit only
#!/o	Show total on screen
#!/o	Scan card
#!/o	Thank you. Tips are appreciated. This job doesn’t pay me enough.
#!/o	Screen for tips
#!/o	Please follow me to the door
#!/o	Go to door
#!/o	Have a nice day… get out. 


def main_loop(robot):

    robot.sleep(duration=5)


############################################

if __name__ == '__main__':
    rospy.init_node('pr2_eup_dialog')
    robot = pr2_eup.RobotFactory().build(RobotType.TURTLEBOT)
    robot.start_robot()
    while not rospy.is_shutdown():
        main_loop(robot)
