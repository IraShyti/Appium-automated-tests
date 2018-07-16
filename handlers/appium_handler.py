import uuid
from base_handler import BaseHandler
from bson.json_util import dumps
from tornado.web import asynchronous
from sources.test_source import TestSource
from tornado.ioloop import IOLoop
from multiprocessing.pool import ThreadPool
from Tests.appium_worker import AppiumWorker
from Utilities.logger import Logger
from sources.test_case_source import TestCaseSource
from sources.device_source import DeviceSource


_workers = ThreadPool(10)


def run_background(func, callback, args=(), kwds={}):
    def _callback(result):
        IOLoop.instance().add_callback(lambda: callback(result))
    _workers.apply_async(func, args, kwds, _callback)


def blocking_task(test_name_list, device_name_list, handler):

    logger = Logger()
    worker = AppiumWorker()
    worker.setLogger(logger)

    #TODO device list

    #device = DeviceSource.get_device(device_name_list[0])
    worker.setDevice(device_name_list[0])
    print 'after set device'
    for test in test_name_list:
        print test + ' starting'
        TestSource(handler, worker, logger).__getattribute__(test)()


    #test_case = TestSource(handler, worker, logger).__getattribute__(test_name)
    '''
    print test_case
    if not test_case:
        handler.on_complete('test not foud')
        return
    handler.on_complete('test started')
    '''
    #test_case()
    return


class AppiumHandler(BaseHandler):

    def initialize(self, buffer):
        print 'initialize AppiumHandler'
        self.global_log_buffer = buffer

    def send_log(self, log, log_type, status, download):
        print 'send_log'
        message = {
            "log_id": str(uuid.uuid4()),
            "body": log,
            "type": log_type,
            "status": status,
            "download": download,
        }
        self.global_log_buffer.new_messages([message])

    @asynchronous
    def get(self):
        test_name_list = self.request.arguments.get("test_name")
        device_name_list = self.request.arguments.get("device_name")

        print test_name_list
        print device_name_list

        test_cases = TestCaseSource().get_test_cases()
        test_cases = sorted(test_cases, key=lambda x: x['test_case_index'], reverse=False)

        print 'get'

        test_names = []
        for test in test_cases:
            if test['attribute_name'] in test_name_list:
                test_names.append(test['attribute_name'])

        run_background(blocking_task, self.on_complete, (test_names, device_name_list,  self))

    def on_complete(self, result):
        self.write(dumps({'result': result}))
        self.finish()
