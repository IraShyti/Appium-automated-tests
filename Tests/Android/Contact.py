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


user1 = "cihangok@yahoo.com"
pass1 = "1q2w3e4r"

class CONTACT(object):
    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("************************************", 'green')
        self.logger.log('Contact test initialized', 'yellow')
        self.logger.log("************************************", 'green')

    def test(self):
        sleep(0.5)
        self.logger.log("************************************")
        sleep(0.5)
        self.logger.log('Contact test initialized', 'yellow')
        self.logger.log("************************************", 'green')
        self.appium_worker.entrance_android()
        self.logger.log("Clicking left sub-menu")
        self.driver.find_element_by_id("drawer_indicator").click()
        sleep(1)
        drawer = self.appium_worker.submenu()
        if drawer == 2:
            self.logger.log("Scrolling up the screen")
            element2 = self.driver.find_element_by_class_name("android.widget.ListView")
            touch_actions = TouchActions(self.driver)
            touch_actions.flick_element(element2, 0, 1000, 100).perform()
            touch_actions.perform()
            sleep(1)
        self.logger.log("Scrolling down")
        element2 = self.driver.find_element_by_class_name("android.widget.RelativeLayout")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -1000, 100).perform()
        touch_actions.perform()
        sleep(1)
        self.logger.log("Clicking Contact")
        self.driver.find_elements_by_class_name("android.widget.LinearLayout")[16].click()
        self.appium_worker.bekle_android("tvSupport")
        m1 = self.driver.find_element_by_id("tvAddress").text
        m2 = self.driver.find_element_by_id("tvFax").text
        m3 = self.driver.find_element_by_id("tvPhoneNumber").text
        m4 = self.driver.find_element_by_id("tvEmail").text
        self.logger.log("Address: " + m1, 'blue')
        self.logger.log("Fax: " + m2, 'blue')
        self.logger.log("Phone: " + m3, 'blue')
        self.logger.log("Mail: " + m4, 'blue')
        self.logger.log("Clicking Support button")
        self.driver.find_element_by_id("tvSupport").click()
        sleep(2)
        self.logger.log("Going back")
        self.driver.back()
        self.logger.log("Clicking New Message")
        self.driver.find_element_by_id("tvNewMessage").click()
        self.logger.log("Going back")
        self.driver.back()
        sleep(2)
        self.driver.back()
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())
