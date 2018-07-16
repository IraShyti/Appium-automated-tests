"""
UI iOS tests for AmerikadanIste app.
Ira Shyti 29-09-2016
"""

from appium import webdriver
import codecs
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
import datetime
import uuid
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException


class SIGNUPIOS(object):
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
                self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1][@name = 'Skip']")
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
            # self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()

        if flag == 2:
            sleep(1)

        if flag == 3:
            sleep(1)

    def test(self):
        sleep(3)
        self.entrance()
        sleep(1)
        self.logger.log("Clicking Sign Up")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]").click()
        sleep(1)
        self.logger.log("Entering Name")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[6]").send_keys("testName")
        self.logger.log("Entering Surname")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[7]").send_keys("testSurname")
        self.logger.log("Entering an already used email address")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[8]").send_keys("cihangok@yahoo.com")
        self.logger.log("Entering a short password")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]").send_keys("1234")
        self.logger.log("Entering Phone number")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[9]").send_keys("5555555555")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAImage[12]").click()
        self.logger.log("Clicking Create Account")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[6]").click()
        self.logger.log("Expecting error message for not accepting terms and conditions")
        sleep(2)

        self.logger.log("Message is : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[1]").text)
        self.logger.log("Clicking Done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[10]").click()
        sleep(1.5)
        self.logger.log("Clicking to accept terms and conditions")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[4]").click()
        self.logger.log("Clicking Create Account")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[6]").click()
        self.logger.log("Expecting warning message for short password")
        sleep(1)
        self.logger.log("Message : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[1]").text)
        self.logger.log("Clicking Done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[10]").click()
        self.logger.log("Changing password")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]").clear()
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]").send_keys("1234567")
        # click somewhere
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAImage[12]").click()
        self.logger.log("Clicking Create Account")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[6]").click()
        sleep(3)
        self.logger.log("Expecting message for used email address")
        self.logger.log("Message : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[1]").text)
        self.logger.log("Clicking Done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[10]").click()
        self.logger.log("Changing the email address")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[8]").clear()
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[8]").send_keys("6@test.com")
        # click somewhere
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAImage[12]").click()
        self.logger.log("Clicking Create Account")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[6]").click()

        sleep(3)
        self.logger.log("Clicking to read detailed information")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[2]").click()
        sleep(1)
        self.logger.log("Clicking to exit")
        self.driver.find_element_by_xpath(" //UIAApplication[1]/UIAWindow[1]/UIAButton[8]").click()
        self.logger.log("Clicking to read registration fee infromation")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[1]").click()
        self.logger.log("Clicking done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[10]").click()
        self.logger.log("Clicking to read membership plan information")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[4]").click()
        self.logger.log("Clicking Done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[10]").click()
        self.logger.log("Selecting Yearly Membership Plan")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[3]").click()
        #self.logger.log("Entering false promotion code")
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[1]").send_keys("false")
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]").click()
        #self.logger.log("Clicking Apply")
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[5]").click()
        #self.logger.log("Error message for false promotion code is expected")
        #self.logger.log("Message : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[1]").text)
        #self.logger.log("Clicking Done")
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[10]").click()
        self.logger.log("Entering correct promotion code")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[1]").clear()
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[1]").send_keys("REGISTERTEST062016")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]").click()
        self.logger.log("Clicking Apply")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[5]").click()
        sleep(1)
        self.logger.log("Earned promotion : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]"
                                                                      "/UIAButton[5]").text)
        self.logger.log("Clicking to enter payment information")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[6]").click()
        sleep(1)
        self.logger.log("Entering Card Holder name")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[2]").\
            send_keys("testName")
        self.logger.log("Entering Card Holder surname")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[3]").\
            send_keys("testSurname")
        self.logger.log("Entering card number")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[4]").send_keys("4090700214269159")

        self.logger.log("Selecting card expiration day")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[5]").click()
        self.driver.find_elements_by_class_name("UIAPickerWheel")[1].send_keys("2017")
        self.logger.log("Entering Card CVC")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[6]"). \
            send_keys("494")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]").click()
        sleep(3)
        self.logger.log("Clicking Complete")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[7]").click()
        sleep(5)
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())

        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAToolbar[1]/UIAButton[2]").click()
        # click somewhere
        #self.logger.log("Clicking COMPLETE")
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[7]").click()
        # wait/checl
        # test finished


