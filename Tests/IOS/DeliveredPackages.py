"""
UI iOS tests for AmerikadanIste app.
Ira Shyti 26-09-2016
"""

from appium import webdriver
import time
import codecs
import datetime
from codecs import decode
from datetime import datetime
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


class DELIVEREDPACKAGESIOS(object):
    log_flag = 0

    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("**************************")

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

        self.logger.log("Clicking Delivered Package")
        self.driver.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[7]/UIAStaticText[1]").click()
        sleep(3)

        self.logger.log("Clicking one package")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[5]/UIATableCell[3]").click()
        sleep(1)
        self.logger.log("Sender : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                            "UIAStaticText[4]").text)

        self.logger.log("Carrier : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                             "UIAStaticText[5]").text)
        self.logger.log("Code : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                          "UIAStaticText[8]").text)
        self.logger.log("Content : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                             "UIATableView[1]/UIATableCell[1]/UIAStaticText[2]").text)
        self.logger.log("Received at : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                                 "UIATableView[1]/UIATableCell[2]/UIAStaticText[2]").text)

        self.logger.log("Shipped at : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                                "UIATableView[1]/UIATableCell[3]/UIAStaticText[2]").text)
        self.logger.log("Clicking back")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]").click()
        sleep(2)

        #log("Clicking one package")
        #sleep(2)
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[5]/UIATableCell[1]").click()
        #sleep(1)
        #log("Sender : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
        #                                                    "UIAStaticText[4]").text)

        #log("Carrier : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
        #                                                     "UIAStaticText[5]").text)
        #log("Code : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
        #                                                  "UIAStaticText[8]").text)
        #log("Content : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
        #                                                     "UIATableView[1]/UIATableCell[1]/UIAStaticText[2]").text)
        #log("Received at : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
        #                                                         "UIATableView[1]/UIATableCell[2]/UIAStaticText[2]").text)

        #log("Shipped at : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
        #                                                        "UIATableView[1]/UIATableCell[3]/UIAStaticText[2]").text)
        #log("Clicking back")
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]").click()
        sleep(2)

        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())


