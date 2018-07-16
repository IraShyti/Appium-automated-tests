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


class WAITING(object):
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
        self.logger.log('Order Waiting test initialized', 'yellow')
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
        #self.logger.log("Clicking left sub-menu")
        #self.driver.find_element_by_id("drawer_indicator").click()
        #sleep(1)
        #self.driver.find_element_by_class_name("android.widget.LinearLayout").click()
        sleep(1)
        self.logger.log("Clicking Inbox icon")
        self.driver.find_element_by_id("ivSubmenuInbox").click()
        sleep(1)
        self.logger.log("Clicking Waiting")
        self.driver.find_element_by_id("llWaiting").click()
        self.logger.log("Scrolling down list")
        element2 = self.driver.find_element_by_class_name("android.widget.FrameLayout")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -500, 100).perform()
        touch_actions.perform()
        sleep(3)
        self.logger.log("Scrolled")
        self.logger.log("Selecting order")
        self.logger.log("Selecting package")
        self.driver.find_elements_by_id("rlWrapper")[3].click()
        sleep(1)

        try:
            self.driver.find_element_by_id("tvAddNote")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            self.logger.log("Clicking Add Note")
            self.driver.find_element_by_id("tvAddNote").click()
            self.driver.find_element_by_id("etNote").send_keys("Test note")
            self.driver.back()
            self.logger.log("Clicking Save")
            self.driver.find_element_by_id("tvSave").click()
            sleep(2)
        try:
            self.driver.find_element_by_id("ivAddTrackingCode")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            self.logger.log("Clicking to add Tracking Code")
            self.driver.find_element_by_id("ivAddTrackingCode").click()
            self.logger.log("Adding Tracking Code as 1234")
            self.driver.find_element_by_id("etTrackingCode").send_keys("1234")
            self.logger.log("Selecting US Carrier as UPS")
            self.driver.find_element_by_id("ivUPS").click()
            self.logger.log("Clicking OK")
            self.driver.find_element_by_id("tvOK").click()
            sleep(1)
        try:
            self.driver.find_element_by_id("ivAdd")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            self.driver.find_element_by_id("ivAdd").click()
            self.driver.back()
        m1 = self.driver.find_element_by_id("etContent").text
        m2 = self.driver.find_element_by_id("tvCreationDate").text
        m3 = self.driver.find_element_by_id("tvNote").text
        m4 = self.driver.find_element_by_id("tvSender").text
        m5 = self.driver.find_element_by_id("tvPackageCode").text
        self.logger.log("Content: " + self.funct_decode(str(m1)))
        sleep(0.5)
        self.logger.log("Creation date: " + self.funct_decode(str(m2)))
        sleep(0.5)
        self.logger.log("Note : " + self.funct_decode(str(m3)))
        sleep(0.5)
        self.logger.log("Sender: " + self.funct_decode(str(m4)))
        sleep(0.5)
        self.logger.log("Package Code: " + self.funct_decode(str(m5)))
        sleep(0.5)
        self.logger.log("Clicking Waiting Packages")
        self.driver.find_element_by_id("tvWaitingPackages").click()
        # self.driver.back()
        self.logger.log("Scrolling down list")
        element2 = self.driver.find_element_by_class_name("android.widget.FrameLayout")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -500, 100).perform()
        touch_actions.perform()
        sleep(3)
        self.logger.log("Scrolled")
        self.logger.log("Selecting package")
        self.driver.find_elements_by_id("rlWrapper")[5].click()
        try:
            self.driver.find_element_by_id("tvAddNote")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            self.logger.log("Clicking Add Note")
            self.driver.find_element_by_id("tvAddNote").click()
            self.driver.find_element_by_id("etNote").send_keys("Test note")
            self.driver.back()
            self.logger.log("Clicking Save")
            self.driver.find_element_by_id("tvSave").click()
            sleep(2)
        try:
            self.driver.find_element_by_id("ivAddTrackingCode")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            self.logger.log("Clicking to add Tracking Code")
            self.driver.find_element_by_id("ivAddTrackingCode").click()
            self.logger.log("Adding Tracking Code as 1234")
            self.driver.find_element_by_id("etTrackingCode").send_keys("1234")
            self.logger.log("Selecting US Carrier as UPS")
            self.driver.find_element_by_id("ivUPS").click()
            self.logger.log("Clicking OK")
            self.driver.find_element_by_id("tvOK").click()
            sleep(1)
        try:
            self.driver.find_element_by_id("ivAdd")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            self.driver.find_element_by_id("ivAdd").click()
            self.driver.find_element_by_id("etTrackingCode").send_keys("1234")
            self.driver.find_element_by_id("tvOK").click()
            # self.driver.back()
        m1 = self.driver.find_element_by_id("etContent").text
        m2 = self.driver.find_element_by_id("tvCreationDate").text
        m3 = self.driver.find_element_by_id("tvNote").text
        m4 = self.driver.find_element_by_id("tvSender").text
        m5 = self.driver.find_element_by_id("tvPackageCode").text
        self.logger.log("Content: " + self.funct_decode(str(m1)))
        sleep(0.5)
        self.logger.log("Creation date: " + self.funct_decode(str(m2)))
        sleep(0.5)
        self.logger.log("Note : " + self.funct_decode(str(m3)))
        sleep(0.5)
        self.logger.log("Sender: " + self.funct_decode(str(m4)))
        sleep(0.5)
        self.logger.log("Package Code: " + self.funct_decode(str(m5)))
        sleep(0.5)
        self.logger.log("Clicking Waiting Packages")
        self.driver.find_element_by_id("tvWaitingPackages").click()
        # self.driver.back()
        self.logger.log("Clicking one order to delete")
        self.driver.find_elements_by_id("ivIcon")[2].click()
        sleep(1)
        self.appium_worker.screenshot("Deleting_order")
        sleep(1)
        self.logger.log("Clicking No")
        self.driver.find_element_by_id("tvNegative").click()
        self.logger.log("Going back")
        self.driver.back()

        self.driver.back()
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())