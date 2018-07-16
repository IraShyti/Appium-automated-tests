from codecs import decode
import os
import codecs
import datetime
from datetime import datetime
from datetime import time
import time


format = "%Y-%m-%d"
format1 = "%H:%M:%S"
dt = datetime.now()


class Logger(object):

    def funct_decode(self, the_string):
        return codecs.encode(the_string, 'utf-8')

    def getFileName(self):
        return self.file_name

    def __init__(self, test_source=None):
        self.test_source = test_source
        self.default_color = 'white'
        self.file_name = "default_{}.log".format(dt.strftime(format))
        self.file = open(os.getcwd() + "/static/Logs/" + self.file_name, "w")

    def newFile(self, file_name):
        self.file_name = "{}_{}.log".format(file_name, dt.strftime(format))
        self.file = os.open("{}/static/Logs/{}".format(os.getcwd(), self.file_name), os.O_CREAT | os.O_RDWR)

    def log(self, text, color="green", type=1, status=1, download=""):

        color_hex = {
            'red': '91m',
            'green': '92m',
            'yellow': '93m',
            'blue': '94m',
            'cyan': '96m'
        }
        if self.test_source:
            self.test_source.send_log(text.decode('utf-8'), type, status, download)
        else:

            print(
                '[' + time.strftime("%H:%M:%S") +'] \033[{color} {string} \033[0m'.format(
                   # time=dt.strftime(format1),
                    color=color_hex[color],
                    string=text.decode('utf-8')
                )
            )


        try:

            os.write(self.file, dt.strftime(format1) + ": " + text + "\n")
        except IOError as (errno, strerror):
            print "I/O error({0}): {1}".format(errno, strerror)

        if status == 2:
            print "status 2 flush and close"
            os.fsync(self.file)





