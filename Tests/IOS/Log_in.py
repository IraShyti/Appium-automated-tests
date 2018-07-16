"""
UI iOS tests for AmerikadanIste app.
Ira Shyti 23-09-2016
"""
from appium import webdriver
import time
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


class TestLogInIOS(object):
    log_flag = 0

    def __init__(self, appium_worker):

        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("************************************", 'green')

    def entrance(self):

        flag = 0
        while flag == 0:
            try:
                self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]")
                flag = 1
            except NoSuchElementException:
                try:
                    self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1][@name='Login']")
                    flag = 2
                except NoSuchElementException:
                    try:
                        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/"
                                                          "UIAButton[1]")
                        flag = 3
                    except NoSuchElementException:
                        sleep(1)
                        self.logger.log("Wait")
                        flag = 0
        if flag == 1:
            self.logger.log('Pressing pass')
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()

        if flag == 2:
            sleep(1)

        if flag == 3:
            sleep(1)

    def test(self):
        user1 = ''
        pass1 = ''
        pass2 = 'abcdefg'
        sleep(3)
        self.entrance()
        self.logger.log("Clicking Log In")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        self.logger.log("Entering email " + user1)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys(user1)
        flag1 = 0
        while flag1 == 0:
            m1 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").text
            self.logger.log(m1)
            if str(m1) == user1:
                sleep(0.5)
                flag1 = 1
            else:
                flag1 = 0
                self.logger.log("Mail was entered incorrect")
                self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").clear()
                self.logger.log("Entering email " + str(user1))
                self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys(user1)
        self.logger.log("Entering incorrect password " + pass2)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]").send_keys(pass2)
        self.logger.log("Clicking LogIn")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        self.logger.log("Expecting error message")
        try:
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[6]")
            flag1 = 1
        except NoSuchElementException:
            flag1 = 0
        if flag1 == 0:
            self.logger.log("Error message not shown")
        elif flag1 == 1:
            self.logger.log("Error message shown")
            self.appium_worker.screenshot("Incorrect_password")
            self.logger.log("Clicking done")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[6]").click()
        self.logger.log("Entering correct password " + pass1)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]").clear()
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]").send_keys(pass1)
        self.logger.log("Clicking LogIn")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        sleep(3)
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())
