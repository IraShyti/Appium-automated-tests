from base_handler import BaseHandler
import json
from bson.json_util import dumps
from sources.test_case_source import TestCaseSource


class SystemHandler(BaseHandler):
    def get(self):
        self.write(dumps({'url': '192.168.1.88:8080'}))
