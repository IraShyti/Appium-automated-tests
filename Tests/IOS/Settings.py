"""
UI iOS tests for AmerikadanIste app.
Ira Shyti 23-09-2016
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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException


class TestSettingsIOS(object):
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
        self.logger.log("Clicking My Profile")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[5]").click()
        self.appium_worker.bekle_ios("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[3]")
        self.logger.log("Clicking settings icon")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[3]").click()
        lang = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[1]").text
        if self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[1]").text == "English":
            self.logger.log("Language is Turkish")
        else:
            self.logger.log("Language is English")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[1]").click()
        if self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[1]").is_enabled():
            self.logger.log("Sms notification is enabled")
            self.logger.log("Clicking to disable it")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIASwitch[1]").click()
        else:
            self.logger.log("Sms notification is disabled")
            self.logger.log("Clicking to enable it")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIASwitch[1]").click()
        sleep(3)
        if self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIASwitch[3]").is_enabled():
            self.logger.log("Newsletter is enabled")
            self.logger.log("Clicking to disable it")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIASwitch[3]").click()
        else:
            self.logger.log("Newsletter is disabled")
            self.logger.log("Clicking to enable it")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIASwitch[3]").click()

        if self.driver.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIASwitch[4]").is_enabled():
            self.logger.log("Deal Aler is enabled")
            self.logger.log("Clicking to disable it")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIASwitch[4]").click()
        else:
            self.logger.log("Deal Alert is disabled")
            self.logger.log("Clicking to enable it")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIASwitch[4]").click()
        sleep(2)
        self.logger.log("Clicking Home Page button")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[1]").click()
        sleep(2)
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())


