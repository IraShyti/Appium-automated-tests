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


class SETTINGS(object):
    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("************************************", 'green')


    def test(self):
        sleep(0.5)
        self.logger.log("************************************")
        sleep(0.5)
        self.logger.log('Settings test initialized', 'yellow')
        sleep(0.5)
        self.logger.log("************************************", 'green')
        self.appium_worker.entrance_android()
        self.appium_worker.bekle_android("drawer_indicator")
        self.driver.find_element_by_id("drawer_indicator").click()
        sleep(1)
        self.logger.log("Scrolling down")
        element2 = self.driver.find_element_by_class_name("android.widget.RelativeLayout")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -1000, 100).perform()
        touch_actions.perform()
        sleep(1)
        self.logger.log("Clicking Settings")
        self.driver.find_elements_by_class_name("android.widget.LinearLayout")[15].click()
        sleep(1)
        self.logger.log("Clicking to change language")
        self.driver.find_element_by_id("tvLanguage").click()
        sleep(1)
        self.logger.log("Language changed to : " + self.logger.funct_decode(self.driver.find_element_by_id("tvLanguage").text))
        if self.logger.funct_decode(self.driver.find_element_by_id("tvLanguage").text) != "English":
            self.driver.find_element_by_id("tvLanguage").click()
        self.appium_worker.screenshot("Language_changed")
        el1 = self.driver.find_element_by_id("cbSms")
        el1.click()
        self.driver.find_element_by_id("cbNewsletter").click()
        self.driver.back()
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())
