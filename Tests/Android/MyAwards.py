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


class MYAWARDS(object):
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
        self.logger.log('My Awards test initialized', 'yellow')
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
        self.logger.log("Clicking My Awards")
        self.driver.find_elements_by_class_name("android.widget.LinearLayout")[13].click()
        sleep(1)
        try:
            self.driver.find_element_by_id("rlAvailableAwards")
            flag = 1
        except NoSuchElementException:
            self.logger.log("ERROR")
            flag = 0
        if flag == 1:
            self.logger.log("Available awards")
            sleep(2)
            self.appium_worker.screenshot("awards")
            self.driver.find_element_by_id("rlUsedAwards").click()
            sleep(1)
            el1 = self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[2]
            self.logger.log("Date of used award : " + self.logger.funct_decode(el1.find_element_by_id("tvDetail").text))
            self.logger.log("Price used for award: " + self.logger.funct_decode(el1.find_element_by_id("tvAmount").text))
            try:
                el1.find_element_by_id("tvHeader")
                flag = 1
            except NoSuchElementException:
                flag = 0
            if flag == 1:
                self.logger.log("Message of award is : " + el1.find_element_by_id("tvHeader").text)
            self.logger.log("Scrolling")
            element2 = self.driver.find_element_by_class_name("android.widget.ListView")
            touch_actions = TouchActions(self.driver)
            touch_actions.flick_element(element2, 0, -800, 100).perform()
            touch_actions.perform()
            sleep(2)
            el1 = self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[5]
            self.logger.log("Date of used award : " + self.logger.funct_decode(el1.find_element_by_id("tvDetail").text))
            self.logger.log("Price used for award: " + self.logger.funct_decode(el1.find_element_by_id("tvAmount").text))
            # print "aaaa"
            # try:
            #     el1.find_element_by_id("tvHeader")
            #     flag = 1
            # except NoSuchElementException:
            #     flag = 0
            # print "aaaa"
            # if flag == 1:
            #     self.logger.log("Message of award is : " + self.logger.funct_decode(str(el1.find_element_by_id("tvHeader").text)))
            # print "aaa"
            self.driver.back()
            self.driver.back()
            self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())
        else:
            self.logger.log("ERROR")
