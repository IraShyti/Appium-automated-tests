"""UI iOS tests for AmerikadanIste app.
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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException


class NOTIFICATIONSIOS(object):
    log_flag = 0

    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger

    def notification(self, e1):
        self.logger.log(e1.text)
        #e1 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]")
        if e1.text == "MY US MAILBOX":
            self.logger.log("You can click to show your US mailbox")
            self.logger.log("Pressing back")
            self.driver.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]").click()
        elif e1.text == "PACKAGE TRACKING":
            self.logger.log("Click to track your package")
            self.logger.log("Pressing back")
            self.driver.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]").click()
        elif e1.text == "MY ORDERS":
            self.logger.log("Click to open your orders")
            self.logger.log("Pressing back")
            self.driver.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]").click()
        elif e1.text == "Done":
            self.logger.log("Pressing DONE button")
            self.appium_worker.bekle_ios("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()

    def test(self):
        self.appium_worker.entrance_ios()
        flag1 = 0
        while flag1 == 0:
            try:
                self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[5]")
                flag1 = 1
            except NoSuchElementException:
                flag1 = 0
                self.logger.log("Wait")
                sleep(1)
        self.logger.log("Clicking Notifications icon")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]").click()
        sleep(2)
        self.logger.log("Pressing a notification")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]").click()
        self.appium_worker.bekle_ios("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]")
        e1 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]")
        self.notification(e1)
        self.logger.log("Pressing a notification")

        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[6]").click()
        self.appium_worker.bekle_ios("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]")
        e1 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]")
        self.notification(e1)
        sleep(2)
        self.driver.back()
        sleep(2)
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())

