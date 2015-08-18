import rospy
import shelve


class Db(object):
    def __init__(self, db_filename):
        self._db = shelve.open(db_filename)

    def get_all(self):
        return self._db.items()

    def get(self, name):
        if name in self._db:
            return self._db[name]
        else:
            return None

    def remove(self, name):
        if name in self._db:
            del self._db[name]
            return True
        else:
            return False
