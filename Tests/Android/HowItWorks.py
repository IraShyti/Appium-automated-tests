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


class HOWITWORKS(object):
    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("*******************************", 'green')


    def test(self):
        self.logger.log("*******************************", 'green')
        sleep(0.5)
        self.logger.log('How It Works test initialized', 'yellow')
        sleep(0.5)
        self.logger.log("*******************************", 'green')
        self.appium_worker.entrance_android()
        self.driver.find_element_by_id("drawer_indicator").click()
        sleep(1)
        self.logger.log("Scrolling down")
        element2 = self.driver.find_element_by_class_name("android.widget.RelativeLayout")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -1000, 100).perform()
        touch_actions.perform()
        sleep(1)
        self.logger.log("Clicking How It Works")
        self.driver.find_elements_by_class_name("android.widget.LinearLayout")[11].click()
        sleep(3)
        self.appium_worker.bekle_android("imageview")
        self.appium_worker.screenshot("How_it_works")
        m = self.driver.find_element_by_id("tvTitle").text
        m1 = self.driver.find_element_by_id("tvDescription").text
        self.logger.log("Image : " + str(m))
        self.logger.log("Text : " + str(m1))
        self.logger.log("Scrolling")
        element2 = self.driver.find_element_by_class_name("android.support.v4.view.ViewPager")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, -1000, 0, 100).perform()
        touch_actions.perform()
        sleep(2)
        self.appium_worker.bekle_android("imageview")
        m = self.driver.find_element_by_id("tvTitle").text
        m1 = self.driver.find_element_by_id("tvDescription").text
        self.logger.log("Image : " + str(m))
        self.logger.log("Text : " + str(m1))
        self.logger.log("Scrolling")
        element2 = self.driver.find_element_by_class_name("android.support.v4.view.ViewPager")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, -1000, 0, 100).perform()
        touch_actions.perform()
        sleep(2)
        self.appium_worker.bekle_android("imageview")
        m = self.driver.find_element_by_id("tvTitle").text
        m1 = self.driver.find_element_by_id("tvDescription").text
        self.logger.log("Image : " + str(m))
        self.logger.log("Text : " + str(m1))
        self.logger.log("Scrolling")
        element2 = self.driver.find_element_by_class_name("android.support.v4.view.ViewPager")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, -1000, 0, 100).perform()
        touch_actions.perform()
        sleep(2)
        self.appium_worker.bekle_android("imageview")
        m = self.driver.find_element_by_id("tvTitle").text
        m1 = self.driver.find_element_by_id("tvDescription").text
        self.logger.log("Image : " + str(m))
        self.logger.log("Text : " + str(m1))
        self.logger.log("Scrolling")
        element2 = self.driver.find_element_by_class_name("android.support.v4.view.ViewPager")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, -100, 0, 100).perform()
        touch_actions.perform()
        sleep(2)
        self.appium_worker.bekle_android("imageview")
        m = self.driver.find_element_by_id("tvTitle").text
        m1 = self.driver.find_element_by_id("tvDescription").text
        self.logger.log("Image : " + str(m))
        self.logger.log("Text : " + str(m1))
        self.driver.back()
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())