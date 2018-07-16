from Tests.appium_worker import AppiumWorker
from Utilities.logger import Logger

from Tests.appium_worker import webdriver
import unittest
import random
import os
import time
from time import sleep
import codecs
import datetime
import uuid
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException



class SIGNUP(object):
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
        self.logger.log('Sign Up initialized', 'yellow')
        sleep(0.5)
        self.logger.log("************************************", 'green')
        mail_var = uuid.uuid4().hex
        name = 'name'
        surname = 'surname'
        email = 'mail3@mail.com'
        newmail = "mail_" + mail_var + "@mail.com"
        pass1 = 'abcd'
        pass2 = "testpass"
        flag_err = 0

        flag = 0
        while flag == 0:
            try:
                self.driver.find_element_by_id('tvPass')
                flag = 1
            except NoSuchElementException:
                try:
                    self.driver.find_element_by_id("tvLogin")
                    flag = 2
                except NoSuchElementException:
                    try:
                        self.driver.find_element_by_id("drawer_indicator")
                        flag = 3
                    except NoSuchElementException:
                        sleep(1)
                        self.logger.log("Wait")
                        flag = 0
        if flag == 1:
            self.logger.log("Pressing Pass")
            self.driver.find_element_by_id('tvPass').click()

        if flag == 2:
            sleep(1)

        if flag == 3:
            sleep(1)

        self.logger.log("Pressing Sign Up")
        self.driver.find_element_by_id('tvSingUp').click()
        self.logger.log("Inserting name '" + name + "'")
        self.driver.find_element_by_id('etName').send_keys(name)
        self.logger.log("Inserting surname '" + surname + "'")
        self.driver.find_element_by_id('etSurname').send_keys(surname)
        self.logger.log("Inserting email '" + email + "'")
        self.driver.find_element_by_id('etEmail').send_keys(email)
        self.logger.log("Inserting password '" + pass1 + "'")

        self.driver.find_element_by_id('etPassword').send_keys(pass1)
        self.driver.back()
        self.logger.log("Clicking button to create account")
        self.logger.log("ERROR is expected")
        self.driver.find_element_by_id('btnCreateAccount').click()
        try:
            self.driver.find_element_by_id("tvPositive")
            flag = 1
        except NoSuchElementException:
            flag = 0

        if flag == 1:
            self.logger.log("Error for unchecked agreement shown")
            self.appium_worker.screenshot("Error_unchecked_agreement")
            self.driver.find_element_by_id("tvPositive").click()
            sleep(1)
        else:
            self.logger.log("Error of agreement was expected")
            self.logger.log("Quit driver. Test Unsuccessful")
            self.driver.quit()
            self.logger.log("Selecting agreement button")
        self.driver.find_element_by_id("tvReadAgreement").click()
        sleep(1)
        self.logger.log("Clicking OK")
        flag = 0
        while flag == 0:
            try:
                self.driver.find_element_by_id("tvPositive")
                flag = 1
            except NoSuchElementException:
                sleep(1)
                flag = 0
        self.driver.find_element_by_id("tvPositive").click()
        self.logger.log("Clicking to read agreement")
        self.driver.find_element_by_id("cbReadAgreement").click()
        self.logger.log("Entering phone number '" + "5544984171'")
        self.driver.find_element_by_id('etPhoneNumber').send_keys("5544984171")
        self.driver.back()
        self.logger.log("Clicking button to create account")
        self.driver.find_element_by_id('btnCreateAccount').click()
        self.logger.log("ERROR for sign-up field is expected")
        try:
            self.driver.find_element_by_id("tvPositive")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            self.logger.log("Error for sign up fields is shown")
            self.appium_worker.screenshot("Error_fields")
            self.driver.find_element_by_id("tvPositive").click()

        else:
            self.logger.log("Error was expected")
            flag_err += 1
            self.logger.log("Quit driver. Test Unsuccessful")
            self.driver.quit()
        self.logger.log("Adding new password '" + pass2 + "'")
        self.driver.find_element_by_id("etPassword").clear()
        self.driver.find_element_by_id("etPassword").clear()
        self.driver.find_element_by_id('etPassword').send_keys(pass2)
        self.driver.back()
        self.logger.log("Adding birthday")
        self.driver.find_element_by_id("rlBirthday").click()
        self.driver.find_element_by_id("date_picker_year").click()
        self.logger.log("Clicking DONE")
        self.driver.find_element_by_id("done").click()
        self.logger.log("Clicking button to create account")
        self.driver.find_element_by_id('btnCreateAccount').click()
        flag = 0
        while flag == 0:
            try:
                self.driver.find_element_by_id("tvPositive")
                flag = 0
            except NoSuchElementException:
                flag = 1
            if flag == 0:
                self.logger.log("Email is used")
                self.appium_worker.screenshot("Used_email")
                self.logger.log("Clicking OK")
                self.driver.find_element_by_id("tvPositive").click()
                self.logger.log("Change email to '" + newmail + "'")
                self.driver.find_element_by_id("etEmail").clear()
                self.driver.find_element_by_id("etEmail").clear()
                self.driver.find_element_by_id("etEmail").send_keys(newmail)
                self.driver.back()
                self.logger.log("Clicking button to create account")
                self.driver.find_element_by_id('btnCreateAccount').click()
                sleep(3)
            if flag == 1:
                self.logger.log("Email not used")
                sleep(2)
        self.logger.log("******************************")
        sleep(0.5)
        self.appium_worker.bekle_android("ivRegAmountInfo")
        self.logger.log("Showing page '" + codecs.encode(self.driver.find_element_by_id("tvHeader").text, 'utf-8') + "'")
        self.logger.log("Clicking Detailed Information")
        self.driver.find_element_by_id("tvDetailedInfo").click()
        self.logger.log("Showing detailed information")
        sleep(1)
        self.logger.log("Clicking OK")
        self.driver.find_element_by_id("tvPositive").click()
        self.logger.log("Clicking to show registration payment information")
        self.driver.find_element_by_id("ivRegAmountInfo").click()
        try:
            self.driver.find_element_by_id("tvPositive")
            flag = 1
        except NoSuchElementException:
            flag = 0
            self.logger.log("Registration fee information was expected to be shown")
            self.logger.log("ERROR!!")
            flag_err += 1
        if flag == 1:
            sleep(2)
            self.driver.find_element_by_id("tvPositive").click()
        self.logger.log("Clicking to show membership type info")
        self.driver.find_element_by_id("ivMembershipType").click()
        try:
            self.driver.find_element_by_id("tvPositive")
            flag = 1
        except NoSuchElementException:
            flag = 0
            self.logger.log("Membership type information was expected")
            self.logger.log("ERROR!!")
            flag_err += 1
        if flag == 1:
            sleep(2)
            self.driver.find_element_by_id("tvPositive").click()
        self.logger.log("Change membership type")
        self.driver.find_element_by_id("llYearly").click()
        self.logger.log("Inserting promotion code '" + "REGISTERTEST'")
        self.driver.find_element_by_id("etPromotionCode").send_keys('REGISTERTEST')
        self.driver.back()
        self.logger.log("Clicking Aply")
        self.driver.find_element_by_id("tvApplyPromotionCode").click()
        sleep(1)
        try:
            self.driver.find_element_by_id("tvPositive")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            self.logger.log("Promotion code incorrect")
            self.appium_worker.screenshot("Promotion_code_incorrect")
            self.logger.log("Clicking Ok")
            self.driver.find_element_by_id("tvPositive").click()
            self.logger.log("Entering new promotion code '" + "REGISTERTEST062016'")
            self.driver.find_element_by_id("etPromotionCode").clear()
            self.driver.find_element_by_id("etPromotionCode").clear()
            self.driver.find_element_by_id("etPromotionCode").send_keys('REGISTERTEST062016')
            self.driver.back()
            self.logger.log("Clicking Apply button")
            self.driver.find_element_by_id("tvApplyPromotionCode").click()
        else:
            self.logger.log("Promotion code correct")
            # check for a correct promotion code
        self.logger.log("Clicking to enter payment information")
        self.driver.find_element_by_id("tvPaymentInfo").click()
        self.logger.log("Scrolling down")
        element2 = self.driver.find_element_by_class_name("android.widget.RelativeLayout")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -700, 100).perform()
        touch_actions.perform()
        sleep(3)
        # self.driver.find_element_by_id("etCardHolderName").send_keys("cardholder")
        self.logger.log("Adding card holder surname '" + "Surname'")

        self.driver.find_element_by_id("etCardHolderSurName").send_keys("Surname" + "\n")
        surname = self.driver.find_element_by_id("etCardHolderSurName").text
        self.logger.log("Surname entered : " + str(surname))
        self.driver.find_element_by_id("etCardNumber").send_keys("4090700214269159")
        card = self.driver.find_element_by_id("etCardNumber").text
        self.logger.log("Card number entered : " + str(card))
        self.driver.find_element_by_id("tvExpireDate").click()
        self.driver.find_elements_by_id("numberpicker_input")[1].send_keys("2017")
        self.driver.find_elements_by_id("numberpicker_input")[0].click()
        element2 = self.driver.find_elements_by_id("numberpicker_input")[1]
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -200, 100).perform()
        touch_actions.perform()
        self.driver.find_element_by_id("btnOk").click()
        expire = self.driver.find_element_by_id("tvExpireDate").text
        self.logger.log("Expiring date of card : " + str(expire))

        self.driver.find_element_by_id("ivCCV").click()
        try:
            self.driver.find_element_by_id("tvPositive")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            self.logger.log("Information of CCV")
            self.driver.find_element_by_id("tvPositive").click()
        else:
            self.logger.log("CCV information was expected to be shown")
            self.logger.log("ERROR!!")
            flag_err += 1
        self.logger.log("Adding CCV number '494'")
        self.driver.find_element_by_id("etCCV").send_keys("494")
        self.driver.back()
        self.logger.log("Clicking finalize")
        self.driver.find_element_by_id("btnFinalize").click()
        sleep(0.5)
        self.logger.log("Error for missing card information is shown")
        self.appium_worker.screenshot("Missing_card_info_1")
        try:
            self.driver.find_element_by_id("etCardHolderName")
            flag = 1
        except NoSuchElementException:
            flag = 0
        if flag == 1:
            self.logger.log("Adding card holder name 'Test'")
            self.driver.find_element_by_id("etCardHolderName").send_keys("Test")
            self.driver.back()
            self.logger.log("Clicking finalize")
            self.driver.find_element_by_id("btnFinalize").click()
        else:
            self.logger.log("Error message for payment information was expected")
            self.logger.log("ERROR!!")
            flag_err += 1

        #flag = 0
        #while flag == 0:
        #    self.logger.log("Wait")
        #    try:
        #        self.driver.find_element_by_id("tvPositive")
        #        flag = 1
        #    except NoSuchElementException:
        #        flag = 0
#
        #if flag == 1:
        #    self.logger.log("Connection time out")
        #    self.driver.find_element_by_id("tvPositive").click()
        #    self.driver.back()
        #else:
        #    flag1 = 0
        #    while flag1 == 0:
        #        try:
        #            self.driver.find_element_by_id("tvUserDetail")
        #            flag1 = 1
        #        except NoSuchElementException:
        #            sleep(1)
        #            flag1 = 0
        #    self.appium_worker.screenshot("Registration_completed")
        #    m1 = self.driver.find_element_by_id("tvUserDetail").text
        #    self.logger.log("User details: " + m1)
        #    self.driver.find_element_by_id("tvStartShopping").click()
#
        #    self.logger.log("Clicking HOME button")
        #    self.driver.find_element_by_id("ivSubmenuHome").click()
        #    sleep(1)
        #    self.logger.log("Clicking left sub-menu")
        #    self.driver.find_element_by_id("drawer_indicator").click()
        #    self.logger.log("Scrolling down")
        #    element2 = self.driver.find_element_by_class_name("android.widget.RelativeLayout")
        #    touch_actions = TouchActions(self.driver)
        #    touch_actions.flick_element(element2, 0, -1000, 100).perform()
        #    touch_actions.perform()
        #    sleep(1)
        #    self.logger.log("Clicking Exit")
        #    self.driver.find_elements_by_class_name("android.widget.LinearLayout")[19].click()
        #    sleep(2)
        #self.driver.back()
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())
    
        if flag_err == 0:
            self.logger.log("Test finished without errors \n")
        else:
            self.logger.log("Test finished with  %d errors \n" % flag_err)