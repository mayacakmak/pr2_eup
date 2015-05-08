import rospy
import shelve


class LocationDb(object):
    def __init__(self, db_filename, tf_listener):
        self._db = shelve.open(db_filename)
        self._tf_listener = tf_listener

    def get_all_locations(self):
        return self._db.items()

    def get_location(self, name):
        if name in self._db:
            return self._db[name]
        else:
            return None

    def remove_location(self, name):
        if name in self._db:
            del self._db[name]
            return True
        else:
            return False

    def set_location(self, name, pose_stamped):
        if rospy.resolve_name(pose_stamped.header.frame_id) != '/map':
            pose_stamped.header.stamp = rospy.Time(0)
            try:
                pose_stamped = self._tf_listener.transformPose(
                    '/map', pose_stamped)
            except:
                rospy.logerr(
                    '[LocationDb] TF error while setting location {}'.format(
                        name))
                return False

        self._db[name] = pose_stamped
        return True
