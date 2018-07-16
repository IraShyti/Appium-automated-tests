import tornado


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, , PUT, DELETE, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')

    @tornado.web.asynchronous
    def options(self, *args, **kwargs):
        """XHR cross-domain OPTIONS handler"""
        self.preflight()
        self.finish()

    def preflight(self):
        """Handles request authentication"""
        if 'Origin' in self.request.headers:
            if self.verify_origin():
                self.set_header('Access-Control-Allow-Origin',
                                self.request.headers['Origin'])

                self.set_header('Access-Control-Allow-Credentials', 'true')
                self.set_header('Access-Control-Allow-Methods', 'POST, GET, DELETE, PUT, OPTIONS')

                return True
            else:
                return False
        else:
            return True

    def verify_origin(self):
        """Verify if request can be served"""
        # TODO: Verify origin
        return True
