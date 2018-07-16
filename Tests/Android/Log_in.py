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


class LOGIN(object):
    def __init__(self, appium_worker):

        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("************************************", 'green')


    def test(self):

        user1 = ''
        pass1 = ''
        pass3 = 'abcd'
        pass2 = 'testpass'
        flag_err = 0
        count = 0

        try:
            self.driver.find_element_by_id("err_no_connection")
            flag = 0
        except NoSuchElementException:
            flag = 1
        if flag == 1:
            flag1 = 0
            while flag1 == 0:
                try:
                    self.driver.find_element_by_id("tvLogin")
                    flag1 = 1
                except NoSuchElementException:
                    try:
                        self.driver.find_element_by_id('tvPass')
                        flag1 = 2
                    except NoSuchElementException:
                        sleep(1)
                        flag1 = 0
            self.logger.log('Log In test case initialized')
            sleep(1)
            self.logger.log("************************************")
            if flag1 == 2:
                self.logger.log("Clicking Pass")
                self.driver.find_element_by_id('tvPass').click()
                sleep(1)
            if flag1 == 1:
                sleep(1)
            self.appium_worker.bekle_android("tvLogin")
            self.logger.log("Clicking Log In", "yellow")
            self.driver.find_element_by_id("tvLogin").click()
            self.logger.log("Entering email " + str(user1), 'blue')
            self.driver.find_element_by_id("etEmail").send_keys(user1)
            sleep(2)
            m1 = self.driver.find_element_by_id("etEmail").text
            if str(m1) == user1:
                sleep(0.5)
            else:
                self.logger.log("Mail was entered incorrect")
                self.driver.find_element_by_id("etEmail").clear()
                self.logger.log("Entering email " + str(user1), 'blue')
                self.driver.find_element_by_id("etEmail").send_keys(user1)
            self.logger.log("Entering Password " + str(pass3), 'blue')
            self.driver.find_element_by_id("etPassword").send_keys(pass3)
            self.logger.log("Clicking log in")
            self.driver.find_element_by_id("btnSend").click()
            self.appium_worker.screenshot("short_password")

            self.logger.log("Entering Password " + pass2, 'blue')
            self.driver.find_element_by_id("etPassword").send_keys(pass2)
            self.logger.log("Clicking log in")
            self.driver.find_element_by_id("btnSend").click()
            sleep(3)
            try:
                self.driver.find_element_by_id("tvPositive")
                flag = 1
            except NoSuchElementException:
                flag = 0
            if flag == 1:
                sleep(0.5)
                self.appium_worker.screenshot("Incorrect_password")
                self.logger.log("Clicking ok")
                self.driver.find_element_by_id("tvPositive").click()
            else:
                self.logger.log("Error for incorrect password was expected")
                self.logger.log("ERROR")

            self.driver.find_element_by_id("etPassword").clear()
            self.logger.log("Entering Password " + pass1, 'blue')
            self.driver.find_element_by_id("etPassword").clear()
            self.driver.find_element_by_id("etPassword").send_keys(pass1)
            self.driver.find_element_by_id("btnSend").click()
            try:
                self.driver.find_element_by_id("tvPositive")
                flag = 1
            except NoSuchElementException:
                flag = 0
            if flag == 1:
                self.logger.log("Unexpected error")
                fl1 = 0
                while fl1 == 0:
                    self.logger.log("Entering email " + str(user1), 'blue')
                    self.driver.find_element_by_id("etEmail").clear()
                    self.driver.find_element_by_id("etEmail").send_keys(user1)
                    self.logger.log("Entering Password " + pass1, 'blue')
                    self.driver.find_element_by_id("etPassword").clear()
                    self.driver.find_element_by_id("etPassword").send_keys(pass1)
                    self.logger.log("Clicking Log In")
                    self.driver.find_element_by_id("btnSend").click()
                    sleep(1)
                    try:
                        self.driver.find_element_by_id("tvPositive")
                        fl1 = 0
                    except NoSuchElementException:
                        fl1 = 1
            self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())

                #else:
                #    self.logger.log("Clicking left sub-menu")
                #    self.driver.find_element_by_id("drawer_indicator").click()
                #    self.logger.log("Scrolling down")
                #    element2 = self.driver.find_element_by_class_name("android.widget.RelativeLayout")
                #    touch_actions = TouchActions(self.driver)
                #    touch_actions.flick_element(element2, 0, -1000, 100).perform()
                #    touch_actions.perform()
                #    sleep(1)
                #    self.logger.log("Clicking Exit")
                #    self.driver.find_elements_by_class_name("android.widget.LinearLayout")[19].click()
                #    sleep(2)

        else:
            self.logger.log("Error for short password was expected")
            self.logger.log("ERROR")
