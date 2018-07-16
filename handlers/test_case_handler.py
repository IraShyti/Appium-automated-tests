from base_handler import BaseHandler
import json
from bson.json_util import dumps
from sources.test_case_source import TestCaseSource


class TestCaseHandler(BaseHandler):
    def get(self, test_case_name):

        if not test_case_name or test_case_name == '/':
            test_case_name = None
        else:
            test_case_name = test_case_name.strip('/')

        result = None
        if not test_case_name:
            result = TestCaseSource().get_test_cases()
            result = sorted(result, key=lambda x: x['test_case_index'], reverse=False)
        else:
            result = TestCaseSource().get_test_case(test_case_name)
        self.write(dumps(result))

    def post(self, *args, **kwargs):
        payload = json.loads(self.request.body)
        attribute_name = payload['attribute_name']
        test_case_name = payload['test_case_name']
        test_case_index = payload['test_case_index']
        test_platform = payload['test_platform']
        self.write(dumps(
            {'result': TestCaseSource().add_test_case(test_case_name, attribute_name, test_case_index, test_platform)}))

    def put(self, *args, **kwargs):
        payload = json.loads(self.request.body)
        attribute_name = payload['attribute_name']
        test_case_name = payload['test_case_name']
        test_case_index = payload['test_case_index']
        test_platform = payload['test_platform']
        self.write(dumps(
            {'result': TestCaseSource().update_test_case(test_case_name, attribute_name, test_case_index, test_platform)}))

    def delete(self, *args, **kwargs):
        payload = json.loads(self.request.body)
        test_case_name = payload['test_case_name']
        self.write(dumps({'result': TestCaseSource().delete_test_case(test_case_name)}))

