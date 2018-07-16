from base_handler import BaseHandler
import json
from bson.json_util import dumps
from sources.test_source import TestSource


class TestHandler(BaseHandler):
    def post(self):

        print self.request.body
        payload = json.loads(self.request.body)
        '''
        userName = payload['userName']
        userID = payload['userID']
        authToken = payload['authToken']
        authTokenSecret = payload['authTokenSecret']
        '''
        self.write(dumps(TestSource().test(payload)))

