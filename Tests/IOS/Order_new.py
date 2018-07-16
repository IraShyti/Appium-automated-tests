"""
UI iOS tests for AmerikadanIste app.
Ira Shyti 26-09-2016
"""

import os
from appium import webdriver
import time
from time import sleep
from selenium import webdriver
from Utilities.logger import Logger
from Tests.appium_worker import webdriver
import unittest
import random
import codecs
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException


class NEWORDERIOS(object):
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
        self.appium_worker.bekle_ios("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]")
        self.logger.log("Presing New Order")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]").click()
        sleep(2)
        #self.logger.log("Clicking SAVE THE SHOPPING button without entering any detail")
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]").click()
        #sleep(2)
        #self.logger.log("Message : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[3]").text)
        #self.logger.log("Clicking Done")
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[9]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").click()
        sleep(2)
        self.logger.log("Entering shopping site as 6pm")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys("6pm")
        self.logger.log("Clicking done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAKeyboard[1]/UIAButton[4]").click()
        self.logger.log("Entering content as Clothes")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[1]").send_keys("Clothes")
        self.logger.log("Entering notes for the order")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[2]").send_keys("Test note")
        self.logger.log("Clicking to keep the original package")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAImage[7]").click()
        self.logger.log("Clicking SAVE THE SHOPPING button")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]").click()
        self.appium_worker.bekle_ios("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAImage[2]")
        #sleep(3)
        self.logger.log("New Order created successfully")
        self.logger.log("Clicking Back")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]").click()
        sleep(2)
        self.logger.log("Clicking Back")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]").click()
        sleep(2)
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())

