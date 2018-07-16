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


class PROFILE(object):
    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("**************************")

    def test(self):
        sleep(0.5)
        self.logger.log("************************************")
        sleep(1)
        self.logger.log('Profile test initialized', 'yellow')
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
        self.logger.log("Clicking to open profile")
        self.driver.find_element_by_id("ivSubmenuProfile").click()
        username = self.driver.find_element_by_id("etUserName").text
        self.logger.log("Username is : " + username)
        birthday = self.driver.find_element_by_id("tvBirthday").text
        self.logger.log("Birthday : " + birthday)
        txt1 = self.driver.find_element_by_id("tvUSAddressLabel").text + \
               " is : " + self.driver.find_element_by_id("tvUSAddress").text
        self.logger.log(self.driver.find_element_by_id("tvUSAddressLabel").text +
            " is : " + self.driver.find_element_by_id("tvUSAddress").text)
        txt2 = self.driver.find_element_by_id("tvEmailLabel").text + "is : " + self.driver.find_element_by_id(
            "tvEmail").text
        self.logger.log(txt2)
        self.logger.log("Clicking button for changing mail address")
        self.driver.find_element_by_id("ivEditEmail").click()
        sleep(1)
        try:
            self.driver.find_element_by_id("button1")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 0:
            self.logger.log("Pop-up message for changing e-mail was expected to be shown")
            self.logger.log("ERROR!!")
            err_flag += 1
        else:
            self.logger.log("Clicking confirm without adding email address")
            self.driver.find_element_by_id("button1").click()
            self.appium_worker.screenshot("No_email_entered")
        self.logger.log("Adding email")
        # self.driver.find_element_by_class_name("android.widget.EditText").send_keys(user1)
        flag = 0
        while flag == 0:
            self.driver.find_element_by_class_name("android.widget.EditText").send_keys(user1)
            if self.driver.find_element_by_class_name("android.widget.EditText").text != user1:
                self.logger.log("Mail is written wrong")
                flag = 0
            else:
                flag = 1
        self.driver.find_element_by_id("button1").click()
        sleep(1)
        self.logger.log("Request for mail change")
        self.appium_worker.screenshot("Mail_change_request")
        self.driver.find_element_by_id("tvPositive").click()
        self.logger.log(self.driver.find_element_by_id("tvPhoneNumbersLabel").text + "is :" + self.driver.find_element_by_id(
            "tvPhoneNumber").text)
        self.logger.log("Clicking to Phone number")
        self.driver.find_element_by_id("rlPhoneNumbers").click()
        sleep(2)
        self.logger.log("Phone details")
        flag = 0
        while flag == 0:
            try:
                self.driver.find_element_by_id("tvAddNewPhoneNumber")
                flag = 1
            except NoSuchElementException:
                flag = 0
        self.logger.log("Adding new number")
        self.driver.find_element_by_id("tvAddNewPhoneNumber").click()
        sleep(1)
        self.logger.log("Saving without adding number")
        self.logger.log("Error expected")
        self.driver.find_element_by_id("tvSave").click()
        try:
            self.driver.find_element_by_id("tvPositive")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            self.logger.log("Error message shown")
            self.appium_worker.screenshot("Number_error")
            self.driver.find_element_by_id("tvPositive").click()
        else:
            self.logger.log("Error not shown")
        self.driver.find_element_by_id("etPhoneNumber").send_keys("05665468732")
        self.driver.back()
        self.logger.log("Setting number as default")
        self.driver.find_element_by_id("cbSetAsDefault").click()
        sleep(2)
        self.driver.back()
        self.driver.back()
        txt4 = self.driver.find_element_by_id("tvTRAddressLabel").text + \
               " is : " + self.driver.find_element_by_id("tvTRAddress").text
        self.logger.log(txt4)
        self.logger.log("Pressing Turkish Address")
        self.driver.find_element_by_id("rlTRAddress").click()
        #self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[1].click()



        # deleting address
        #flag = 0
        #while flag == 0:
        #    self.logger.log("ktu")
        #    adr = self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[1]
        #    touch_actions = TouchActions(self.driver)
        #    touch_actions.long_press(self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[1]).perform()
        #    try:
        #        self.driver.find_element_by_id("select_dialog_listview")
        #        flag = 1
        #    except NoSuchElementException:
        #        flag = 0
        #self.logger.log("Deleting one of the addresses")
        #self.driver.find_element_by_id("select_dialog_listview").click()
        #try:
        #    self.driver.find_element_by_id("tvPositive")
        #    flag = 1
        #except NoSuchElementException:
        #    flag = 0
        #if flag == 0:
        #    self.logger.log("Warning was supposed to be shown")
        #else:
        #    self.logger.log("Warning of deleting address")
        #    self.appium_worker.screenshot("Deleting_address")
        #    self.driver.find_element_by_id("tvPositive").click()
        #    sleep(1)

        self.logger.log("Add new address")
        self.driver.find_element_by_id("tvAddNewAddress").click()
        self.logger.log("Adding address title")
        self.driver.find_element_by_id("etTitle").clear()
        self.driver.find_element_by_id("etTitle").send_keys("work")
        self.driver.back()
        self.driver.find_element_by_id("tvSaveAddress").click()
        try:
            self.driver.find_element_by_id("tvPositive")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            self.appium_worker.screenshot("No_address")
            self.driver.find_element_by_id("tvPositive").click()
        self.logger.log("Entering Open Address")
        self.driver.find_element_by_id("etFullAddress").send_keys("Akatlar")
        self.driver.back()
        self.driver.find_element_by_id("tvSaveAddress").click()
        try:
            self.driver.find_element_by_id("tvPositive")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            self.appium_worker.screenshot("No_ZIP")
            self.logger.log("Clicking Ok")
            self.driver.find_element_by_id("tvPositive").click()
        self.logger.log("Entering ZIP code")
        self.driver.find_element_by_id("etZipCode").send_keys(1000)
        self.driver.back()
        self.logger.log("Selecting District")
        self.driver.find_element_by_id("spinnerDistrict").click()
        self.driver.find_elements_by_id("tvSpinner")[9].click()
        self.logger.log("Selecting Set as default adress")
        self.driver.find_element_by_id("cbSetAsDefaultAddress").click()
        self.logger.log("Clicking to save address")
        self.driver.find_element_by_id("tvSaveAddress").click()
        self.driver.back()
        self.driver.back()
        self.appium_worker.home_menu()
        #self.driver.back()
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())
