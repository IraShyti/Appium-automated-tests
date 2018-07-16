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


class SUPPORTIOS(object):
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
        sleep(1)
        self.logger.log("Clicking Support")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]").click()
        sleep(1)
        self.logger.log(self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAStaticText[1]").text + " : " +
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAStaticText[2]").text)
        self.logger.log("Clicking My Messages")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]").click()
        sleep(1)
        self.logger.log("Selecting a message")
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]").click()
        self.driver.find_elements_by_class_name("UIATableCell")[1].click()
        sleep(1)
        self.logger.log("Clicking Reply")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        self.logger.log("Entering message")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[1]").send_keys("test note")
        self.logger.log("Clicking Done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAToolbar[1]/UIAButton[2]").click()
        self.logger.log("Clicking Send")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        self.logger.log("Clicking Back")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]").click()
        self.logger.log("Clicking New Message")
        sleep(0.5)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[3]").click()
        sleep(0.5)
        self.logger.log("Clicking Send without adding subject or message")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        self.logger.log("Expecting error message")
        self.logger.log("Message : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[2]").text)
        self.logger.log("Clicking Done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[4]").click()
        self.logger.log("Entering subject")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys("test subject")
        self.logger.log("Entering message")
        self.driver.find_element_by_xpath(" //UIAApplication[1]/UIAWindow[1]/UIATextView[1]").send_keys("test message")
        self.logger.log("Clicking Done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAToolbar[1]/UIAButton[2]").click()
        self.logger.log("Clicking Send")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        sleep(0.5)
        self.logger.log("Clicking Call Me")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[4]").click()
        sleep(0.5)
        self.logger.log("Clicking Done without entering Subject and Time")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        sleep(2)
        self.logger.log("Error message expected")
        self.logger.log("Message : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[1]").text)
        self.logger.log("Clicking Done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[4]").click()
        self.logger.log("Entering subject")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys("test subject")
        self.logger.log("Selecting date")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[2]").click()
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAPicker[1]/UIAPickerWheel[2]").click()
        self.driver.find_elements_by_class_name("UIAPickerWheel")[1].send_keys("November")
        self.logger.log("Clicking Done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        sleep(3)
        self.logger.log("Message : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAStaticText[2]").text)
        #self.logger.log("Message : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAStaticText[3]").text)
        self.logger.log("Clicking Done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        self.logger.log("Clicking Back")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]").click()
        sleep(2)
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())



