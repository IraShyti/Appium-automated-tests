from appium_worker import AppiumWorker
from Utilities.logger import Logger

from appium_worker import webdriver
import unittest
import random
import IOS
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
        self.logger.log('What To Buy test initialized', 'yellow')
        self.logger.log("************************************", 'green')

    def test(self):
        self.appium_worker.entrance()
        try:
            self.driver.find_element_by_id("ivSubmenuWhatToBuy")
            flag1 = 1
        except:
            try:
                self.driver.find_element_by_id("fancyCoverFlow")
                flag1 = 2
            except NoSuchElementException:
                sleep(1)
        if flag1 == 1:
            self.logger.log("Clicking What To Buy button")
            self.appium_worker.bekle("ivSubmenuWhatToBuy")
            self.driver.find_element_by_id("ivSubmenuWhatToBuy").click()
        if flag1 == 2:
            sleep(1)
        self.logger.log("fancy")
        #self.appium_worker.bekle("fancyCoverFlow")
        self.driver.find_elements_by_class_name("android.widget.Gallery")[0]
        self.driver.find_elements_by_id("ivIcon")[0].click()
        self.logger.log("Scrolling icon menu")
        element = self.driver.find_elements_by_class_name("android.widget.Gallery")[0]
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element, -500, 0, 50).perform()
        touch_actions.perform()
        sleep(3)
        self.driver.find_elements_by_id("ivIcon")[0].click()
        sleep(3)
        self.logger.log("Scrolling list menu")
        element1 = self.driver.find_elements_by_class_name("android.widget.Gallery")[1]
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element1, -400, 0, 100).perform()
        touch_actions.perform()
        sleep(3)
        self.driver.find_elements_by_id("textView")[1].click()
        sleep(3)
        self.logger.log("Scrolling down items")
        element2 = self.driver.find_element_by_class_name("android.widget.GridView")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -500, 100).perform()
        touch_actions.perform()
        sleep(3)
        self.logger.log("Scrolling icon menu")
        self.driver.find_elements_by_id("gridview")[0].click()
        el2 = self.driver.find_elements_by_class_name("android.widget.Gallery")[0]
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(el2, -200, 0, 50).perform()
        touch_actions.perform()
        self.driver.find_elements_by_id("ivIcon")[2].click()
        sleep(1)
        self.logger.log("Scrolling down items")
        el3 = self.driver.find_element_by_class_name("android.widget.GridView")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(el3, 0, -500, 100).perform()
        touch_actions.perform()
        element2 = self.driver.find_elements_by_class_name("android.widget.Gallery")[0]
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, -1000, 0, 50).perform()
        touch_actions.perform()
        self.driver.find_elements_by_id("ivIcon")[2].click()
        sleep(1)
        self.logger.log("Searching for 'ayak'")
        self.driver.find_element_by_id("etSearch").send_keys("ayak")
        self.logger.log("Clicking to search")
        self.driver.find_element_by_id("tvSearch").click()
        sleep(3)
        self.driver.back()
        self.appium_worker.bekle("tvName")
        self.appium_worker.screenshot("search.png")
        self.driver.back()
        self.driver.back()
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())
