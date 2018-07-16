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


class WHATTOBUY(object):
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
        self.logger.log('Log in as guest test initialized', 'yellow')
        sleep(0.5)
        self.logger.log("************************************", 'green')
        flag = 0
        while flag == 0:
            try:
                self.driver.find_element_by_id('tvPass')
                flag = 1
            except NoSuchElementException:
                try:
                    self.driver.find_element_by_id("tvLogin")
                    flag = 2
                except NoSuchElementException:
                    sleep(1)
                    flag = 0
        if flag == 1:
            self.logger.log("Clicking Pass")
            self.driver.find_element_by_id('tvPass').click()
        if flag == 2:
            self.logger.log("Clicking Pass")
            self.driver.find_element_by_id('tvPass').click()
        self.logger.log("Clicking Continue as guest")
        self.driver.find_element_by_id('tvContinueAsGuest').click()
        sleep(4)
        self.driver.find_elements_by_class_name("android.widget.Gallery")[0]
        self.driver.find_elements_by_id("ivIcon")[0].click()
        self.logger.log("Scrolling Icon menu")
        element = self.driver.find_elements_by_class_name("android.widget.Gallery")[0]
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element, -500, 0, 50).perform()
        touch_actions.perform()
        sleep(2)
        self.logger.log("Selecting an icon")
        self.driver.find_elements_by_id("ivIcon")[0].click()
        sleep(3)
        self.logger.log("Scrolling list menu")
        element1 = self.driver.find_elements_by_class_name("android.widget.Gallery")[1]
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element1, -400, 0, 100).perform()
        touch_actions.perform()
        sleep(1)
        self.driver.find_elements_by_id("textView")[1].click()
        sleep(3)
        self.logger.log("Scrolling item list")
        element2 = self.driver.find_element_by_class_name("android.widget.GridView")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -500, 100).perform()
        touch_actions.perform()
        sleep(1)

        self.driver.find_elements_by_id("gridview")[0].click()
        self.logger.log("Scrolling Icon menu")
        el2 = self.driver.find_elements_by_class_name("android.widget.Gallery")[0]
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(el2, -200, 0, 50).perform()
        touch_actions.perform()
        self.driver.find_elements_by_id("ivIcon")[2].click()
        sleep(1)
        self.logger.log("Scrolling item list")
        el3 = self.driver.find_element_by_class_name("android.widget.GridView")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(el3, 0, -500, 100).perform()
        touch_actions.perform()
        self.logger.log("Scrolling Icon menu")
        element2 = self.driver.find_elements_by_class_name("android.widget.Gallery")[0]
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, -1000, 0, 50).perform()
        touch_actions.perform()
        self.logger.log("Selecting Search Product")
        self.driver.find_elements_by_id("ivIcon")[2].click()
        sleep(1)
        self.logger.log("Searching for 'AYAK'")
        self.driver.find_element_by_id("etSearch").send_keys("ayak")
        self.driver.back()
        self.logger.log("Clicking Search")
        self.driver.find_element_by_id("tvSearch").click()
        sleep(1)
        self.logger.log("Scrolling item list")
        element3 = self.driver.find_element_by_class_name("android.widget.GridView")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element3, 0, -500, 100).perform()
        touch_actions.perform()
        self.logger.log("Selecting an item")
        self.driver.find_elements_by_id("ivIcon")[0].click()
        sleep(7)
        self.logger.log("Going back")
        self.driver.back()
        self.driver.back()
        self.driver.back()
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())
