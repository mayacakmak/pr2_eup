from db import Db

class LocationDb(Db):
    def __init__(self, db_filename, tf_listener):
        Db.__init__(db_filename, tf_listener)
        self._tf_listener = tf_listener

    def set(self, name, pose_stamped):
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
