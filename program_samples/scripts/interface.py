import rospy
import rapid_robot as robot

if __name__ == '__main__':
    rospy.init_node('test_interface')
    robot.init()
    robot.interface.say_message('Hello', timeout=1)
    choice = robot.interface.ask_choice('Heads or tails?', ['Heads', 'Tails'])
    rospy.loginfo(choice)
    rospy.spin()
