from interface import Interface
from location_db import LocationDb
from navigation import Navigation
from event_monitor import EventMonitor
from pr2_eup.msg import InterfaceParams
from pr2_eup.msg import InterfaceSubmission
import rospy
import tf
import time


class RobotFactory(object):
    def build(self):
        """Builds a robot object.

        Returns: Robot. A robot object.
        """
        # Navigation
        tf_listener = tf.TransformListener()
        navigation = Navigation('base_footprint', 'map', tf_listener)

        # Interface
        interface = Interface()

        # Speech


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
    def start(action_function, kwargs={}):
        monitor = EventMonitor(
            target=action_function,
            kwargs=kwargs)
        monitor.start()
        return monitor

    @staticmethod
    def do(action_function, kwargs={}):
        event_monitor = Robot.start(action_function, kwargs)
        #while event_monitor.is_alive():
        #    time.sleep(0.05)
        #return event_monitor.get_result()
        return event_monitor.join()


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
