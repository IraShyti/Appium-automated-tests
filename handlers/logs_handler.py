from base_handler import BaseHandler
from tornado import gen


class LogsHandler(BaseHandler):

    def initialize(self, buffer):
        self.global_log_buffer = buffer

    @gen.coroutine
    def options(self):
        self.set_header('Content-type', '*')
        cursor = self.get_argument("cursor", None)
        self.future = self.global_log_buffer.wait_for_messages(cursor=cursor)
        messages = yield self.future
        if self.request.connection.stream.closed():
            return
        self.write(dict(messages=messages))

    @gen.coroutine
    def post(self):
        cursor = self.get_argument("cursor", None)
        self.future = self.global_log_buffer.wait_for_messages(cursor=cursor)
        messages = yield self.future
        if self.request.connection.stream.closed():
            return
        self.write(dict(messages=messages))

    def on_connection_close(self):
        self.global_log_buffer.cancel_wait(self.future)