from rapid_robot.msg import InterfaceParams
from rapid_robot.msg import InterfaceSubmission
import json
import rospy

#_default_timer = None # Timer to go back to default screen.
_publisher = rospy.Publisher('rapid_robot/interface/interface_params', InterfaceParams)

#def _set_timer(duration, callback):
#    global _default_timer
#    _default_timer = rospy.Timer(duration, callback, oneshot=True)
#
#def _reset_timer():
#    global _default_timer
#    if _default_timer is not None:
#        _default_timer.shutdown()
#
#def _schedule_default(duration):
#    def callback(event):
#        display_default()
#    _set_timer(rospy.Duration(duration), callback)

def display_default():
    global _publisher
    message = InterfaceParams()
    message.interface_type = 'default'
    _publisher.publish(message)

def ask_choice(message, choices, timeout=None):
    global _publisher
    #_reset_timer()
    msg = InterfaceParams()
    msg.interface_type = 'ask_choice'
    msg.keys = ['message', 'choices']
    msg.values = [message, json.dumps(choices)]
    _publisher.publish(msg)
    submission = rospy.wait_for_message('rapid_robot/interface/interface_submission', InterfaceSubmission, timeout)
    if submission is None or submission.interface_type != 'ask_choice' or len(submission.values) == 0:
        return None
    display_default()
    return submission.values[0]

def display_message(message, seconds=None):
    global _publisher
    #_reset_timer()
    msg = InterfaceParams()
    msg.interface_type = 'display_message'
    msg.keys = ['message']
    msg.values = [message]
    _publisher.publish(msg)
    if seconds is not None:
        rospy.sleep(seconds)
    display_default()
