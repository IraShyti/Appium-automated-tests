import subprocess
from base_handler import BaseHandler
from multiprocessing.pool import ThreadPool
from tornado.ioloop import IOLoop
from sources.bash_source import BashSource
from sources.test_source import TestSource
from bson.json_util import dumps

_workers = ThreadPool(10)

def run_background(func, callback, args=(), kwds={}):
    def _callback(result):
        IOLoop.instance().add_callback(lambda: callback(result))
    _workers.apply_async(func, args, kwds, _callback)


def blocking_task(handler):

    BashSource().startAppium()
    return


class AppiumBashHandler(BaseHandler):


    def get(self):
        run_background(blocking_task, self.on_complete, self)

    def on_complete(self, result):
        self.write(dumps({'result': result}))
        self.finish()



