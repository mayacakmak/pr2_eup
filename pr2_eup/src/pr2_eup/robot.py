from interface import Interface
from location_db import LocationDb
from sound_db import SoundDb
from navigation import Navigation
from voice import Voice
from head import Head
from event_monitor import EventMonitor
from pr2_eup.msg import InterfaceParams
from pr2_eup.msg import InterfaceSubmission
import rospy
import tf
import time
from threading import Thread

TURTLEBOT = 'Chester'
PR2 = 'Rosie'

class RobotFactory(object):

    def build(self, robot_name):
        """Builds a robot object.

        Returns: Robot. A robot object.
        """

        # Interface
        interface = Interface(robot_name)

        # Navigation
        tf_listener = tf.TransformListener()
        location_db = LocationDb('dummy', tf_listener)
        navigation = Navigation(location_db, tf_listener)

        # Speech and sounds
        sound_db = SoundDb('dummy')
        voice = Voice(sound_db)

        # Head
        # TODO: Head action database?
        if robot_name == PR2:
            head = Head()
        else:
            head = None

        # Arms
        # TODO: Arm action database?
        # TODO: Arm action execution
        #arms = Arms()

        robot = Robot(robot_name, interface, navigation, voice, head)
        return robot

class Robot(object):
    def __init__(self, robot_name, interface, navigation, voice, head):
        self.interface = interface
        self.navigation = navigation
        self.voice = voice
        self.head = head

    def start_robot(self):
        update_thread = Thread(target=self._run)
        update_thread.start()

    @staticmethod
    def start(action_function, **kwargs):
        monitor = EventMonitor(
            target=action_function,
            kwargs=kwargs)
        monitor.start()
        return monitor

    @staticmethod
    def wait(action_monitor):
        return action_monitor.join()

    @staticmethod
    def do(action_function, **kwargs):
        monitor = EventMonitor(
            target=action_function,
            kwargs=kwargs)
        monitor.start()
        return Robot.wait(monitor)

    def _run(self):
        while not rospy.is_shutdown():
            self._update()
            time.sleep(0.05)

    def _update(self):

        if self.head is not None:
            self.head.update()