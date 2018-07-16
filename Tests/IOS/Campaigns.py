"""
UI iOS tests for AmerikadanIste app.
Ira Shyti 28-09-2016
"""
from appium import webdriver
import datetime
from codecs import decode
from datetime import datetime
from Tests.appium_worker import AppiumWorker
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


class CAMPAIGNSIOS(object):
    log_flag = 0

    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("********************************")

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

        sleep(3)
        self.logger.log("Clicking Campaigns")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[9]").click()
        sleep(2)
        self.logger.log("Showing all Campaigns")
        self.logger.log("Clicking Following")
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]").click()
        sleep(1)
        try:
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/"
                                      "UIACollectionCell[1]")
            flag1 = 1
        except NoSuchElementException:
            flag1 = 0
        if flag1 == 0:
            self.logger.log("You are not following any campaign")
            self.logger.log("Clicking All")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
            try:
                self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/"
                                                  "UIACollectionCell[1]")
                flag2 = 1
            except NoSuchElementException:
                flag2 = 0
            if flag2 == 0:
                self.logger.log("There are no campaigns")
            else:
                self.logger.log("There are campaigns you can follow")
                self.logger.log("Campaign name : " + self.driver.find_element_by_xpath(" //UIAApplication[1]/UIAWindow[1]/"
                                                                           "UIACollectionView[1]/UIACollectionCell[1]/"
                                                                           "UIAStaticText[1]").text)
                self.logger.log("Price : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIACollectionView"
                                                                   "[1]/UIACollectionCell[1]/UIAStaticText[2]").text)
        if flag1 == 1:
            self.logger.log("Selecting a campaign")
            self.logger.log("Name : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/"
                                                              "UIACollectionCell[1]/UIAStaticText[1]").text)
            self.logger.log("Price : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/"
                                                               "UIACollectionCell[1]/UIAStaticText[2]").text)
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/"
                                              "UIACollectionCell[1]").click()
            self.logger.log("Text : " + self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAStaticText[1]").text)
            self.logger.log("Clicking to unfollow it")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAImage[3]").click()
            self.logger.log("Clicking back")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]").click()
            sleep(1)
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())


