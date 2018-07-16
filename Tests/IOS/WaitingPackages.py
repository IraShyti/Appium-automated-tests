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
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException


class WAITINGPACKAGESIOS(object):
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
        self.logger.log("Clicking Waiting Packages button")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/"
                                          "UIAStaticText[1]").click()
        sleep(1)
        self.logger.log("Clicing a package")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[2]/UIATableCell[1]").click()
        sleep(1)
        self.logger.log("*********************************")
        self.logger.log("Sender : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[4]").text)
        sleep(1)
        try:
            self.driver.find_element_by_xpath(" //UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[5]")
            flag1 = 1
        except NoSuchElementException:
            flag1 = 0
        if flag1 == 0:
            self.logger.log("Clicking to ad Carrier")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[1]").click()
            self.logger.log("Adding tracking code as 12345")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys("12345")
            self.logger.log("Selecting Carrir UPS")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAImage[2]").click()
            self.logger.log("Clicking Save buton")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        if flag1 == 1:
            self.logger.log("Carrier is : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                                    "UIAStaticText[5]").text)
        self.logger.log("Package code is : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                                     "UIAStaticText[8]").text)
        self.logger.log("Content : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                             "UIATableView[1]/UIATableCell[1]/UIATextField[1]").text)
        self.logger.log("Date : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                          "UIATableView[1]/UIATableCell[2]/UIAStaticText[2]").text)
        self.logger.log("Pressing to edit note")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAImage[6]").click()
        sleep(1)
        self.logger.log("Editing Note")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[1]").clear()
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[1]").send_keys("New note")
        self.logger.log("Clicking Save")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        sleep(1)
        self.logger.log("Clicking expected packages button")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]").click()
        sleep(2)
        '''
        sleep(3)
        self.logger.log("222222")
        self.logger.log("Clicing a package")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[2]/UIATableCell[4]").click()
        sleep(1)
        self.logger.log("*********************************")
        self.logger.log("Sender : " + self.driver.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[4]").text)
        sleep(1)
        try:
            self.driver.find_element_by_xpath(" //UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[5]")
            flag1 = 1
        except NoSuchElementException:
            flag1 = 0
        if flag1 == 0:
            self.logger.log("Clicking to ad Carrier")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[1]").click()
            self.logger.log("Adding tracking code as 12345")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys("12345")
            self.logger.log("Selecting Carrir UPS")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAImage[2]").click()
            self.logger.log("Clicking Save buton")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        if flag1 == 1:
            self.logger.log("Carrier is : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                                    "UIAStaticText[5]").text)
        self.logger.log("Package code is : " + self.driver.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
            "UIAStaticText[8]").text)
        self.logger.log("Content : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                             "UIATableView[1]/UIATableCell[1]/UIATextField[1]").text)
        self.logger.log("Date : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                          "UIATableView[1]/UIATableCell[2]/UIAStaticText[2]").text)
        self.logger.log("Pressing to edit note")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAImage[6]").click()
        sleep(1)
        self.logger.log("Editing Note")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[1]").clear()
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[1]").send_keys("New note")
        self.logger.log("Clicking Save")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        sleep(1)
        self.logger.log("Clicking expected packages button")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[5]").click()
        sleep(2)
'''
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]").click()
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())
        sleep(2)



