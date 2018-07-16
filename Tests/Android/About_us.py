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

from time import sleep
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

user1 = "cihangok@yahoo.com"
pass1 = "1q2w3e4r"

class ABOUTUS(object):

    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("************************************", 'green')
        
    def test(self):

        self.appium_worker.entrance_android()
        self.appium_worker.bekle_android("drawer_indicator")
        sleep(0.5)
        self.logger.log("************************************")
        sleep(0.5)
        self.logger.log('About Us test initialized')
        sleep(0.5)
        self.logger.log("************************************")
        sleep(0.5)
        self.logger.log("Opening left sub-menu")
        self.driver.find_element_by_id("drawer_indicator").click()
        sleep(1)
        self.logger.log("Scrolling down")
        element2 = self.driver.find_element_by_class_name("android.widget.RelativeLayout")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -1000, 100).perform()
        touch_actions.perform()
        sleep(1)
        self.logger.log("Clicking About Us")
        self.driver.find_elements_by_class_name("android.widget.LinearLayout")[10].click()
        sleep(2)
        try:
            self.driver.find_element_by_id("tvAboutUs")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            self.logger.log("Clicking About Us")
            self.driver.find_element_by_id("tvAboutUs").click()
            sleep(1)
            self.logger.log("Scrolling down")
            element2 = self.driver.find_element_by_class_name("android.webkit.WebView")
            # element2 = self.driver.find_element_by_id("webview")
            touch_actions = TouchActions(self.driver)
            touch_actions.flick_element(element2, 0, -1500, 100).perform()
            touch_actions.perform()
            sleep(3)
            self.driver.back()
            try:
                self.driver.find_element_by_id("tvAboutUs")
                flag = 1
            except NoSuchElementException:
                flag = 0
            if flag == 1:
                self.logger.log("Clicking Terms")
                self.driver.find_element_by_id("tvTerms").click()
                sleep(1)
                self.logger.log("Scrolling down")
                element2 = self.driver.find_element_by_class_name("android.webkit.WebView")
                # element2 = self.driver.find_element_by_id("webview")
                touch_actions = TouchActions(self.driver)
                touch_actions.flick_element(element2, 0, -1800, 100).perform()
                touch_actions.perform()
                sleep(3)
                self.driver.back()
                try:
                    self.driver.find_element_by_id("tvAboutUs")
                    flag = 1
                except NoSuchElementException:
                    flag = 0
                if flag == 1:
                    self.logger.log("Clicking Privacy")
                    self.driver.find_element_by_id("tvPrivacy").click()
                    sleep(1)
                    self.logger.log("Scrolling down")
                    element2 = self.driver.find_element_by_class_name("android.webkit.WebView")
                    # element2 = self.driver.find_element_by_id("webview")
                    touch_actions = TouchActions(self.driver)
                    touch_actions.flick_element(element2, 0, -700, 100).perform()
                    touch_actions.perform()
                    sleep(3)
                    self.driver.back()
                    try:
                        self.driver.find_element_by_id("tvAboutUs")
                        flag = 1
                    except NoSuchElementException:
                        flag = 0
                    if flag == 1:
                        self.logger.log("Clicking FAQ")
                        self.driver.find_element_by_id("tvFaq").click()
                        sleep(1)
                        self.logger.log("Scrolling down")
                        element2 = self.driver.find_element_by_class_name("android.webkit.WebView")
                        # element2 = self.driver.find_element_by_id("webview")
                        touch_actions = TouchActions(self.driver)
                        touch_actions.flick_element(element2, 0, -1800, 100).perform()
                        touch_actions.perform()
                        sleep(3)
                        self.driver.back()
                        self.driver.back()
                        self.driver.back()
                        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())
                    else:
                        self.logger.log("ERROR")
                else:
                    self.logger.log("ERROR")
            else:
                self.logger.log("ERROR")
        else:
            self.logger.log("ERROR")
