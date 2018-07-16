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


class BUYFORME(object):
    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("********************************")


    def funct_decode(self, the_string):
        strng = codecs.encode(the_string, 'utf-8')
        return strng

    def test(self):
        sleep(0.5)
        self.logger.log("************************************")
        sleep(0.5)
        self.logger.log('Buy For Me initialized', 'yellow')
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
        # CHANGE LANGUAGE
        # flag = 0
        # while flag == 0:
        #    try:
        #        self.driver.find_element_by_id("ivSubmenuProfile")
        #        flag = 1
        #    except NoSuchElementException:
        #        sleep(1)
        #        flag = 0
        # self.logger.log("Clicking 'PROFILE' button")
        # self.driver.find_element_by_id("ivSubmenuProfile").click()
        # self.logger.log("Clicking 'SETTINGS' button")
        # self.driver.find_element_by_id("ivSettings").click()
        # self.logger.log("Clicking 'LANGUAGE' to change language of application")
        # self.driver.find_element_by_id("tvLanguage").click()
        # sleep(2)
        # m1 = self.driver.find_element_by_id("tvLanguage").text
        # self.logger.log("Language changed to : " + str(m1))
        # self.logger.log("Going back")
        # self.driver.back()
        # self.logger.log("Clicking 'HOME' button")
        # self.driver.find_element_by_id("ivSubmenuHome").click()

        # BUY FOR ME
        self.driver.find_element_by_id("drawer_indicator").click()
        self.driver.find_elements_by_class_name("android.widget.LinearLayout")[16].click()
        flag = 0
        while flag == 0:
            try:
                self.driver.find_elements_by_id("tvFinalizeOrder")
                flag = 1
            except NoSuchElementException:
                print "wait"
                sleep(1)
                flag = 0

        try:
            self.driver.find_element_by_id("ivAdd")
            flag2 = 1
        except NoSuchElementException:
            sleep(0.5)
        try:
            self.driver.find_element_by_class_name("android.widget.ScrollView")
            flag2 = 2
        except NoSuchElementException:
            sleep(0.5)
        if flag2 == 2:
            self.logger.log("Scrolling down to read 'Buy For Me' details")
            element2 = self.driver.find_element_by_class_name("android.widget.ScrollView")
            touch_actions = TouchActions(self.driver)
            touch_actions.flick_element(element2, 0, -500, 100).perform()
            touch_actions.perform()
            sleep(1)
        self.logger.log("Clicking 'PREVIOUS ORDERS' button")
        self.driver.find_element_by_id("rlPrevious").click()
        self.appium_worker.bekle_android("tvWhatToBuy")
        self.logger.log("Opening one of the orders")
        self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[1].click()
        self.appium_worker.bekle_android("tvSiteAmount")
        self.logger.log("**********************************")
        m1 = self.driver.find_element_by_id("tvSiteAmount").text
        m2 = self.driver.find_element_by_id("tvCollectedAmount").text
        m3 = self.driver.find_element_by_id("tvOrderDate").text
        m4 = self.driver.find_element_by_id("tvPurchaseDate").text
        self.logger.log("Amount of shopping : " + self.funct_decode(str(m1)))
        self.logger.log("Amount that will be collected : " + self.funct_decode(str(m2)))
        self.logger.log("Date of order : " + self.funct_decode(str(m3)))
        self.logger.log("Date bought : " + self.funct_decode(str(m4)))
        self.logger.log("************************************")
        self.logger.log("Going back")
        self.driver.back()
        self.driver.find_element_by_id("rlNewBFM").click()
        flag = 0
        # while flag == 0:
        #    m1 = self.driver.find_element_by_id("tvHeader").text
        #    print self.funct_decode(m1)
        #    if str(self.funct_decode(m1)) is "BUY FOR ME":
        #        print "AAA"
        #        flag = 1
        #    else:
        #        sleep(1)
        #        flag = 0
        # self.appium_worker.bekle_android("tvBfmDetailHeader")
        flag = 0
        while flag == 0:
            try:
                self.driver.find_element_by_id("tvAddFirstProduct")
                flag = 1
            except NoSuchElementException:
                try:
                    self.driver.find_element_by_id("tvFinalizeOrder")
                    flag = 1
                except NoSuchElementException:
                    sleep(1)
                    flag = 0

        print "aa"
        try:
            self.driver.find_element_by_id("tvAddFirstProduct")
            self.logger.log("No orders were placed on the list")
            flag1 = 1
        except NoSuchElementException:
            try:
                self.driver.find_element_by_id("tvFinalizeOrder")
                self.logger.log("Order already created")
                flag1 = 2
            except NoSuchElementException:
                sleep(0.5)
        if flag1 == 1:
            self.logger.log("Clicking to crate a order")
            self.driver.find_element_by_id("tvAddFirstProduct").click()
            self.logger.log("Entering the URL of the product")
            self.driver.find_element_by_id("etProductUrl").send_keys("link")
            self.driver.back()
            self.logger.log("Entering the details of the product")
            self.driver.find_element_by_id("etProductProperties").send_keys("clothes")
            self.driver.back()
            self.logger.log("Selecting the delivery type")
            self.driver.find_element_by_id("tvSpinner").click()
            self.driver.find_elements_by_id("tvSpinner")[1].click()
            sleep(0.5)
            m1 = self.driver.find_element_by_id("tvSpinner").text
            self.logger.log("Type of delivery selected is : " + self.funct_decode(m1))
            self.logger.log("Clicking ADD")
            self.driver.find_element_by_id("tvAdd").click()
            sleep(3)
            try:
                self.driver.find_element_by_id("tvAdd")
                flag = 1
            except NoSuchElementException:
                sleep(1)
                flag = 0
            if flag == 1:
                self.driver.find_element_by_id("tvAdd").click()
            self.appium_worker.bekle_android("tvFinalizeOrder")
            self.logger.log("Clicking to finalize order")
            self.driver.find_element_by_id("tvFinalizeOrder").click()
            # self.logger.log("Trying to add product without adding link")
            # self.logger.log("Clicking ADD")
            # self.driver.find_element_by_id("tvAdd").click()
            # sleep(0.5)
            # self.appium_worker.screenshot("Empty_link_field")
            # self.driver.find_element_by_id("tvAddFirstProduct").click()
            # self.logger.log("Adding link field 'link'")
            # self.driver.find_element_by_id("etProductUrl").send_keys("link")
            # self.driver.back()
            # self.logger.log("Trying to add product without adding details")
            # self.logger.log("Clicking ADD")
            # self.driver.find_element_by_id("tvAdd").click()
            # sleep(0.5)
            # self.appium_worker.screenshot("Empty_details_field")
            # self.driver.find_element_by_id("tvAddFirstProduct").click()
            # self.logger.log("Adding product details 'clothes'")
            # self.logger.log("Adding link field 'link'")
            # self.driver.find_element_by_id("etProductUrl").send_keys("link")
            # self.driver.find_element_by_id("etProductProperties").send_keys("clothes")
            # self.driver.back()
            # self.logger.log("Clicking ADD")
            # self.driver.find_element_by_id("tvAdd").click()
        if flag1 == 2:
            self.logger.log("Clicking to Complete Order")
            self.driver.find_element_by_id("tvFinalizeOrder").click()
            # count_prod = 0
            # flag = 0
            # elem = self.driver.find_element_by_id("favGrid")
            # while flag == 0:
            #    print count_prod
            #    try:
            #        elem.find_elements_by_class_name("android.widget.LinearLayout")[count_prod]
            #        flag = 0
            #        flag1 = 1
            #    except NoSuchElementException:
            #        sleep(0.5)
            #        flag = 1
            #    if flag1 == 1:
            #        count_prod += 1
            site_amount = 100.0
            app_amount = 0

        self.appium_worker.bekle_android("etSiteAmount")
        self.logger.log("Entering ammount to be paid to the site : " + str(site_amount))
        self.driver.find_element_by_id("etSiteAmount").send_keys("100")
        self.logger.log("Calculating the amount that will be taken")
        self.logger.log("Clicking CALCULATE")
        self.driver.find_element_by_id("tv2").click()
        sleep(2)
        m1 = self.driver.find_element_by_id("tvTotalAmount").text
        self.logger.log("Amount calculated as : " + str(m1))
        m2 = m1[1:4]
        m3 = m1[5:]
        app_amount = float(m2 + "." + m3)
        elem = self.driver.find_element_by_id("favGrid")
        if app_amount > (site_amount * 1.0596) + 15:
            self.logger.log("There are more than 5 products on the BFM list")
            count_prod = 0
            left = app_amount - ((site_amount * 1.0596) + 15)
            left = str(left)
            left = left[0:1]
            aa = int(left)
            count_prod = aa / 3
            count_prod += 4
            try:
                elem.find_elements_by_class_name("android.widget.LinearLayout")[count_prod]
                flag2 = 1
            except NoSuchElementException:
                sleep(0.5)
                flag2 = 0
            if flag2 == 1:
                self.logger.log("Amount calculated correctly")
        elif app_amount == (site_amount * 1.0596) + 15:
            self.logger.log("Amount calculated correctly")
        self.logger.log("Clicking to continue")
        self.driver.find_element_by_id("tvContinue").click()
        sleep(2)
        self.logger.log("Entering card holder name 'Test'")
        self.driver.find_element_by_id("etCardHolderName").send_keys("Test" + "\n")
        self.logger.log("Entering card holder surname 'Surname'")
        self.driver.find_element_by_id("etCardHolderSurName").send_keys("Surname" + "\n")
        self.logger.log("Entering the card number '4090700214269159'")
        self.driver.find_element_by_id("etCardNumber").send_keys("4090700214269159")
        self.logger.log("Selecting expire date")
        self.driver.find_element_by_id("tvExpireDate").click()
        # self.driver.find_elements_by_id("numberpicker_input")[1].send_keys("2017")
        self.driver.find_elements_by_id("numberpicker_input")[0].click()
        element2 = self.driver.find_elements_by_id("numberpicker_input")[1]
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -200, 100).perform()
        touch_actions.perform()
        self.logger.log("Clicking Ok")
        self.driver.find_element_by_id("btnOk").click()
        self.logger.log("Entering CCV number '494'")
        self.driver.find_element_by_id("etCCV").send_keys(494)
        self.driver.back()
        self.driver.find_element_by_id("tvOK").click()
        self.appium_worker.bekle_android("tvConfirmText")
        # sleep(8)
        sleep(1)
        self.appium_worker.screenshot("BFM_Completed")
        self.driver.back()
        self.driver.back()
        self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())


        if flag_err == 0:
            self.logger.log("Test finished without errors \n")
        else:
            self.logger.log("Test finished with  %d errors \n" % flag_err)