from tornado.httpserver import HTTPServer
import tornado.web
import os.path
from tornado.options import define, options
from tornado.ioloop import IOLoop
from Utilities.log_buffer import LogBuffer
from handlers.appium_handler import AppiumHandler
from handlers.device_handler import DeviceHandler
from handlers.logs_handler import LogsHandler
from handlers.test_case_handler import TestCaseHandler
from handlers.appium_bash_handler import AppiumBashHandler
from handlers.coordinates_handler import CoordinatesHandler
from handlers.system_handler import SystemHandler
from Utilities.logger import Logger
from Tests.appium_worker import AppiumWorker

define("port", default=8888, help="run on the given port", type=int)
global_log_buffer = LogBuffer()



settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug": True,
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "xsrf_cookies": False
}


if __name__ == '__main__':
    tornado.options.parse_command_line()

    app = tornado.web.Application([

        (r"/api/logs", LogsHandler, dict(buffer=global_log_buffer)),
        (r'/api/starttest', AppiumHandler, dict(buffer=global_log_buffer)),
        (r'/api/devices(/[^/]*)*', DeviceHandler),
        (r'/api/test_cases(/[^/]*)*', TestCaseHandler),
        (r'/api/appium/start', AppiumBashHandler),
        
        (r'/api/coordinates', CoordinatesHandler)


    ], **settings)

    http_server = HTTPServer(app)
    http_server.listen(options.port)
    IOLoop.instance().start()
