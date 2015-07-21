import rospy
from threading import Lock
from std_msgs.msg import String


class SpeechMonitor():
    
    def __init__(self, speech_db):
        self._speech_db = speech_db
        self._received_command = None
        self._previous_command = None
        self._speech_lock = Lock()
        rospy.Subscriber('recognizer/output', 
            String, self.receive_sphinx_result)

    def receive_sphinx_result(self, data):
        self._speech_lock.acquire()
        self._previous_command = self._received_command
        self._received_command = data.data
        rospy.loginfo('Received command:' + self._received_command)
        self._speech_lock.release()

    def join(self, timeout=None):

        # First reset the command so we
        # start listening now and ignore the past
        self._speech_lock.acquire()
        self._previous_command = self._received_command
        self._received_command = None
        self._speech_lock.release()

        # Then wait until a command is received.
        # TODO: Timeout!
        is_command_received = False
        while (not is_command_received):
            self._speech_lock.acquire()
            if self._received_command is not None:
                is_command_received = True
                command_received = self._received_command
            self._speech_lock.release()
        return command_received

    def get_last_command(self):
        self._speech_lock.acquire()
        last_command = self._received_command
        self._speech_lock.release()
        return last_command

    def get_previous_command(self):
        self._speech_lock.acquire()
        previous_command = self._previous_command
        self._speech_lock.release()
        return previous_command
