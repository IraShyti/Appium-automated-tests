"""
UI iOS tests for AmerikadanIste app.
Ira Shyti 26-09-2016
"""
import os
import codecs
import datetime
from codecs import decode
from datetime import datetime
from Tests.appium_worker import AppiumWorker
from Utilities.logger import Logger
from Tests.appium_worker import webdriver
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from time import sleep
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

user1 = "cihangok@yahoo.com"
pass1 = "1q2w3e4r"



class ABOUTUSiOS(object):
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
        self.logger.log("Clicking About Us")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[12]").click()
        sleep(1)
        self.logger.log("CLicking About us")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        sleep(1)
        # SPUNON
        self.logger.log("Text :" + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                         "UIAWebView[1]").text)
        self.logger.log("Clicking back")
        self.driver.back()
        self.logger.log("Clicking Terms and Conditions")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]").click()
        sleep(2)
        self.logger.log("Clicking back")
        self.driver.back()
        self.logger.log("Clicking Privacy")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[3]").click()
        sleep(2)
        self.logger.log("Clicking back")
        self.driver.back()
        self.logger.log("Clicking F.A.Q")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[4]").click()
        sleep(2)
        self.logger.log("Clicking back")
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]").click()
        sleep(3)

        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())

