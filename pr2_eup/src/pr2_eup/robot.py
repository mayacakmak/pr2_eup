from interface import Interface
from location_db import LocationDb
from sound_db import SoundDb
from navigation import Navigation
from command_db import CommandDb
from speech_monitor import SpeechMonitor
from voice import Voice
from head import Head
from event_monitor import EventMonitor
from pr2_eup.msg import InterfaceParams
from pr2_eup.msg import InterfaceSubmission
from pr2_eup.msg import RobotType
import rospy
import tf
import time
from threading import Thread

class RobotFactory(object):

    def build(self, robot_type):
        """Builds a robot object.

        Returns: Robot. A robot object.
        """

        # Interface
        interface = Interface(robot_type)

        # Navigation
        tf_listener = tf.TransformListener()
        location_db = LocationDb('location_db', tf_listener)
        navigation = Navigation(robot_type, location_db, tf_listener)

        # Speech and sounds
        sound_db = SoundDb('sound_db')
        for i in range(10):
            sound_db.set('sound' + str(i+1))
        voice = Voice(sound_db)

        command_db = CommandDb('command_db')
        speech_monitor = SpeechMonitor(command_db)

        # Head
        # TODO: Head action database?
        if robot_type == RobotType.PR2:
            head = Head()
        else:
            head = None

        # Arms
        # TODO: Arm action database?
        # TODO: Arm action execution
        #arms = Arms()

        robot = Robot(robot_type,
            interface, navigation, voice, head,
            speech_monitor, tf_listener)

        return robot

class Robot(object):
    def __init__(self, robot_type,
        interface, navigation, voice, head,
        speech_monitor, tf_listener):

        self.robot_type = robot_type
        self.interface = interface
        self.navigation = navigation
        self.voice = voice
        self.head = head
        self.speech_monitor = speech_monitor
	self.tf_listener = tf_listener
        #self.voice.play_sound('sound10')


    def location_db(self, db_filename):
        """Returns a location database.
        The location DB file can be any Python shelve file that maps strings
        to geometry_msgs/PoseStamped messages.
        Args:
          db_filename: string. The location on the filesystem of DB file.
        Returns: LocationDb.
        """
        return LocationDb(db_filename, self.tf_listener)

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
    def wait_multiple(action_monitors):
        while True:
            for i in range(len(action_monitors)):
                monitor = action_monitors[i]
                if not monitor.is_alive():
                    rospy.loginfo('Monitors ' + str(i)
                        + ' detected an event')
                    return monitor.get_result()
            rospy.sleep(0.1)

    @staticmethod
    def sleep(duration):
        rospy.sleep(duration)

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

    ### Function wrappers

    def display_message(self, **kwargs):
        Robot.do(self.interface.display_message,
            **kwargs)
    def ask_choice(self, **kwargs):
        return Robot.do(self.interface.ask_choice,
            **kwargs)
    def turn_right(self, **kwargs):
        Robot.do(self.navigation.turn_right,
            **kwargs)
    def turn_left(self, **kwargs):
        Robot.do(self.navigation.turn_left,
            **kwargs)
    def move_forward(self, **kwargs):
        Robot.do(self.navigation.move_forward,
            **kwargs)
    def move_backward(self, **kwargs):
        Robot.do(self.navigation.move_backward,
            **kwargs)
    def move(self, **kwargs):
        Robot.do(self.navigation.move,
            **kwargs)
    ## TODO: rename this as start_play_sound b/c that how it behaves
    def play_sound(self, **kwargs):
        Robot.do(self.voice.play_sound,
            **kwargs)
    ## TODO: rename this as start_say b/c that how it behaves
    def say(self, **kwargs):
        Robot.do(self.voice.say,
            **kwargs)
    def wait_for_speech(self, commands=None):
        self.speech_monitor.set_command_list(commands)
        self.speech_monitor.start()
        received_command = Robot.wait(self.speech_monitor)
        self.speech_monitor.set_command_list(None)
        return received_command

    def ask_choice_display_and_voice(self, message, choices):
        self.speech_monitor.set_command_list(choices)
        self.speech_monitor.start()
        interface_monitor = Robot.start(self.interface.ask_choice,
            message=message,
            choices=choices)
        result = Robot.wait_multiple([interface_monitor, self.speech_monitor])
        self.speech_monitor.set_command_list(None)
        return result

    def go_to(self, **kwargs):
        is_simulation = False
        if is_simulation:
            rospy.loginfo('Ignoring go_to')
        else:
            Robot.do(self.navigation.go_to_location,
                **kwargs)
