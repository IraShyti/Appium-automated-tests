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


class INBOX(object):
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
        count_sec = 0
        promotion_false = "SHIPMENTTEST"
        promotion_correct = "SHIPMENTTEST062016"
        sleep(0.5)
        self.logger.log("************************************")
        sleep(1)
        self.logger.log('Order Inbox test initialized', 'yellow')
        sleep(0.5)
        self.logger.log("**************************")


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
        #self.logger.log("Clicking Waiting")
        self.logger.log("Clicking Inbox icon")
        self.driver.find_element_by_id("ivSubmenuInbox").click()
        sleep(1)
        #self.logger.log("Clicking Inbox")
        #self.driver.find_element_by_id("llMyInbox").click()
        sleep(2)

        while flag == 0 and count_sec < 4:
            try:
                self.driver.find_element_by_class_name("android.widget.ListView")
                flag = 1
            except NoSuchElementException:
                flag = 0
                count_sec += 1
                sleep(1)
        if count_sec >= 4:
            self.logger.log("There is no package delivered")
            m1 = self.driver.find_element_by_class_name("android.widget.TextView").text
            self.logger.log("Message shown on screen is : \n\t\t" + self.funct_decode(m1))
        else:
            self.logger.log("Choosing one of the orders")
            self.driver.find_elements_by_id("rlWrapper")[0].click()
            try:
                self.driver.find_element_by_id("tvStatus")
                flag = 1
            except NoSuchElementException:
                flag = 0
            if flag == 1:

                if self.driver.find_element_by_id(
                        "tvStatus").text is "Package Has Warning":  # or "Paketinizde Uyar? Var":
                    flag = 0
                if self.driver.find_element_by_id("tvStatus").text is "Paketinizde Uyar? Var":
                    flag = 0
                else:
                    flag = 1
                if flag == 0:
                    self.logger.log("Package has warning!")
                    self.logger.log("Clicking back")
                    self.driver.back()
                else:
                    self.logger.log("Clicking 'SELECT TO SEND' button")
                    self.driver.find_element_by_id("tvSelect").click()
                self.logger.log("Clicking 'SEND SELECTED' button")
                self.driver.find_element_by_id("tvSendSelected").click()
                sleep(1)
                try:
                    self.driver.find_element_by_id("tvPositive")
                    fl1 = 1
                except NoSuchElementException:
                    fl1 = 0
                if fl1 == 1:
                    self.logger.log("warning message for unpayed invoices")
                    self.appium_worker.screenshot("Unpayed_invoices")
                    self.logger.log("Clicking to continue with payment")
                    self.driver.find_element_by_id("tvPositive").click()
                    self.appium_worker.bekle_android("tvPay")

                    flag = 0
                    while flag == 0:

                        self.logger.log("Showing invoices page")
                        m = self.driver.find_elements_by_id("rlRoot")[0]
                        m.find_element_by_id("tvPay").click()

                        self.appium_worker.bekle_android("ivSecure")
                        self.logger.log("Adding card information")
                        self.driver.find_element_by_id("etCardHolderName").send_keys("Test" + "\n")
                        name = self.driver.find_element_by_id("etCardHolderName").text
                        self.logger.log("Name entered : " + self.funct_decode(name))
                        self.driver.find_element_by_id("etCardHolderSurName").send_keys(
                            "Surname" + "\n")
                        surname = self.driver.find_element_by_id("etCardHolderSurName").text
                        self.logger.log("Surname entered : " + self.funct_decode(surname))
                        self.driver.find_element_by_id("etCardNumber").send_keys("4090700214269159")
                        card = self.driver.find_element_by_id("etCardNumber").text
                        self.logger.log("Card number entered : " + self.funct_decode(card))
                        self.driver.find_element_by_id("tvExpireDate").click()
                        self.driver.find_elements_by_id("numberpicker_input")[1].send_keys("2017")
                        self.driver.find_elements_by_id("numberpicker_input")[0].click()
                        element2 = self.driver.find_elements_by_id("numberpicker_input")[1]
                        touch_actions = TouchActions(self.driver)
                        touch_actions.flick_element(element2, 0, -200, 100).perform()
                        touch_actions.perform()
                        self.driver.find_element_by_id("btnOk").click()
                        expire = self.driver.find_element_by_id("tvExpireDate").text
                        self.logger.log("Expiring date of card : " + self.funct_decode(expire))
                        self.driver.find_element_by_id("etCCV").send_keys(494)
                        ccv = self.driver.find_element_by_id("etCCV").text
                        self.logger.log("CCV of the card : " + self.funct_decode(ccv))
                        self.logger.log("Clicking 'COMPLETE' button")
                        self.driver.find_element_by_id("tvOK").click()
                        sleep(7)
                        try:
                            self.driver.find_elements_by_id("rlRoot")[0].find_element_by_id("tvPay")
                            flag = 0
                        except NoSuchElementException:
                            flag = 1

                    self.logger.log("Choosing one of the orders")
                    self.driver.find_elements_by_id("rlWrapper")[0].click()
                    try:
                        self.driver.find_element_by_id("tvStatus")
                        flag = 1
                    except NoSuchElementException:
                        flag = 0
                    if flag == 1:
                        if self.driver.find_element_by_id(
                                "tvStatus").text is "Package Has Warning":  # or "Paketinizde Uyar? Var":
                            flag = 0
                        if self.driver.find_element_by_id("tvStatus").text is "Paketinizde Uyar? Var":
                            flag = 0
                        else:
                            flag = 1
                        if flag == 0:
                            self.logger.log("Package has warning!")
                            self.logger.log("Clicking back")
                            self.driver.back()
                        else:
                            self.logger.log("Clicking 'SELECT TO SEND' button")
                            self.driver.find_element_by_id("tvSelect").click()
                        self.logger.log("Clicking 'SEND SELECTED' button")
                        self.driver.find_element_by_id("tvSendSelected").click()
                        sleep(1)

                if fl1 == 0:

                    try:
                        self.driver.find_elements_by_id("ivBox")
                        flag = 1
                    except NoSuchElementException:
                        flag = 0
                    if flag == 0:
                        self.logger.log("There are packages that have harms")
                        self.appium_worker.screenshot("Harm_package")
                        txt = self.driver.find_element_by_id("tvMessage").text
                        self.logger.log("Message : \n\t" + self.funct_decode(txt))
                        self.driver.find_elements_by_id("tvPositive")
                    if flag == 1:
                        flag = 0
                        while flag == 0:
                            try:
                                self.driver.find_element_by_id("ivBox")
                                flag = 1
                            except NoSuchElementException:
                                sleep(1)
                                flag = 0
                        self.logger.log("*************************")
                        self.logger.log("Order Details : ")
                        m1 = self.driver.find_element_by_id("tvNumOfPackages").text
                        m2 = self.driver.find_element_by_id("tvWeight").text
                        m3 = self.driver.find_element_by_id("etReceiverName").text
                        m4 = self.driver.find_element_by_id("tvAmountToPay").text
                        self.logger.log("Number of pasckages: " + str(m1))
                        self.logger.log("Weight in lbd : " + str(m2))
                        self.logger.log("Receiver's name : " + self.funct_decode(m3))
                        self.logger.log("Amount to be payed : " + m4)
                        prc = m4[1:3]
                        prc += ".0"
                        pay_price = float(prc)
                        calc_price = 22.0 + int(m2) * 6
                        self.logger.log("Price calculated from formula is : $:" + str(calc_price))
                        if calc_price == pay_price:
                            self.logger.log("Price for payment is calculated correctly")
                        else:
                            self.logger.log("Price for payment is NOT calculated correctly")
                            self.logger.log("Price shown is " + str(pay_price) + "but is should be " + str(
                                calc_price))
                        m1 = self.driver.find_element_by_id("tvPhoneNumber").text
                        self.logger.log("Number : " + str(m1))
                        self.logger.log("Clicking phone number to change")
                        self.driver.find_element_by_id("iv2").click()
                        sleep(1)
                        self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[
                            1].click()
                        # self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[0].click()
                        sleep(2)
                        m1 = self.driver.find_element_by_id("tvPhoneNumber").text
                        self.logger.log("New Number : " + str(m1))
                        # self.driver.back()

                        m1 = self.driver.find_element_by_id("tvAddress").text
                        m2 = self.driver.find_element_by_id("tvAddressDetail").text
                        self.logger.log("Address : \n " + self.funct_decode(
                            m1) + "\nDetails : " + self.funct_decode(m2))

                        # sleep(1)
                        # self.logger.log("Clicking to change address")
                        # self.driver.find_element_by_id("rlAddress").click()
                        # try:
                        #    self.driver.find_element_by_id("tvPositive")
                        #    fl1 = 1
                        # except NoSuchElementException:
                        #    fl1 = 0
                        # if fl1 == 1:
                        #    flag = 0
                        #    while flag == 0:
                        #        print "AA"
                        #        #self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[1].click()
                        #        try:
                        #            self.driver.find_element_by_id("ivBox")
                        #            flag = 1
                        #        except NoSuchElementException:
                        #            sleep(0.5)
                        #            flag = 0
                        #    # self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[3].click()
                        #    self.logger.log("Warning for changing default address")
                        #    self.screenshot("Address_warning")
                        #    #self.driver.find_element_by_id("tvNegative").click()
                        #    sleep(1)
                        #    try:
                        #        self.driver.find_element_by_id("tvPositive")
                        #        flag = 1
                        #    except NoSuchElementException:
                        #        flag = 0
                        #    if flag == 1:
                        #        self.driver.find_element_by_id("tvNegative").click()
                        #        sleep(1)
                        #    else:
                        #        self.logger.log("Message was expected")
                        #        sleep(2)
                        #
                        # if fl1 == 0:
                        #    self.driver.back()

                        # m1 = self.driver.find_element_by_id("tvAddress").text
                        # m2 = self.driver.find_element_by_id("tvAddressDetail").text
                        # self.logger.log("Address : \n \t" + self.funct_decode(m1) + "\n\tDetails : " + self.funct_decode(m2))
                        # self.logger.log("Adding false promotion code " + promotion_false)
                        sleep(0.5)
                        self.logger.log("Adding promotion code '" + promotion_false + "'")
                        self.driver.find_element_by_id("etPromotionCode").send_keys(promotion_false)
                        sleep(1)
                        self.driver.back()
                        try:
                            self.driver.find_element_by_id("tvSendSelected")
                            flag = 0
                        except NoSuchElementException:
                            flag = 1
                        if flag == 0:
                            self.driver.find_element_by_id("tvSendSelected").click()
                            sleep(1)
                        self.logger.log("Clicking 'APPLY' button")
                        self.driver.find_element_by_id("tvApplyPromotionCode").click()
                        sleep(1)
                        self.appium_worker.bekle_android("tvPositive")
                        try:
                            self.driver.find_element_by_id("tvPositive")
                            print "AAAA"
                            flag = 0
                        except NoSuchElementException:
                            "BBBB"
                            flag = 1
                        if flag == 0:
                            self.logger.log("Promotion code error")
                            self.appium_worker.screenshot("Promotion_code_error")
                            self.driver.find_element_by_id("tvPositive").click()
                            fl1 = 0
                            while fl1 == 0:
                                self.driver.find_element_by_id("etPromotionCode").clear()
                                self.logger.log("Adding promotion code '" + promotion_correct + "'")
                                self.driver.find_element_by_id("etPromotionCode").send_keys(
                                    promotion_correct)
                                self.driver.back()
                                self.logger.log("Clicking 'APPLY' button")
                                self.driver.find_element_by_id("tvApplyPromotionCode").click()
                                sleep(3)

                                try:
                                    self.driver.find_element_by_id("tvPositive")
                                    self.logger.log("promotion code error")
                                    self.appium_worker.screenshot("Promotion_code_error")
                                    fla2 = 0
                                    fl1 = 0
                                except NoSuchElementException:
                                    fla2 = 1
                                    fl1 = 1
                                if fla2 == 0:
                                    self.driver.find_element_by_id("tvPositive").click()

                            m1 = self.driver.find_element_by_id("tvApplyPromotionCode").text
                            m2 = self.driver.find_element_by_id("tvAmountToPay").text
                            self.logger.log("Promotion price : " + m1)
                            self.logger.log("NEW price to be payed : " + m2)
                            prc = m2[1:3] + "." + m2[4:]
                            pay1 = float(prc)
                            prom = m1[2:3] + "." + m1[4:]
                            if pay1 == (pay_price - float(prom)):
                                self.logger.log("Promotion amount subtracted correctly")
                            else:
                                self.logger.log("Promotion price NOT subtracted correctly")

                        sleep(1)
                        try:
                            self.driver.find_element_by_id("tvUseAward")
                            flag = 1
                        except NoSuchElementException:
                            flag = 0
                        if flag == 1:
                            self.logger.log("Use award points")
                            self.driver.find_element_by_id("tvUseAward").click()
                        self.logger.log("*********************")
                        self.logger.log("Clicking button to show information of Cekull")
                        self.driver.find_element_by_id("ivCekulInfo").click()
                        try:
                            self.driver.find_element_by_id("tvPositive")
                            flag = 1
                        except NoSuchElementException:
                            flag = 0
                        if flag == 1:
                            self.logger.log("Information of Cekull")
                            sleep(1)
                            m1 = self.driver.find_element_by_id("tvMessage").text
                            self.logger.log("'INFORMATION' message : \n\t" + self.funct_decode(m1))
                            self.driver.find_element_by_id("tvPositive").click()
                        else:
                            self.logger.log("Message was expected")
                        try:
                            self.driver.find_element_by_id("tvAddNote")
                            flag = 1
                        except NoSuchElementException:
                            flag = 0
                        if flag == 1:
                            self.logger.log("Clicking Add Note button")
                            self.logger.log("Adding note")
                            self.driver.find_element_by_id("tvAddNote").click()
                            self.driver.find_element_by_id("etNote").send_keys("Test note")
                            self.driver.back()
                            self.logger.log("Clicking Save button")
                            self.driver.find_element_by_id("tvSave").click()
                            sleep(1)
                            m1 = self.driver.find_element_by_id("tvNote").text
                            self.logger.log("Message shown on NOTE : \n\t" + self.funct_decode(m1))
                            self.logger.log("Scrolling down list")
                            element2 = self.driver.find_element_by_id("llRoot")
                            touch_actions = TouchActions(self.driver)
                            touch_actions.flick_element(element2, 0, -200, 100).perform()
                            touch_actions.perform()
                            sleep(1)
                            self.logger.log("Scrolled")
                            self.logger.log("Clicking 'CONTINUE' button")
                            self.driver.find_element_by_id("tvContinue").click()
                            sleep(1)
                            m1 = self.driver.find_element_by_id("tvInboxHeader").text
                            self.logger.log("Page : " + self.funct_decode(m1))
                            self.logger.log("Adding card information")
                            self.driver.find_element_by_id("etCardHolderName").send_keys("Test" + "\n")
                            name = self.driver.find_element_by_id("etCardHolderName").text
                            self.logger.log("Name entered : " + self.funct_decode(name))
                            self.driver.find_element_by_id("etCardHolderSurName").send_keys(
                                "Surname" + "\n")
                            surname = self.driver.find_element_by_id("etCardHolderSurName").text
                            self.logger.log("Surname entered : " + self.funct_decode(surname))
                            self.driver.find_element_by_id("etCardNumber").send_keys("4090700214269159")
                            card = self.driver.find_element_by_id("etCardNumber").text
                            self.logger.log("Card number entered : " + self.funct_decode(card))
                            self.driver.find_element_by_id("tvExpireDate").click()
                            self.driver.find_elements_by_id("numberpicker_input")[1].send_keys("2017")
                            self.driver.find_elements_by_id("numberpicker_input")[0].click()
                            element2 = self.driver.find_elements_by_id("numberpicker_input")[1]
                            touch_actions = TouchActions(self.driver)
                            touch_actions.flick_element(element2, 0, -200, 100).perform()
                            touch_actions.perform()
                            self.driver.find_element_by_id("btnOk").click()
                            expire = self.driver.find_element_by_id("tvExpireDate").text
                            self.logger.log("Expiring date of card : " + self.funct_decode(expire))
                            self.driver.find_element_by_id("etCCV").send_keys(494)
                            ccv = self.driver.find_element_by_id("etCCV").text
                            self.logger.log("CCV of the card : " + self.funct_decode(ccv))
                            self.logger.log("Clicking 'COMPLETE' button")
                            self.driver.find_element_by_id("tvOK").click()
                            sleep(3)
                            self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())
                            #self.driver.find_element_by_id("tvOK").click()
                            #sleep(3)
                            #flag2 = 0
                            #while flag2 == 0:
                            #    try:
                            #        self.driver.find_element_by_id("tvPositive")
                            #        flag = 1
                            #        flag2 = 1
                            #    except NoSuchElementException:
                            #        sleep(1)
                            #        flag2 = 0
                            #        flag = 0
                            #    if flag == 1:
                            #        self.logger.log("Error with the credit card")
                            #        self.appium_worker.screenshot("Credit_card_error")
                            #        self.driver.find_element_by_id("tvPositive").click()
                            #        self.driver.back()
#
                            #    else:
                            #        self.logger.log("no error")
                            #        self.driver.find_element_by_id("tvOK").click()
                            #        sleep(3)
                            #        self.appium_worker.screenshot("Order_completed")

        self.appium_worker.home_menu()
        #self.driver.back()
        #self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())