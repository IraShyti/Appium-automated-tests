from Tests.appium_worker import AppiumWorker
from Utilities.logger import Logger
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


class Order(object):
    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("********************************")


    #def funct_decode(self, the_string):
    #    return codecs.encode(the_string, 'utf-8')

    def funct_decode(self, the_string):
        strng = codecs.encode(the_string, 'utf-8')
        return strng

    def test(self):
        sleep(0.5)
        self.logger.log("************************************")
        sleep(0.5)
        self.logger.log('Order initialized', 'yellow')
        sleep(0.5)
        self.logger.log("********************************")
        user1 = "cihangok@yahoo.com"
        pass1 = "1q2w3e4r"
        promotion_false = "SHIPMENTTEST"
        promotion_correct = "SHIPMENTTEST062016"
        pay_price = 0.0
        flag2 = 0
        flag_err = 0

        self.appium_worker.entrance_android()
        self.appium_worker.bekle_android("drawer_indicator")
        self.logger.log("Clicking left sub menu")
        self.driver.find_element_by_id("drawer_indicator").click()
        sleep(1)
        drawer = self.appium_worker.submenu()
        if drawer == 2:
            self.logger.log("Scrolling up the screen")
            element2 = self.driver.find_element_by_class_name("android.widget.ListView")
            touch_actions = TouchActions(self.driver)
            touch_actions.flick_element(element2, 0, 1000, 100).perform()
            touch_actions.perform()
            sleep(1)
        self.logger.log("Clicking 'NEW ORDER' button")
        self.driver.find_element_by_class_name("android.widget.LinearLayout").click()
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
                    self.logger.log("Clicking 'WAITING' button")
                    self.driver.find_element_by_id("tvWaitingOrders").click()
                    self.appium_worker.bekle_android("llWaiting")
                    self.logger.log("Selecting one package")
                    # m1 = self.driver.find_element_by_id("lvAddress")
                    # m1.find_elements_by_class_name("android.widget.RelativeLayout")[1].click()
                    self.appium_worker.bekle_android("list")

                    m = self.driver.find_element_by_id("list")
                    m.find_elements_by_id("rlRoot")[1].click()
                    flag = 0
                    while flag == 0:
                        try:
                            self.driver.find_element_by_id("ivBox")
                            flag = 1
                        except NoSuchElementException:
                            # mm = m1.find_elements_by_class_name("android.widget.RelativeLayout")[1]
                            # mm.find_element_by_id("llMiddle").click()
                            self.driver.find_elements_by_id("rlRoot")[1].click()
                            flag = 0
                    try:
                        self.driver.find_element_by_id("ivAddTrackingCode")
                        flag = 1
                    except NoSuchElementException:
                        flag = 0
                    if flag == 1:
                        self.driver.find_element_by_id("tvAddTrackingCode").click()
                        self.logger.log("Adding tracking code '1234'")
                        self.driver.find_element_by_id("etTrackingCode").send_keys("1234")
                        self.logger.log("Selecting US Carries as 'UPS'")
                        self.driver.find_element_by_id("ivUPS").click()
                        self.appium_worker.screenshot("Tracking_code")
                        self.logger.log("Clicking 'OK' button")
                        self.driver.find_element_by_id("tvOK").click()
                    else:
                        sleep(1)
                    sleep(1)
                    m1 = self.driver.find_element_by_id("etContent").text
                    m2 = self.driver.find_element_by_id("tvCreationDate").text
                    m3 = self.driver.find_element_by_class_name("android.widget.TextView").text
                    self.logger.log("*************************")
                    self.logger.log("Content: " + self.funct_decode(m1))
                    self.logger.log("Creation date: " + self.funct_decode(m2))
                    self.logger.log("Package state: " + self.funct_decode(m3))
                    self.logger.log("Clicking 'WAITING PACKAGES' button")
                    self.driver.find_element_by_id("tvWaitingPackages").click()
                    sleep(2)

                    self.logger.log("Selecting package to delete")
                    elem = self.driver.find_elements_by_id("rlWrapper")[2]
                    elem.find_element_by_id("ivIcon").click()
                    try:
                        self.driver.find_element_by_id("tvPositive")
                        flag = 1
                    except NoSuchElementException:
                        self.logger.log("Warning for deleting order was expected")
                        self.logger.log("ERROR!")
                        flag_err += 1
                    if flag == 1:
                        self.appium_worker.screenshot("deleting_order")
                        self.driver.find_element_by_id("tvPositive").click()

                        # TRACKING
                    self.logger.log("Clicking 'TRACKING' button")
                    self.driver.find_element_by_id("llTracking").click()
                    fl2 = 0
                    count_sec = 0
                    while fl2 == 0 and count_sec < 4:
                        try:
                            self.driver.find_elements_by_id("rlRoot")[1].find_element_by_id("vCheck")
                            fl2 = 1
                        except NoSuchElementException:
                            self.logger.log("Wait")
                            sleep(1)
                            count_sec += 1
                            fl2 = 0
                    if count_sec >= 4:
                        self.logger.log("There are no packages you can track")
                        mm = self.driver.find_element_by_id("inbox_content_frame")
                        m1 = mm.find_element_by_class_name("android.widget.TextView").text
                        self.logger.log("The message shown on screen is : \n\t\t" + self.funct_decode(m1))
                    else:
                        self.logger.log("Opening one of the orders")
                        self.driver.find_elements_by_id("rlRoot")[1].find_element_by_id("vCheck")
                        try:
                            self.driver.find_element_by_id("tvBottom")
                            flag = 1
                        except NoSuchElementException:
                            flag = 0
                        if flag == 1:
                            m1 = self.driver.find_element_by_id("tvContent").text
                            m2 = self.driver.find_element_by_id("tvEntryDate").text
                            m3 = self.driver.find_element_by_id("tvDepartureDate").text
                            #m4 = self.driver.find_element_by_id("tvTrackingCode").text
                            m5 = self.driver.find_element_by_id("tvSender").text
                            m6 = self.driver.find_element_by_id("tvPackageCode").text
                            self.logger.log("*************************")
                            self.logger.log("Content: " + self.funct_decode(m1))
                            self.logger.log("Entry date: " + self.funct_decode(m2))
                            self.logger.log("Departure date: " + self.funct_decode(m3))
                            #self.logger.log("Tacking code " + self.funct_decode(m4))
                            self.logger.log("Sender: " + self.funct_decode(m5))
                            self.logger.log("Code: " + self.funct_decode(m6))
                            if self.driver.find_element_by_id("tvBottom").text is "OK" or self.driver.find_element_by_id("tvBottom").text is "Tamam":
                                flag = 1
                            elif self.driver.find_element_by_id("tvBottom").text is "DETAILED TRACKING":
                                flag = 0
                            if flag == 1:
                                #self.driver.find_element_by_id("tvBottom").click()
                                self.logger.log("Clicking BACK")
                                self.driver.back()
                            elif flag == 0:
                                # self.driver.find_element_by_id("tvBottom").click()
                                # sleep(3)
                                # self.driver.back()
                                self.logger.log("Clicking BACK")
                                self.driver.back()
                        self.logger.log("Scrolling down list")
                        element2 = self.driver.find_element_by_id("rlList")
                        touch_actions = TouchActions(self.driver)
                        touch_actions.flick_element(element2, 0, -200, 100).perform()
                        touch_actions.perform()
                        sleep(1)
                        self.logger.log("Scrolled")
                        self.logger.log("Opening one of the orders")
                        self.driver.find_elements_by_id("rlWrapper")[3].click()
                        try:
                            self.driver.find_element_by_id("tvBottom")
                            flag = 1
                        except NoSuchElementException:
                            flag = 0
                        if flag == 1:
                            m1 = self.driver.find_element_by_id("tvContent").text
                            m2 = self.driver.find_element_by_id("tvEntryDate").text
                            m3 = self.driver.find_element_by_id("tvDepartureDate").text
                            #m4 = self.driver.find_element_by_id("tvTrackingCode").text
                            m5 = self.driver.find_element_by_id("tvSender").text
                            m6 = self.driver.find_element_by_id("tvPackageCode").text
                            self.logger.log("*************************")
                            self.logger.log("Content: " + self.funct_decode(m1))
                            self.logger.log("Entry date: " + self.funct_decode(m2))
                            self.logger.log("Departure date: " + self.funct_decode(m3))
                            # self.logger.log("Tacking code " + str(m4))
                            self.logger.log("Sender: " + self.funct_decode(m5))
                            self.logger.log("Code: " + self.funct_decode(m6))
                            #if self.driver.find_element_by_id("tvBottom").text is "OK":
                            #    flag = 1
                            #elif self.driver.find_element_by_id("tvBottom").text is "DETAILED TRACKING":
                            #    flag = 0
                            #if flag == 1:
                            #    self.driver.find_element_by_id("tvBottom").click()
                            #elif flag == 0:
                            #    sleep(3)
                            #    self.logger.log("Clicking BACK")
                            #    self.driver.back()
                            #    self.driver.back()
                            #    self.driver.back()
                        self.driver.back()
                        self.logger.log("Scrolling down list")
                        element2 = self.driver.find_element_by_id("rlList")
                        touch_actions = TouchActions(self.driver)
                        touch_actions.flick_element(element2, 0, -600, 100).perform()
                        touch_actions.perform()
                        sleep(1)
                        self.logger.log("Scrolled")
                        self.logger.log("Opening one of the orders")
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
                            #m4 = self.driver.find_element_by_id("tvTrackingCode").text
                            m5 = self.driver.find_element_by_id("tvSender").text
                            m6 = self.driver.find_element_by_id("tvPackageCode").text
                            self.logger.log("*************************")
                            self.logger.log("Content: " + self.funct_decode(m1))
                            self.logger.log("Entry date: " + self.funct_decode(m2))
                            self.logger.log("Departure date: " + self.funct_decode(m3))
                            #self.logger.log("Tacking code " + self.funct_decode(m4))
                            self.logger.log("Sender: " + self.funct_decode(m5))
                            self.logger.log("Code: " + self.funct_decode(m6))
                            if self.driver.find_element_by_id("tvBottom").text == "OK" or "TAMAM":
                                flag = 1
                            if self.driver.find_element_by_id("tvBottom").text == "DETAILED TRACKING":
                                flag = 0
                            if flag == 1:
                                self.driver.find_element_by_id("tvBottom").click()
                            # elif flag == 0:
                            else:
                                # self.driver.find_element_by_id("tvBottom").click()
                                sleep(3)
                                self.logger.log("Clicking BACK")
                                # self.driver.back()
                                self.driver.back()

                                # ORDER DELIVERED
                    self.logger.log("****************************")
                    self.logger.log("Clicking 'DELIVERED' button")
                    self.driver.find_element_by_id("llDelivered").click()
                    flag = 0
                    count_sec = 0
                    while flag == 0 and count_sec < 4:
                        try:
                            self.driver.find_element_by_class_name("android.widget.ListView")
                            flag = 1
                        except NoSuchElementException:
                            flag = 0
                            count_sec += 1
                            sleep(2)
                    # sleep(5)
                    if count_sec >= 4:
                        self.logger.log("There is no package delivered")
                        m1 = self.driver.find_element_by_class_name("android.widget.TextView").text
                        self.logger.log("Message shown on screen is : \n\t\t" + self.funct_decode(m1))
                    else:
                        element2 = self.driver.find_element_by_class_name("android.widget.ListView")
                        touch_actions = TouchActions(self.driver)
                        touch_actions.flick_element(element2, 0, -500, 100).perform()
                        touch_actions.perform()
                        self.logger.log("Choosing a package")
                        self.driver.find_elements_by_id("rlRoot")[3].click()
                        p1 = self.driver.find_element_by_id("tvContent")
                        p2 = self.driver.find_element_by_id("tvEntryDate")
                        p3 = self.driver.find_element_by_id("tvDepartureDate")
                        p4 = self.driver.find_element_by_id("tvDeliveryDate")
                        self.logger.log("*************************")
                        self.logger.log("Content: " + self.funct_decode(p1.text))
                        self.logger.log("Entry date: " + p2.text)
                        self.logger.log("Departure date: " + p3.text)
                        self.logger.log("Delivered date: " + p4.text)
                        self.appium_worker.screenshot("package")
                        self.driver.find_element_by_id("tvBottom").click()
                        element2 = self.driver.find_element_by_class_name("android.widget.ListView")
                        touch_actions = TouchActions(self.driver)
                        touch_actions.flick_element(element2, 0, -500, 100).perform()
                        touch_actions.perform()
                        self.logger.log("Choosing a package")
                        self.driver.find_elements_by_id("rlRoot")[5].click()
                        p1 = self.driver.find_element_by_id("tvContent")
                        p2 = self.driver.find_element_by_id("tvEntryDate")
                        p3 = self.driver.find_element_by_id("tvDepartureDate")
                        p4 = self.driver.find_element_by_id("tvDeliveryDate")
                        self.logger.log("*************************")
                        self.logger.log("Content: " + self.funct_decode(p1.text))
                        self.logger.log("Entry date: " + p2.text)
                        self.logger.log("Departure date: " + p3.text)
                        self.logger.log("Delivered date: " + p4.text)
                        self.driver.find_element_by_id("tvBottom").click()

                        # POSTA KUTUM
                    self.logger.log("*************************")
                    self.logger.log("Opening order inbox")
                    self.driver.find_element_by_id("llMyInbox").click()
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
                                        self.logger.log("TEST FINISHED", "green", 1, 2,
                                                        self.appium_worker.logger.getFileName())
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

                    self.driver.back()
                    self.driver.back()
                    self.appium_worker.home_menu()
                   # self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())

            else:
                self.logger.log("ERROR was not expected")
                flag_err += 1

        if flag_err == 0:
            self.logger.log("Test finished without errors \n")
        else:
            self.logger.log("Test finished with  %d errors \n" % flag_err)
