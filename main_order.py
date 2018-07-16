from Tests.Android.BuyForMe import BUYFORME
from Tests.Android.order import Order
from Tests.Android.About_us import ABOUTUS
from Tests.Android.Settings import SETTINGS
from Tests.Android.Prices import PRICES
from Tests.Android.Log_in import LOGIN
from Tests.Android.Support import SUPPORT
from Tests.Android.HowItWorks import HOWITWORKS
from Tests.Android.Share import SHARE
from Tests.Android.MyAwards import MYAWARDS
from Tests.Android.WhatToBuy import WHATTOBUY
from Utilities.logger import Logger
from Tests.appium_worker import AppiumWorker

from appium import webdriver
import unittest
import random
import os
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException


class Main_Order(object):

    def __init__(self):

        self.logger = Logger()
        self.appium_worker = AppiumWorker(self.logger)

    def test(self, item):

        try:
            item.test()
        except:
            self.appium_worker.main_page()
        finally:
            self.appium_worker.main_page()

    def test_all(self):
        self.test_order()

    def test_order(self):
        order = Order(self.appium_worker)
        self.test(order)


if __name__ == '__main__':
    main = Main_Order()
    main.test_all()
