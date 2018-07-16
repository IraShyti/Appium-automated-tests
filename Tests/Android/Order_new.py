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


class NEWORDER(object):
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

        sleep(0.5)
        self.logger.log('New Order test case initialized', 'yellow')
        sleep(0.5)
        self.logger.log("********************************")

        flag_err = 0

        self.appium_worker.entrance_android()
        self.appium_worker.bekle_android("drawer_indicator")
        #self.logger.log("Clicking left sub menu")
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
        #self.logger.log("Clicking 'NEW ORDER' button")
        #self.driver.find_element_by_class_name("android.widget.LinearLayout").click()
        sleep(1)
        self.logger.log("Clicking Inbox icon")
        self.driver.find_element_by_id("ivSubmenuInbox").click()
        sleep(1)
        self.logger.log("Clicking New")
        self.driver.find_element_by_id("llNew").click()
        self.logger.log("Continue without selecting shopping site")
        sleep(1)
        try:
            self.driver.find_element_by_id("tvSaveShopping")
            flag = 1
        except NoSuchElementException:
            flag = 0
            self.appium_worker.screenshot("Unexpected error")
        if flag == 0:
            self.logger.log("ERROR was not expected", 'red')
            flag_err += 1
            self.driver.close()
        self.driver.find_element_by_id("tvSaveShopping").click()
        try:
            self.driver.find_element_by_id("tvPositive")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 0:
            self.logger.log("ERROR", 'red')
            self.logger.log("Warning message was expected", 'red')
            flag_err += 1
        if flag == 1:
            self.logger.log("Warning message for not choosing shopping site", 'green')
            self.appium_worker.screenshot("site_warning")
            flag = 0
            while flag == 0:

                try:
                    self.driver.find_element_by_id("tvPositive")
                    flag = 1
                    fl1 = 1
                except NoSuchElementException:
                    sleep(0.5)
                    flag = 0
                    fl1 = 0
                if fl1 == 1:
                    self.driver.find_element_by_id("tvPositive").click()

            self.logger.log("Selecting shopping site")
            # try:
            #    self.driver.find_element_by_id("etShoppingSite")
            # except NoSuchElementException:
            #    sleep(1)
            try:
                self.driver.find_element_by_id("etShoppingSite").click()
                flag = 1
            except NoSuchElementException:
                flag = 0
                self.appium_worker.screenshot("Unexpected error")
            if flag == 1:
                self.driver.find_element_by_id("etShoppingSite").click()
                flag = 0
                while flag == 0:
                    choice = random.randint(0, 5)
                    self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[2].click()
                    sleep(1)
                    try:
                        self.driver.find_element_by_id("etShoppingSite")
                        flag = 1
                    except NoSuchElementException:
                        sleep(0.5)
                        flag = 0
                txt = self.driver.find_element_by_id("etShoppingSite").text
                self.logger.log("Selected '" + self.funct_decode(txt) + "' shopping site", 'blue')

                self.logger.log("Adding details")
                self.driver.find_element_by_id("etShoppingContent").send_keys("clothing")
                self.logger.log("Adding note")
                self.driver.find_element_by_id("etShoppingNote").send_keys("test")
                self.driver.back()
                self.logger.log("Select option for original box")
                self.driver.find_element_by_id("cbOriginalBoxRequest").click()
                self.logger.log("Things to know")
                self.driver.find_element_by_id("tvThingsToKnow").click()
                sleep(1)
                self.logger.log("Clicking 'OK' button")
                self.driver.find_element_by_id("tvOK").click()
                self.logger.log("Save shopping")
                self.driver.find_element_by_id("tvSaveShopping").click()
                try:
                    self.driver.find_element_by_id("tvShoppingSaved")
                    flag = 1
                except NoSuchElementException:
                    flag = 0
                if flag == 1:
                    sleep(1)
                    self.logger.log("Order given", 'green')
                    flag = 0
                    while flag == 0:
                        try:
                            self.driver.find_element_by_id("imageView")
                            flag = 1
                        except NoSuchElementException:
                            flag = 0
                    self.logger.log("Scrolling image to the right")
                    element2 = self.driver.find_element_by_id("imageView")
                    touch_actions = TouchActions(self.driver)
                    touch_actions.flick_element(element2, -400, 0, 100).perform()
                    touch_actions.perform()
                    sleep(2)
                    self.logger.log("Scrolling image to the right")
                    element2 = self.driver.find_element_by_id("imageView")
                    touch_actions = TouchActions(self.driver)
                    touch_actions.flick_element(element2, -400, 0, 100).perform()
                    touch_actions.perform()
                    sleep(2)
                    self.appium_worker.screenshot("Order_given")
        self.driver.back()
        self.driver.back()
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())

        if flag_err == 0:
            self.logger.log("Test finished without errors \n")
        else:
            self.logger.log("Test finished with  %d errors \n" % flag_err)
