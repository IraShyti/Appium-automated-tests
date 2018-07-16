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


class SHARE(object):
    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("*****************************", 'green')


    def test(self):
        sleep(0.5)
        self.logger.log("************************************")
        sleep(0.5)
        self.logger.log('Share test initialized', 'yellow')
        sleep(0.5)
        self.logger.log("*****************************", 'green')
        self.appium_worker.entrance_android()
        self.appium_worker.bekle_android("drawer_indicator")
        self.logger.log("Opening left sub-menu")
        self.driver.find_element_by_id("drawer_indicator").click()
        sleep(1)
        self.logger.log("Scrolling down")
        element2 = self.driver.find_element_by_class_name("android.widget.RelativeLayout")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -1000, 100).perform()
        touch_actions.perform()
        sleep(1)
        self.logger.log("Clicking Share")
        self.driver.find_elements_by_class_name("android.widget.LinearLayout")[12].click()
        self.appium_worker.bekle_android("tvContacts")
        self.logger.log("Clicking With Contact button")
        self.driver.find_element_by_id("tvContacts").click()
        self.appium_worker.bekle_android("tvShare")
        self.logger.log("Clicking Share without selecting any contact")
        self.driver.find_element_by_id("tvShare").click()
        sleep(0.5)
        self.logger.log("Watning message shown", 'green')
        self.appium_worker.screenshot("No_contacts")
        # self.driver.find_element_by_id("etSearch").send_keys("test")
        sleep(1)
        self.logger.log("Selecting a contact")
        self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[1].click()
        self.logger.log("Clicking Share button")
        self.driver.find_element_by_id("tvShare").click()
        sleep(0.5)
        self.appium_worker.screenshot("Invitation_sms")
        sleep(1)
        #self.driver.find_element_by_id("tvFacebook").click()
        ## sleep(6)
        #fl3 = 0
        #while fl3 == 0:
        #    try:
        #        self.driver.find_element_by_class_name("android.widget.ImageView")
        #        fl3 = 1
        #    except NoSuchElementException:
        #        fl3 = 0
        #self.driver.find_element_by_class_name("android.widget.ImageView").click()
        self.appium_worker.bekle_android("tvEmail")
        self.logger.log("Clicking Via Invitation button")
        self.driver.find_element_by_id("tvEmail").click()
        self.appium_worker.bekle_android("custom")
        self.logger.log("Clicking Send without entering e-mail")
        self.driver.find_element_by_id("button1").click()
        self.appium_worker.bekle_android("tvPositive")
        self.appium_worker.screenshot("No_email")
        self.logger.log("Clicking OK")
        self.driver.find_element_by_id("tvPositive").click()
        self.appium_worker.bekle_android("tvEmail")
        self.logger.log("Clicking Via Invitation button")
        self.driver.find_element_by_id("tvEmail").click()
        self.appium_worker.bekle_android("custom")
        self.logger.log("Entering e-mail")
        self.driver.find_element_by_id("custom").send_keys("test@mail.com")
        self.driver.back()
        self.logger.log("Clicking Send")
        self.driver.find_element_by_id("button1").click()
        self.driver.back()
        self.driver.back()
        sleep(1)
        self.driver.back()
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())
