"""
UI iOS tests for AmerikadanIste app.
Ira Shyti 26-09-2016
"""

from appium import webdriver
import time
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
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException


class MAILBOXIOS(object):
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
        self.logger.log("Clicking left sub-menu")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]").click()
        self.logger.log("Clicking Mailbox")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[5]/"
                                          "UIAStaticText[1]").click()
        sleep(2)
        self.logger.log("Selecting a package")
        self.driver.find_elements_by_class_name("UIATableCell")[0].click()
        sleep(10)
        self.logger.log("Sender : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                            "UIAStaticText[4]").text)

        self.logger.log("US Carrier : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                                "UIAStaticText[5]").text)
        self.logger.log("Package Code : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                                  "UIAStaticText[8]").text)
        #self.logger.log("Content : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
        #                                                   "UIATableView[1]/UIATableCell[1]/").text)
        self.logger.log("Weight : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                            "UIATableView[1]/UIATableCell[2]/UIAStaticText[2]").text)
        self.logger.log("Received at : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                                 "UIATableView[1]/UIATableCell[3]/UIAStaticText[2]").text)
        self.logger.log("Clicking Choose to Send")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[5]").click()
        sleep(3)

        #self.appium_worker.bekle_ios("//UIAApplication[1]/UIAWindow[1]/UIAButton[4]")
        self.logger.log("Clicking Send Selected Packages")
        #self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[4]").click()
        self.driver.find_element_by_name("SEND SELECTED PACKAGES").click()
        sleep(5)
        self.logger.log("aaaa")

        try:
            self.driver.find_element_by_name("Pay Invoice")
            self.logger.log("bbb")
            flag1 = 1
        except NoSuchElementException:
            self.logger.log("ccc")
            flag1 = 0

        if flag1 == 1:
            self.logger.log("You have unpaid invoices")
            #self.logger.log("Message : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextView[3]").text)
            self.logger.log("Clicking to pay invoices")
            self.driver.find_element_by_name("Pay Invoice").click()
            sleep(3)
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/"
                                              "UIAButton[1]").click()
            sleep(2)

            self.logger.log("Entering Cardholder's First Name")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys("TestName")
            self.logger.log("Entering Cardholder's Last Name")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[2]").send_keys(
                "TestSurname")
            self.logger.log("Entering Card Number")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[3]").send_keys(
                "4090700214269159")
            self.logger.log("Entering CVC")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[5]").send_keys("494")
            self.logger.log("Selecting Expiration Date")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[4]").click()
            sleep(1)
            # self.driver.find_elements_by_class_name("UIAPickerWheel")[0].send_keys("1")
            self.driver.find_elements_by_class_name("UIAPickerWheel")[1].send_keys("2017")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAToolbar[1]/UIAButton[2]").click()
            self.logger.log("Clicking Done")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
            sleep(10)

            flag2 = 0
            flag3 = 0
            while flag2 == 0:
                try:
                    self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]"
                                                      "/UIAButton[1]")
                    flag3 = 1
                except NoSuchElementException:
                    self.logger.log("All invoices have been payed")
                    flag2 = 1

                if flag3 == 1:
                    self.driver.find_element_by_xpath(
                        "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/"
                        "UIAButton[1]").click()
                    sleep(2)

                    self.logger.log("Entering Cardholder's First Name")
                    self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys(
                        "TestName")
                    self.logger.log("Entering Cardholder's Last Name")
                    self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[2]").send_keys(
                        "TestSurname")
                    self.logger.log("Entering Card Number")
                    self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[3]").send_keys(
                        "4090700214269159")
                    self.logger.log("Entering CVC")
                    self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[5]").send_keys("494")
                    self.logger.log("Selecting Expiration Date")
                    self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[4]").click()
                    sleep(1)
                    # self.driver.find_elements_by_class_name("UIAPickerWheel")[0].send_keys("1")
                    self.driver.find_elements_by_class_name("UIAPickerWheel")[1].send_keys("2017")
                    self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAToolbar[1]/UIAButton[2]").click()
                    sleep(1)
                    self.logger.log("Clicking Done")
                    self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
                    sleep(6)
                    flag2 = 0

        elif flag1 == 0:
            self.logger.log("You don't have any unpaid invoices")
            sleep(2)

        self.logger.log("Shipment Details")
        self.logger.log("Package : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/"
                                                                         "UIAScrollView[1]/UIAStaticText[1]").text)
        self.logger.log("Lbs : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/"
                                                                     "UIAScrollView[1]/UIAStaticText[2]").text)
        self.logger.log("Clicking Continue")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[12]").click()
        sleep(2)
        self.logger.log("Payment information")
        self.logger.log("Entering Cardholder's First Name")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys(
            "TestName")
        self.logger.log("Entering Cardholder's Last Name")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[2]").send_keys(
            "TestSurname")
        self.logger.log("Entering Card Number")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[3]").send_keys(
            "4090700214269159")
        self.logger.log("Entering CVC")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[5]").send_keys("494")
        self.logger.log("Selecting Expiration Date")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[4]").click()
        sleep(1)
        # self.driver.find_elements_by_class_name("UIAPickerWheel")[0].send_keys("1")
        self.driver.find_elements_by_class_name("UIAPickerWheel")[1].send_keys("2017")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAToolbar[1]/UIAButton[2]").click()
        sleep(1)
        self.logger.log("Clicking Done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        sleep(5)
        self.logger.log("Clicking Done")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        flag4 = 0
        while flag4 == 0:
            try:
                self.driver.find_element_by_name("Promotions")
                flag4 = 1
            except NoSuchElementException:
                self.logger.log("Wait")
                sleep(1)
                flag4 = 0
        self.logger.log("Order Completed")
        self.logger.log("Clicking Done ")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]").click()
        sleep(2)
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())


