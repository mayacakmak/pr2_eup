from interface import Interface
from location_db import LocationDb
from move_base_msgs.msg import MoveBaseAction
from navigation import Navigation
from rapid_robot.msg import InterfaceParams
from rapid_robot.msg import InterfaceSubmission
import actionlib
import rospy
import tf


class RobotFactory(object):
    def build(self):
        """Builds a robot object.

        Returns: Robot. A robot object.
        """
        # Navigation
        move_base_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        tf_listener = tf.TransformListener()
        navigation = Navigation('base_footprint', 'map', tf_listener, move_base_client)

        # Interface
        interface_publisher = rospy.Publisher('rapid_robot/interface/interface_params',
                             InterfaceParams)
        interface = Interface(interface_publisher)

        # Location DB

        robot = Robot(interface, navigation, tf_listener)
        return robot

class Robot(object):
    def __init__(self, interface, navigation, tf_listener):
        self.interface = interface
        self.navigation = navigation
        self._tf_listener = tf_listener

    def location_db(self, db_filename):
        """Returns a location database.

        The location DB file can be any Python shelve file that maps strings
        to geometry_msgs/PoseStamped messages.

        Args:
          db_filename: string. The location on the filesystem of DB file.

        Returns: LocationDb.
        """
        return LocationDb(db_filename, self._tf_listener)

    @staticmethod
    def wait_for_event(function, timeout):
        """Calls the given function, but bounds the time by the given timeout.
    
        The function will be called with no arguments. If it returns before the
        timeout, then this function will return event_complete=True and the result
        of the function. Otherwise, this function will return (False, None).

        Args:
          function: function. A no-argument function to call.
          timeout: float. The time, in seconds, to wait for the function to return.
        """
        import signal
    
        class TimeoutError(Exception):
            pass
    
        def handler(signum, frame):
            raise TimeoutError()
    
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(timeout)
        event_complete = False
        result = None
        try:
            result = function()
            event_complete = True
        except TimeoutError as exc:
            event_complete = False
            result = None
        finally:
            signal.alarm(0)
    
        return event_complete, result
