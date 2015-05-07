import rospy
from rapid_robot.srv import GetAllLocations
from rapid_robot.srv import GetLocation
from rapid_robot.srv import RemoveLocation
from rapid_robot.srv import SetLocation
from rapid_robot.srv import SetLocationDb


class LocationDb(object):
    def __init__(self, db_filename):
        self._get_all_locations = rospy.ServiceProxy(
            'rapid_robot/navigation/get_all_locations', GetAllLocations)
        self._get_location = rospy.ServiceProxy(
            'rapid_robot/navigation/get_location', GetLocation)
        self._remove_location = rospy.ServiceProxy(
            'rapid_robot/navigation/remove_location', RemoveLocation)
        self._set_location = rospy.ServiceProxy(
            'rapid_robot/navigation/set_location', SetLocation)
        self._set_location_db = rospy.ServiceProxy(
            'rapid_robot/navigation/set_location_db', SetLocationDb)
        self._set_location_db.wait_for_service()
        self._set_location_db(db_filename=db_filename)

    def get_all_locations(self):
        response = self._get_all_locations()
        return response.locations

    def get_location(self, name):
        response = self._get_location(name=name)
        if response.success:
            return response.pose_stamped
        else:
            return None

    def remove_location(self, name):
        response = self._remove_location(name=name)
        return response.success

    def set_location(self, name, pose_stamped):
        response = self._set_location(name=name, pose_stamped=pose_stamped)
        return response.success
