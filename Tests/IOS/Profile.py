"""
UI iOS tests for AmerikadanIste app.
Ira Shyti 23-09-2016
"""

from appium import webdriver
import codecs
import datetime
from codecs import decode
from datetime import datetime
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


class TestMyProfileIOS(object):
    log_flag = 0

    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("**************************")

    def test(self):

        self.appium_worker.entrance_ios()
        flag1 = 0
        while flag1 == 0:
            try:
                self.driver.find_element_by_xpath(
                    "//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[5]")
                flag1 = 1
            except NoSuchElementException:
                flag1 = 0
                self.logger.log("Wait")
                sleep(1)
        self.logger.log("Clicking My Profile")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[5]").click()
        sleep(1)
        #m1 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[1]").text
        #self.logger.log("Name of user : " + m1)
        #m2 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[2]").text
        #self.logger.log("Birthday is : " + m2)
        #m3 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[1]").text
        #m4 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[2]").text
        #m5 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[3]").text
        #m6 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[4]").text
        #m7 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[5]").text
        #self.logger.log(m3 + " " + m4 + " " + m5 + " " + m6 + " " + m7)
        #m8 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[6]")
        #m9 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[7]")
        #self.logger.log(str(m8) + " : " + str(m9))
        #self.logger.log("Pressing edit e-mail button")
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[1]").click()
        #flag1 = 0
        #while flag1 == 0:
        #    try:
        #        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[3]/UIAAlert[1]/UIACollectionView[1]/"
        #                                          "UIACollectionCell[1]/UIAButton[1]")
        #        flag1 = 1
        #    except NoSuchElementException:
        #        flag1 = 0
        #        sleep(1)
        #self.logger.log("Entering email 'cihangok@yahoo.com")
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[3]/UIAAlert[1]/UIAScrollView[1]/UIATab"
        #                                  "leView[1]/UIATableCell[1]/UIATextField[1]").send_keys("cihangok@yahoo.com")
        #self.logger.log("Pressing cancel")
        #self.driver.find_element_by_xpath(" //UIAApplication[1]/UIAWindow[3]/UIAAlert[1]/UIACollectionView[1]/"
        #                                  "UIACollectionCell[1]/UIAButton[1]").click()
        #m1 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[8]").text
        #m2 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[9]").text
        #self.logger.log(m1 + " : " + m2)
        #self.logger.log("Pressing to edit phone number")
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[2]").click()
        #sleep(5)
        #self.logger.log("Selecting a number")
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[2]/UIATableCell[2]/"
        #                                  "UIAStaticText[1]").click()
        #self.logger.log("Warning message for default phone number is expected")
        #flag1 = 0
        #count = 0
        #while flag1 == 0 and count < 5:
        #    try:
        #        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[5]")
        #        flag1 = 1
        #    except NoSuchElementException:
        #        sleep(1)
        #        count += 1
        #        flag1 = 0
        #if flag1 == 0:
        #    self.logger.log("Warning message not shown")
        #elif flag1 == 1:
        #    self.logger.log("Warning message shown")
        #    self.logger.log("Pressing Continue")
        #    self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[5]").click()
#
        m1 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[10]").text
        m2 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[11]").text
        self.logger.log(m1 + " : " + m2)
        sleep(2)
        self.logger.log("Clicking to edit Address")
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[3]").click()
        #self.driver.find_element_by_xpath("// //UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAImage[9]"
        #                                  "[@name= 'icon_button_edit_gray' ").click()
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[3]").click()
        sleep(5)
        self.logger.log("Pressing to add new address")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").clear()
        self.logger.log("Entering address title")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys("Home")
        self.logger.log("Entering full address")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/"
                                          "UIATextView[1]").send_keys("Zeytnioglu Cad")

        self.logger.log("Entering Zip code")
        self.driver.find_elements_by_class_name("UIATextView")[1].send_keys("1000")
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/"
        #                                  "UIATextField[1]").send_keys("1000")

        self.logger.log("Selecting country")

        self.logger.log("Clicking Done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAToolbar[1]/UIAButton[2]").click()
        self.logger.log("Selecting city")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATextField[3]").click()
        self.logger.log("Clicking done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAToolbar[1]/UIAButton[2]").click()
        self.logger.log("Selecting country")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATextField[4]").click()
        element2 = self.driver.find_element_by_xpath("/UIAApplication[1]/UIAWindow[2]/UIAPicker[1]/UIAPickerWheel[1]")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -300, 100).perform()
        touch_actions.perform()
        sleep(1)
        self.logger.log("Clicking done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAToolbar[1]/UIAButton[2]").click()
        self.logger.log("Scrolling down")
        element2 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -300, 100).perform()
        touch_actions.perform()
        sleep(1)
        self.logger.log("Setting address as default")
        self.driver.find_element_by_xpath(" //UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAImage[1]").click()
        self.logger.log("Saving address")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAButton[2]").click()
        self.logger.log("Clicking back button")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]").click()
        sleep(3)
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())

