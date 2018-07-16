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


class NOTIFICATIONS(object):
    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger


    def choice(self):
        flag = 0
        try:
            self.driver.find_element_by_id("tvNavigate")
            flag = 1
        except NoSuchElementException:
            try:
                self.driver.find_element_by_id("tvClose")
                flag = 2
            except NoSuchElementException:
                try:
                    self.driver.find_element_by_id("ivFav")
                    flag = 3
                except NoSuchElementException:
                    self.logger.log("choice")

        if flag == 1:
            fl = 0
            self.driver.find_element_by_id("tvNavigate").click()
            try:
                self.driver.find_element_by_id("etEmail")
                fl = 1
            except NoSuchElementException:
                try:
                    self.driver.find_element_by_id("tvNavigate")
                    fl = 2
                except NoSuchElementException:
                    sleep(0.5)
                    #self.logger.log("This type of notification can not be opened")
            if fl == 1:
                self.driver.find_element_by_id("etEmail").send_keys("cihangok@yahoo.com")
                self.driver.find_element_by_id("btnSend").click()
                self.driver.back()
                self.driver.back()
                self.driver.back()
            if fl == 2:
                self.driver.back()
            else:
                self.driver.find_element_by_id("tvReply").click()
                self.driver.find_element_by_id("etMessage").send_keys("Test reply")
                self.driver.back()
                self.driver.find_element_by_id("tvSend").click()
                self.driver.back()
                self.driver.back()
        if flag == 2:
            self.driver.find_element_by_id("tvClose").click()
            sleep(1)
        if flag == 3:
            self.driver.find_element_by_id("ivFav").click()
            sleep(1)

    def test(self):
        sleep(0.5)
        self.logger.log("************************************")
        sleep(0.5)
        self.logger.log('Notifications test initialized', 'yellow')
        sleep(0.5)
        self.logger.log("********************************")
        self.appium_worker.entrance_android()
        self.logger.log("Clicking left sub-menu")
        self.driver.find_element_by_id("drawer_indicator").click()
        drawer = self.appium_worker.submenu()
        if drawer == 2:
            self.logger.log("Scrolling up the screen")
            element2 = self.driver.find_element_by_class_name("android.widget.ListView")
            touch_actions = TouchActions(self.driver)
            touch_actions.flick_element(element2, 0, 1000, 100).perform()
            touch_actions.perform()
            sleep(1)

        self.logger.log("Notifications")
        self.driver.find_elements_by_class_name("android.widget.LinearLayout")[10].click()
        self.logger.log("Choosing a notification")
        self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[5].click()
        sleep(1)
        self.appium_worker.screenshot("Notification")
        self.choice()
        element2 = self.driver.find_element_by_class_name("android.widget.ListView")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -500, 100).perform()
        touch_actions.perform()
        self.logger.log("Choosing a notification")
        self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[8].click()
        sleep(1)
        self.appium_worker.screenshot("Notification")
        self.choice()
        element2 = self.driver.find_element_by_class_name("android.widget.ListView")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -500, 100).perform()
        touch_actions.perform()
        self.logger.log("Choosing a notification")
        self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[13].click()
        sleep(1)
        self.appium_worker.screenshot("Notification")
        self.choice()
        element2 = self.driver.find_element_by_class_name("android.widget.ListView")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -500, 100).perform()
        touch_actions.perform()
        self.logger.log("Choosing a notification")
        self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[11].click()
        sleep(1)
        self.appium_worker.screenshot("Notification")
        self.choice()
        element2 = self.driver.find_element_by_class_name("android.widget.ListView")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -500, 100).perform()
        touch_actions.perform()
        #self.logger.log("Choosing a notification")
        #self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[13].click()
        #sleep(1)
        #self.appium_worker.screenshot("Notification")
        #self.choice()
        sleep(1)
        self.logger.log("Clicking to go to Home page")
        self.driver.find_element_by_id("ivSubmenuHome").click()
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())
