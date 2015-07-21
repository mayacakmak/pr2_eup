import rospy
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient


class Voice:
    def __init__(self, sound_db):
        self._sound_client = SoundClient()

    def play_sound(self, sound_name):
        '''Plays the requested sound.

        Args:
            requested_sound (str): Unique name of the sound in the sound database.
        '''
        sound_filename = sound_db.get(sound_name)
        Response._sound_client.playWave(sound_filename)

        # TODO: Make sure this returns when it is done playing the sound.

    def say(self, text):
        '''Send a TTS (text to speech) command.
        Args:
            text (str): The speech to say.
        '''
        self._sound_client.say(text)

        # TODO: When is speech done? This should return
        # when it is done saying the whole text.
