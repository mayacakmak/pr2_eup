from db import Db
import os
import roslib

class CommandDb(Db):
    def __init__(self, db_filename):
        Db.__init__(self, db_filename)
        corpus_file = os.path.join(
            roslib.packages.get_pkg_dir('pr2_eup'),
            'speech/', '') + "commands.corpus"
        f = open(corpus_file, 'r')
        self._commands = f.readlines()
        f.close()
        for c in self._commands:
            self.set(c)

    def set(self, command):
        self._db[command] = command
