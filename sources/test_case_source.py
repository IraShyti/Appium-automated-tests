from configuration import *


class TestCaseSource(object):

    def get_test_cases(self):

        print 'aaa'
        cases = db.test_cases.find({})
        print 'bbb'
        print 'ccc'
        return list(cases)

    def get_test_case(self, test_case_name):
        return db.test_cases.find_one({'test_case_name': test_case_name})

    def add_test_case(self, test_case_name, attribute_name, test_case_index, test_platform):

        if self.get_test_case(test_case_name):
            return {'status': 'failed', 'message': 'Existing test case'}

        test_case = {'test_case_name': test_case_name, 'attribute_name': attribute_name, 'test_case_index': test_case_index, 'test_platform': test_platform}
        result = db.test_cases.insert_one(test_case)

        if result.inserted_id:
            return {'status': 'success', 'message': 'Test case added'}
        else:
            return {'status': 'failed', 'message': 'Test case could not be added'}

    def delete_test_case(self, test_case_name):
        result = db.test_cases.delete_one({'test_case_name': test_case_name})

        if result.deleted_count == 1:
            return {'status': 'success', 'message': 'Test case deleted'}
        else:
            return {'status': 'failed', 'message': 'Test case could not be deleted'}

    def update_test_case(self, test_case_name, attribute_name, test_case_index, test_platform):

        result = db.test_cases.update_one({'test_case_name': test_case_name}, {'$set': {'attribute_name': attribute_name, 'test_case_index': test_case_index, 'test_platform': test_platform} })

        if result.matched_count == 1:
            return {'status': 'success', 'message': 'Test case updated'}
        else:
            return {'status': 'failed', 'message': 'Test case could not be updated'}




