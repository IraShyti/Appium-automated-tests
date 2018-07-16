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


class SUPPORT(object):
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
        self.logger.log('Support test initialized', 'yellow')
        sleep(0.5)
        self.logger.log("************************************", 'green')
        user1 = 'cihangok@yahoo.com'
        pass1 = '1q2w3e4r'
        flag2 = 0
        err_flag = 0
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

        self.logger.log("Clicking Support")
        self.driver.find_elements_by_class_name("android.widget.LinearLayout")[9].click()
        sleep(1)
        try:
            self.driver.find_element_by_id("rlCall")
            flag = 1
        except NoSuchElementException:
            self.logger.log("ERROR")
            err_flag += 1
            flag = 0
        if flag == 1:
            self.logger.log("Clicking MESSAGES")
            self.driver.find_element_by_id("tvMessages").click()
            sleep(1)
            try:
                self.driver.find_element_by_id("tvNewMessage")
                flag = 1
            except NoSuchElementException:
                self.logger.log("ERROR")
                err_flag += 1
                flag = 0
            if flag == 1:
                self.logger.log("Scrolling down the screen")
                element2 = self.driver.find_element_by_class_name("android.widget.ListView")
                touch_actions = TouchActions(self.driver)
                touch_actions.flick_element(element2, 0, -500, 100).perform()
                touch_actions.perform()
                sleep(1)
                self.logger.log("Opening a message")
                self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[6].click()
                sleep(1)
                try:
                    self.driver.find_element_by_id("tvReply")
                    flag = 1
                except NoSuchElementException:
                    flag = 0
                    self.logger.log("ERROR")
                    err_flag += 1
                if flag == 1:
                    self.logger.log("Clicking REPLY")
                    self.driver.find_element_by_id("tvReply").click()
                    self.logger.log("Clicking SEND")
                    self.driver.find_element_by_id("tvSend").click()
                    self.appium_worker.screenshot("Empty_fields")
                    self.driver.find_element_by_id("etMessage").send_keys("Test reply")
                    self.driver.back()
                    self.logger.log("Clicking SEND")
                    self.driver.find_element_by_id("tvSend").click()
                    self.driver.back()
                    self.logger.log("Clicking NEW MESSAGE")
                    self.driver.find_element_by_id("tvNewMessage").click()
                    self.logger.log("Typing subject")
                    self.driver.find_element_by_id("etSubject").send_keys("test subject")
                    self.logger.log("Clicking SEND")
                    self.driver.find_element_by_id("tvSend").click()
                    sleep(0.5)
                    self.appium_worker.screenshot("Empty_fields")
                    sleep(0.5)
                    self.logger.log("Typing mesage")
                    self.driver.find_element_by_id("etMessage").send_keys("Test message")
                    self.driver.back()
                    self.logger.log("Clicking SEND")
                    self.driver.find_element_by_id("tvSend").click()
                    sleep(0.5)
                    self.appium_worker.screenshot("Message_sent")
                    self.driver.back()
                    self.logger.log("Clicking CALL ME")
                    self.driver.find_element_by_id("tvCallMe").click()
                    try:
                        self.driver.find_element_by_id("tvOK")
                        flag = 1
                    except NoSuchElementException:
                        flag = 0
                        self.logger.log("Unexpected ERROR")
                        err_flag += 1
                    if flag == 1:
                        self.logger.log("Entering subject")
                        self.driver.find_element_by_id("etSubject").send_keys("Delay")
                        self.driver.find_element_by_id("tvOK").click()
                        sleep(1)
                        self.appium_worker.screenshot("Empty_fields")
                        sleep(0.5)
                        self.logger.log("Selecting time")
                        self.driver.find_element_by_id("tvTime").click()
                        self.driver.find_elements_by_class_name("android.view.View")[25].click()
                        self.driver.find_element_by_id("button1").click()
                        self.driver.back()
                        self.logger.log("Clicking OK")
                        self.driver.find_element_by_id("tvOK").click()
                        sleep(1)
                        self.appium_worker.screenshot("Beni_ara")
                        self.logger.log("Clicking OK")
                        self.driver.find_element_by_id("tvOK").click()
                        sleep(2)
                        self.driver.back()
                        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())
            else:
                print 'ok2'
                self.appium_worker.screenshot("Unexpected_error")
                self.driver.back()
                self.driver.back()
                self.driver.back()
                self.driver.back()
