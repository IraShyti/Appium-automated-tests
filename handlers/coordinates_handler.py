from base_handler import BaseHandler
import json
from bson.json_util import dumps
from sources.coordinates_source import CoordinatesSource


class CoordinatesHandler(BaseHandler):
    def get(self):

        result = CoordinatesSource().get_coordinates()
        self.write(dumps(result))

    def post(self, *args, **kwargs):
        payload = json.loads(self.request.body)
        x_coordinate = payload['x_coordinate']
        y_coordinate = payload['y_coordinate']
        self.write(dumps({'result': CoordinatesSource().add_coordinate(x_coordinate, y_coordinate)}))