from db import Db
import os
import roslib

class SoundDb(Db):
    def __init__(self, db_filename, sound_directory=None):
        Db.__init__(self, db_filename)
        if sound_directory is not None:
            self._sound_directory = sound_directory
        else:
            self._sound_directory = os.path.join(
                roslib.packages.get_pkg_dir('pr2_eup'), 'sounds', '')

    def set(self, name, filename=None):
        if filename is None:
            filename = name + '.wav'
        filename = os.path.join(self._sound_directory, filename)
        self._db[name] = filename
