from configuration import *
import time
import calendar


class CoordinatesSource(object):

    def get_coordinates(self):
        coordinates = db.coordinates.find({})
        return list(coordinates)

    def add_coordinate(self, x_coordinate, y_coordinate):

        coordinate = {'x_coordinate': x_coordinate, 'y_coordinate': y_coordinate, 'date': int(calendar.timegm(time.gmtime()))}
        result = db.coordinates.insert_one(coordinate)

        if result.inserted_id:
            return {'status': 'success', 'message': 'Coordinate added'}
        else:
            return {'status': 'failed', 'message': 'Coordinate could not be added'}
