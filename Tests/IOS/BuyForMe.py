"""
UI iOS tests for AmerikadanIste app.
Ira Shyti 26-09-2016
"""
import unittest
import os
from appium import webdriver
import time
import codecs
import datetime
from codecs import decode
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import WebDriverException
from Tests.appium_worker import AppiumWorker
from Utilities.logger import Logger
from Tests.appium_worker import webdriver
import unittest
import random
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

class BUYFORMEIOS(object):
    log_flag = 0

    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("********************************")

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
                self.logger.lo("Wait")
                sleep(1)
        self.logger.lo("Clicking left sub-menu")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]").click()
        self.logger.lo("Presing Buy For Me")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[8]").click()
        sleep(3)
        try:
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]")
            flag1 = 1
        except NoSuchElementException:
            flag1 = 0
        if flag1 == 0:
            self.logger.lo("Clicking to add first item")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[4]").click()

        elif flag1 == 1:
            self.logger.lo("Clicking to add a new product")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIAButton[1]").click()
        sleep(1)
        self.logger.lo("Clicking Add without entering any details")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[6]").click()
        sleep(1)
        self.logger.lo("Message : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[2]").text)
        self.logger.lo("Clicking Done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[10]").click()
        sleep(1)
        self.logger.lo("Entering products url")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys("url_product")
        self.logger.lo("Entering products features")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[2]").send_keys("test product")
        self.logger.lo("Selecting delivery type")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[3]").click()
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAToolbar[1]/UIAButton[2]").click()
        self.logger.lo("Clicking Add")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[6]").click()
        sleep(1)
        self.logger.lo("Clicking Complete Order")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[3]").click()
        sleep(2)
        self.logger.lo("Entering total amount")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys("10")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAToolbar[1]/UIAButton[2]").click()
        self.logger.lo("Clicking Calculate")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[3]").click()
        sleep(1)
        self.logger.lo("Clicking Continue")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[5]").click()
        sleep(2)
        #self.logger.lo("Page : " + self.driver.find_element_by_class_name("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/"
         #                                                      "UIAStaticText[1]").text)
        self.appium_worker.bekle_ios("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys("TestName")
        self.logger.lo("Entering Cardholder's First Name")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys("TestName")
        self.logger.lo("Entering Cardholder's Last Name")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[2]").send_keys("TestSurname")
        self.logger.lo("Entering Card Number")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[3]").send_keys("4090700214269159")
        self.logger.lo("Entering CVC")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[5]").send_keys("494")
        self.logger.lo("Selecting Expiration Date")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[4]").click()
        sleep(1)
        #self.driver.find_elements_by_class_name("UIAPickerWheel")[0].send_keys("1")
        self.driver.find_elements_by_class_name("UIAPickerWheel")[1].send_keys("2017")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAToolbar[1]/UIAButton[2]").click()
        self.logger.lo("Clicking Done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        sleep(10)
        self.logger.lo("Clicking Done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]").click()
        sleep(2)
        self.appium_worker.screenshot("BFM_Completed")
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())



