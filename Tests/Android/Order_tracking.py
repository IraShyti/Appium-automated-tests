from Utilities.logger import Logger

from Tests.appium_worker import webdriver
import unittest
import random
import os
import time
from time import sleep
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException


class TRACKING(object):
    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("**************************")

    def funct_decode(self, the_string):
        strng = codecs.encode(the_string, 'utf-8')
        return strng

    def test(self):
        sleep(0.5)
        self.logger.log("************************************")

        sleep(1)
        self.logger.log('Order Tracking test initialized', 'yellow')
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
        #self.logger.log("Clicking left sub-menu")
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
        sleep(1)
        self.logger.log("Clicking Inbox icon")
        self.driver.find_element_by_id("ivSubmenuInbox").click()
        sleep(1)
        self.logger.log("Clicking Tracking")
        self.driver.find_element_by_id("llTracking").click()
        fl2 = 0
        while fl2 == 0:
            try:
                self.driver.find_elements_by_id("rlRoot")[1]
                fl2 = 1
            except NoSuchElementException:
                self.logger.log("wait")
                sleep(1)
                fl2 = 0
        self.logger.log("Selecting one order")
        self.driver.find_elements_by_id("rlRoot")[1].click()
        try:
            self.driver.find_element_by_id("tvBottom")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            m1 = self.driver.find_element_by_id("tvContent").text
            m2 = self.driver.find_element_by_id("tvEntryDate").text
            m3 = self.driver.find_element_by_id("tvDepartureDate").text
            m4 = self.driver.find_element_by_id("tvTrackingCode").text
            m5 = self.driver.find_element_by_id("tvSender").text
            m6 = self.driver.find_element_by_id("tvPackageCode").text
            self.logger.log("Content: " + self.funct_decode(str(m1)))
            sleep(0.5)
            self.logger.log("Enty date: " + self.funct_decode(str(m2)))
            sleep(0.5)
            self.logger.log("Departure date: " + self.funct_decode(str(m3)))
            sleep(0.5)
            #self.logger.log("Tacking code " + self.funct_decode(str(m4)))
            sleep(0.5)
            self.logger.log("Sender: " + self.funct_decode(str(m5)))
            sleep(0.5)
            self.logger.log("Code: " + self.funct_decode(str(m6)))
            if self.driver.find_element_by_id("tvBottom").text is "OK":
                flag = 1
            elif self.driver.find_element_by_id("tvBottom").text is "DETAILED TRACKING":
                flag = 0
            if flag == 1:
                self.driver.find_element_by_id("tvBottom").click()
            elif flag == 0:
                self.driver.find_element_by_id("tvBottom").click()
                sleep(3)
                self.driver.back()
                self.driver.back()
        self.logger.log("Scrolling down list")
        element2 = self.driver.find_element_by_id("rlList")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -200, 100).perform()
        touch_actions.perform()
        sleep(1)
        self.logger.log("Scrolled")

        self.logger.log("Selecting one order")
        self.driver.find_element_by_id("rlRoot").click()
        try:
            self.driver.find_element_by_id("tvBottom")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            m1 = self.driver.find_element_by_id("tvContent").text
            m2 = self.driver.find_element_by_id("tvEntryDate").text
            m3 = self.driver.find_element_by_id("tvDepartureDate").text
            m4 = self.driver.find_element_by_id("tvTrackingCode").text
            m5 = self.driver.find_element_by_id("tvSender").text
            m6 = self.driver.find_element_by_id("tvPackageCode").text
            self.logger.log("Content: " + self.funct_decode(str(m1)))
            sleep(0.5)
            self.logger.log("Enty date: " + self.funct_decode(str(m2)))
            sleep(0.5)
            self.logger.log("Departure date: " + self.funct_decode(str(m3)))
            sleep(0.5)
            #self.logger.log("Tacking code " + self.funct_decode(str(m4)))
            sleep(0.5)
            self.logger.log("Sender: " + self.funct_decode(str(m5)))
            sleep(0.5)
            self.logger.log("Code: " + self.funct_decode(str(m6)))
            if self.driver.find_element_by_id("tvBottom").text is "OK":
                flag = 1
            elif self.driver.find_element_by_id("tvBottom").text is "DETAILED TRACKING":
                flag = 0
            if flag == 1:
                self.driver.find_element_by_id("tvBottom").click()
            elif flag == 0:
                self.driver.find_element_by_id("tvBottom").click()
                sleep(3)
                self.driver.back()
                self.driver.back()

        self.logger.log("Scrolling down list")
        element2 = self.driver.find_element_by_id("rlList")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -500, 100).perform()
        touch_actions.perform()
        sleep(1)
        self.logger.log("Scrolled")
        self.logger.log("Selecting one order")
        self.driver.find_elements_by_id("rlWrapper")[4].click()
        try:
            self.driver.find_element_by_id("tvBottom")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            m1 = self.driver.find_element_by_id("tvContent").text
            m2 = self.driver.find_element_by_id("tvEntryDate").text
            m3 = self.driver.find_element_by_id("tvDepartureDate").text
            m4 = self.driver.find_element_by_id("tvTrackingCode").text
            m5 = self.driver.find_element_by_id("tvSender").text
            m6 = self.driver.find_element_by_id("tvPackageCode").text
            self.logger.log("Content: " + self.funct_decode(str(m1)))
            sleep(0.5)
            self.logger.log("Enty date: " + self.funct_decode(str(m2)))
            sleep(0.5)
            self.logger.log("Departure date: " + self.funct_decode(str(m3)))
            sleep(0.5)
            #self.logger.log("Tacking code " + self.funct_decode(str(m4)))
            sleep(0.5)
            self.logger.log("Sender: " + self.funct_decode(str(m5)))
            sleep(0.5)
            self.logger.log("Code: " + self.funct_decode(str(m6)))
            if self.driver.find_element_by_id("tvBottom").text is "OK":
                flag = 1
            elif self.driver.find_element_by_id("tvBottom").text is "DETAILED TRACKING":
                flag = 0
            if flag == 1:
                self.driver.find_element_by_id("tvBottom").click()
            elif flag == 0:
                self.driver.find_element_by_id("tvBottom").click()
                sleep(3)
                self.driver.back()
                self.driver.back()


        self.driver.back()
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())