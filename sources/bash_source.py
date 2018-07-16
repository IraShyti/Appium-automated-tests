from configuration import *
import subprocess


class BashSource(object):

    def startAppium(self):
        subprocess.call(['./appium.sh'])