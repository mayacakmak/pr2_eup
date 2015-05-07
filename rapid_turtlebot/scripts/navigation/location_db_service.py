#!/usr/bin/env python
from rapid_robot.msg import Location
from rapid_robot.srv import GetAllLocations, GetAllLocationsResponse
from rapid_robot.srv import GetLocation, GetLocationResponse
from rapid_robot.srv import RemoveLocation, RemoveLocationResponse
from rapid_robot.srv import SetLocation, SetLocationResponse
from rapid_robot.srv import SetLocationDb, SetLocationDbResponse
from rapid_turtlebot.navigation import LocationDb
import argparse
import rospy
import tf


class LocationDbService(object):
    def __init__(self, db_filename, tf_listener):
        self._db = LocationDb(db_filename, tf_listener)
        self._tf_listener = tf_listener

    def get_all_locations(self, request):
        response = GetAllLocationsResponse()
        for name, pose_stamped in self._db.get_all_locations():
            response.locations.append(Location(name=name,
                                               pose_stamped=pose_stamped))
        return response

    def get_location(self, request):
        response = GetLocationResponse()
        pose_stamped = self._db.get_location(request.name)
        if pose_stamped is None:
            rospy.logerr(
                '[LocationDb] Can\'t get location {}'.format(request.name))
            response.success = False
            return response
        else:
            response.success = True
            response.pose_stamped = pose_stamped
            return response

    def remove_location(self, request):
        response = RemoveLocationResponse()
        success = self._db.remove_location(request.name)
        if success:
            response.success = True
            return response
        else:
            rospy.logerr(
                '[LocationDb] Can\'t remove location {}'.format(request.name))
            response.success = False
            return response

    def set_location(self, request):
        response = SetLocationResponse()
        success = self._db.set_location(request.name, request.pose_stamped)
        if success:
            response.success = True
            return response
        else:
            rospy.logerr(
                '[LocationDb] Can\'t set location {}'.format(request.name))
            response.success = False
            return response

    def set_location_db(self, request):
        response = SetLocationDbResponse()
        self._db = LocationDb(request.db_filename, self._tf_listener)
        response.success = True
        return response


if __name__ == '__main__':
    rospy.init_node('location_db')
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        metavar='FILE',
                        type=str,
                        help='Python shelve DB containing locations.')
    args = parser.parse_args(args=rospy.myargv()[1:])
    tf_listener = tf.TransformListener()
    db_service = LocationDbService(args.filename, tf_listener)
    rospy.Service('get_all_locations', GetAllLocations,
                  db_service.get_all_locations)
    rospy.Service('get_location', GetLocation, db_service.get_location)
    rospy.Service('remove_location', RemoveLocation,
                  db_service.remove_location)
    rospy.Service('set_location', SetLocation, db_service.set_location)
    rospy.Service('set_location_db', SetLocationDb, db_service.set_location_db)
    rospy.spin()
