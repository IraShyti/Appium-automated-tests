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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException


class SHAREIOS(object):
    log_flag = 0

    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("*****************************", 'green')

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
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[14]").click()
        sleep(1)
        self.logger.log("Clicking to share Via Invitation")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[4]").click()
        self.logger.log("Clicking Done without entering any email")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[3]/UIAAlert[1]/UIACollectionView[1]/"
                                          "UIACollectionCell[2]/UIAButton[1]").click()
        self.logger.log("Expecting warning message")
        flag1 = 0
        while flag1 == 0:
            try:
                self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[4]")
                flag1 = 1
            except NoSuchElementException:
                sleep(1)
                flag1 = 0
        self.logger.log("Alert message : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[1]").text)
        self.logger.log("Clicking done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[4]").click()
        self.logger.log("Clicking to share Via Invitation")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[4]").click()
        self.logger.log("Entering email address")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[3]/UIAAlert[1]/UIAScrollView[1]/UIATableView[1]"
                                          "/UIATableCell[1]/UIATextField[1]").send_keys("test@test.com")
        self.logger.log("Clicking done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[3]/UIAAlert[1]/UIACollectionView[1]/"
                                          "UIACollectionCell[2]/UIAButton[1]").click()
        sleep(1)
        self.logger.log("Clicking to share with contacts")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
       #sleep(1)
       #self.logger.log("Clicking Send without selecting any contact")
       #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
       #self.logger.log("Expecting warning message")
       #flag1 = 0
       #while flag1 == 0:
       #    try:
       #        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[8]")
       #        flag1 = 1
       #    except NoSuchElementException:
       #        sleep(1)
       #        flag1 = 0
       #self.logger.log("Warning message : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[1]").text)
       #self.logger.log("Clicking Done")
       #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[8]").click()

        sleep(5)
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())

