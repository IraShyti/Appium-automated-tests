"""
UI iOS tests for AmerikadanIste app.
Ira Shyti 26-09-2016
"""

from appium import webdriver
import codecs
import datetime
from codecs import decode
from datetime import datetime
from Tests.appium_worker import AppiumWorker
from Utilities.logger import Logger
from Tests.appium_worker import webdriver
import unittest
import random
import os
import time
from time import sleep
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException


class PRICESIOS(object):
    log_flag = 0

    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("************************************", 'green')

    def test(self):
        self.appium_worker.entrance_ios()
        flag1 = 0
        while flag1 == 0:
            try:
                self.driver.find_element_by_xpath(
                    "//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[5]")
                flag1 = 1
            except NoSuchElementException:
                flag1 = 0
                self.logger.log("Wait")
                sleep(1)
        self.logger.log("Clicking left sub-menu")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]").click()
        sleep(3)
        self.logger.log("ready")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[11]").click()
        sleep(1)
        self.logger.log("Selecting items")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAScrollView[1]/"
                                          "UIAImage[1]").click()
        self.logger.log('Item selected : ' + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                                   "UIAScrollView[1]/UIAStaticText[1]").text)

        sleep(1)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAScrollView[1]/"
                                          "UIAImage[2]").click()

        self.logger.log('Item selected : ' + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]"
                                                                   "/UIAScrollView[1]/UIAStaticText[2]").text)

        self.logger.log("Total items : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                                 "UIAStaticText[10]").text)
        self.logger.log("Total lbs : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                               "UIAStaticText[11]").text)
        self.logger.log("Price of AmerikadanIste " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/"
                                                                           "UIAScrollView[1]/UIAStaticText[3]").text)
        self.logger.log("Price of UPS " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                                "UIAStaticText[6]").text)

        self.logger.log("Price of Fedex " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                                  "UIAStaticText[9]").text)
        sleep(2)

        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())



