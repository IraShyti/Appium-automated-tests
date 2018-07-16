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


class WHATTOBUYIOS(object):
    log_flag = 0

    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("************************************", 'green')

    def test(self):
        user1 = 'cihangok@yahoo.com'
        pass1 = '1q2w3e4r'
        pass2 = 'abcdefg'
        self.appium_worker.entrance_ios()
        self.appium_worker.bekle_ios("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[4]")
        self.logger.log("Pressing What To Buy button")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[4]").click()
        self.appium_worker.bekle_ios("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]")
        self.logger.log("Scrolling icon menu")

        e1 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]")
        #self.driver.execute_script("mobile: scroll", {"direction": 'down', 'element': self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]")})

        el1 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[1]")
        el2 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[5]")
        action = TouchAction(self.driver)
        action.press(el1).move_to(el2).release().perform()


        #self.logger.log("Scrolling icon list")
        #el2 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAElement[2]")
        #touch_actions = TouchActions(self.driver)
        #touch_actions.flick_element(el2, -500, 0, 100).perform()
        #touch_actions.perform()
