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


class DELIVERED(object):
    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("**************************")

    def test(self):
        sleep(0.5)
        self.logger.log("************************************")
        sleep(1)
        self.logger.log('Delivered Orders test initialized', 'yellow')
        sleep(0.5)
        self.logger.log("**************************")
        user1 = "cihangok@yahoo.com"
        pass1 = "1q2w3e4r"
        err_flag = 0

        self.appium_worker.entrance_android()
        flag = 0
        while flag == 0:
            try:
                self.driver.find_element_by_id("ivSubmenuProfile")
                flag = 1
            except NoSuchElementException:
                sleep(1)
                flag = 0
        #self.driver.find_element_by_id("drawer_indicator").click()
        #sleep(1)
        #drawer = self.appium_worker.submenu()
        #if drawer == 2:
        #    self.logger.log("Scrolling up the screen")
        #    element2 = self.driver.find_element_by_class_name("android.widget.ListView")
        #    touch_actions = TouchActions(self.driver)
        #    touch_actions.flick_element(element2, 0, 1000, 100).perform()
        #    touch_actions.perform()
        #    sleep(1)
        #self.driver.find_element_by_class_name("android.widget.LinearLayout").click()
        self.logger.log("Clicking Inbox icon")
        self.driver.find_element_by_id("ivSubmenuInbox").click()
        sleep(1)
        self.logger.log("Clicking Delivered")
        self.driver.find_element_by_id("llDelivered").click()
        flag = 0
        while flag == 0:
            try:
                self.driver.find_element_by_class_name("android.widget.ListView")
                flag = 1
            except NoSuchElementException:
                flag = 0
                sleep(2)
        # sleep(5)
        element2 = self.driver.find_element_by_class_name("android.widget.ListView")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -500, 100).perform()
        touch_actions.perform()
        self.logger.log("Choosing a package")
        self.driver.find_elements_by_id("rlRoot")[3].click()
        p1 = self.driver.find_element_by_id("tvContent")
        p2 = self.driver.find_element_by_id("tvEntryDate")
        p3 = self.driver.find_element_by_id("tvDepartureDate")
        p4 = self.driver.find_element_by_id("tvDeliveryDate")
        self.logger.log("Content: " + p1.text)
        sleep(0.5)
        self.logger.log("Entry date: " + p2.text)
        sleep(0.5)
        self.logger.log("Departure date: " + p3.text)
        sleep(0.5)
        self.logger.log("Delivered date: " + p4.text)
        self.appium_worker.screenshot("package")
        self.driver.find_element_by_id("tvBottom").click()
        element2 = self.driver.find_element_by_class_name("android.widget.ListView")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -500, 100).perform()
        touch_actions.perform()
        self.logger.log("Choosing a package")
        self.driver.find_elements_by_id("rlRoot")[5].click()
        p1 = self.driver.find_element_by_id("tvContent")
        p2 = self.driver.find_element_by_id("tvEntryDate")
        p3 = self.driver.find_element_by_id("tvDepartureDate")
        p4 = self.driver.find_element_by_id("tvDeliveryDate")
        self.logger.log("Content: " + p1.text)
        sleep(0.5)
        self.logger.log("Entry date: " + p2.text)
        sleep(0.5)
        self.logger.log("Departure date: " + p3.text)
        sleep(0.5)
        self.logger.log("Delivered date: " + p4.text)
        self.driver.find_element_by_id("tvBottom").click()
        self.driver.back()
        self.driver.back()
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())