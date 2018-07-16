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


data_products = 0
data_lbs = 0


class PRICES(object):
    def __init__(self, appium_worker):
        self.appium_worker = appium_worker
        self.appium_worker.logger.newFile(self.__class__.__name__)
        self.driver = self.appium_worker.driver
        self.logger = self.appium_worker.logger
        self.logger.log("************************************", 'green')


    def funct_decode(self, the_string):
        strng = codecs.encode(the_string, 'utf-8')
        return strng

    def wait_id(self, button):
        flag = 0
        while flag == 0:
            try:
                self.driver.find_element_by_id(button)
                flag = 1
            except NoSuchElementException:
                sleep(1)
                flag = 0

    def wait_class(self, button):
        flag = 0
        while flag == 0:
            try:
                self.driver.find_element_by_id(button)
                flag = 1
            except NoSuchElementException:
                sleep(1)
                flag = 0

    def decide_product(self, prod_location):
        # global data_products
        # global data_lbs
        # data_products += 1
        flag_f = 0
        aa = prod_location.find_element_by_id("tvText").text
        self.logger.log("\t\t\t" + self.funct_decode(aa))
        bb = self.funct_decode(aa)

        if bb == "Accessories":  # or "Aksesuar":
            flag_f = 1
        if bb == "CD":
            flag_f = 1
        if bb == "Magazine":
            flag_f = 1
        if bb == "Sunglasses":
            flag_f = 1
        if bb == "Belt":
            flag_f = 1
        if bb == "Watch":
            flag_f = 1
        if bb == "Jewelry":
            flag_f = 1
        elif bb == "T-shirt":
            flag_f = 1
        elif bb == "Shoes":
            flag_f = 2
        elif bb == 'Purses':
            flag_f = 2
        elif bb == 'Digital Camera':
            flag_f = 2
        elif bb == 'Cardigan':
            flag_f = 2
        elif bb == 'I-pad':
            flag_f = 2
        elif bb == 'Sweater':
            flag_f = 2
        elif bb == 'Book':
            flag_f = 2
        elif bb == 'Trouser':
            flag_f = 2
        elif bb == 'Sneaker':
            flag_f = 2
        elif bb == 'Boot':
            flag_f = 3
        elif bb == 'Top Boot':
            flag_f = 3

        # data_lbs += flag_f
        return flag_f

    def update_data(self, action, flag_data):
        global data_products
        global data_lbs
        if action == 1:  # "add" or "Add" or "ADD":
            data_lbs += flag_data
            data_products += 1
        # elif action == "remove" or "Remove" or "REMOVE":
        else:
            data_lbs = data_lbs - flag_data
            data_products -= 1
        return data_lbs, data_products

    def screen_calc(self):
        screen_product = int(self.driver.find_element_by_id("tvNumOfPackages").text)
        screen_lbs = int(self.driver.find_element_by_id("tvWeight").text)
        if screen_product == data_products:
            self.logger.log("The number of products in the box is updatet CORRECTLY")
        else:
            self.logger.log("The number of products in the box is NOT updated CORRECTLY")
        if screen_lbs == data_lbs:
            self.logger.log("The weight in the box is updatet CORRECTLY")
        else:
            self.logger.log("The weight in the box is NOT updated CORRECTLY")

    def test(self):
        sleep(0.5)
        self.logger.log("************************************")
        sleep(0.5)
        self.logger.log('Prices test initialized', 'yellow')
        sleep(0.5)
        self.logger.log("************************************", 'green')
        # user1 = 'mail8@mail.com'
        # pass1 = 'testpass'

        user1 = "cihangok@yahoo.com"
        pass1 = "1q2w3e4r"
        promotion_false = "SHIPMENTTEST"
        promotion_correct = "SHIPMENTTEST062016"
        pay_price = 0.0
        flag2 = 0
        flag_err = 0
        nr_products = 0
        lbs = 0

        # PRICES
        self.appium_worker.entrance_android()
        self.driver.find_element_by_id("drawer_indicator").click()
        sleep(1)
        self.logger.log("Scrolling down")

        element2 = self.driver.find_element_by_class_name("android.widget.RelativeLayout")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -1000, 100).perform()
        touch_actions.perform()
        sleep(1)
        self.logger.log("Clicking Prices")
        self.driver.find_elements_by_class_name("android.widget.LinearLayout")[9].click()
        self.wait_id("ivBox")
        nr_products = self.driver.find_element_by_id("tvNumOfPackages").text
        self.logger.log("Number of products is: " + str(nr_products))
        lbs = self.driver.find_element_by_id("tvWeight").text
        self.logger.log("Weight in lbs is: " + str(lbs))

        m = self.driver.find_elements_by_id("rlRoot")[0]
        m1 = m.find_element_by_id("tvText").text

        self.logger.log("*********************************")
        self.logger.log("Selecting item")
        m = self.driver.find_elements_by_id("rlRoot")[0]
        m.click()
        self.logger.log("Item selected is : ")
        flag_data = self.decide_product(m)
        self.logger.log("Weight of the added product is : " + str(flag_data))
        data_lbs, data_products = self.update_data(1, flag_data)
        self.logger.log("Updated lbs is " + str(data_lbs) + " and number of products is " + str(data_products))
        self.screen_calc()

        self.logger.log("*********************************")
        self.logger.log("Selecting item")
        m1 = self.driver.find_elements_by_id("rlRoot")[3]
        m1.click()
        self.logger.log("Item selected is : ")
        flag_data = self.decide_product(self.driver.find_elements_by_id("rlRoot")[3])
        self.logger.log("Weight of the added product is : " + str(flag_data))
        data_lbs, data_products = self.update_data(1, flag_data)
        self.logger.log("Updated lbs is " + str(data_lbs) + " and number of products is " + str(data_products))
        self.screen_calc()

        self.logger.log("*********************************")
        self.logger.log("Selecting item to remove")
        m1 = self.driver.find_elements_by_id("rlRoot")[3]
        m1.find_element_by_id("ivDecrease").click()
        self.logger.log("Item selected is : ")
        flag_data = self.decide_product(self.driver.find_elements_by_id("rlRoot")[3])
        self.logger.log("Weight of the removed product is : " + str(flag_data))
        data_lbs, data_products = self.update_data(0, flag_data)
        self.logger.log("Updated lbs is " + str(data_lbs) + " and number of products is " + str(data_products))
        self.screen_calc()

        self.logger.log("Scrolling right")
        element2 = self.driver.find_element_by_class_name("android.widget.HorizontalScrollView")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, -830, 0, 100).perform()
        touch_actions.perform()
        sleep(1)

        self.logger.log("*********************************")
        self.logger.log("Selecting item")
        m = self.driver.find_elements_by_id("rlRoot")[0]
        m.click()
        self.logger.log("Item selected is : ")
        flag_data = self.decide_product(m)
        self.logger.log("Weight of the added product is : " + str(flag_data))
        data_lbs, data_products = self.update_data(1, flag_data)
        self.logger.log("Updated lbs is " + str(data_lbs) + " and number of products is " + str(data_products))
        self.screen_calc()

        self.logger.log("*********************************")
        self.logger.log("Selecting item")
        m1 = self.driver.find_elements_by_id("rlRoot")[3]
        m1.click()
        self.logger.log("Item selected is : ")
        flag_data = self.decide_product(self.driver.find_elements_by_id("rlRoot")[3])
        self.logger.log("Weight of the added product is : " + str(flag_data))
        data_lbs, data_products = self.update_data(1, flag_data)
        self.logger.log("Updated lbs is " + str(data_lbs) + " and number of products is " + str(data_products))
        self.screen_calc()

        self.logger.log("Scrolling right")
        element2 = self.driver.find_element_by_class_name("android.widget.HorizontalScrollView")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, -830, 0, 100).perform()
        touch_actions.perform()
        sleep(1)

        self.logger.log("*********************************")
        self.logger.log("Selecting item")
        m = self.driver.find_elements_by_id("rlRoot")[1]
        m.click()
        self.logger.log("Item selected is : ")
        flag_data = self.decide_product(m)
        self.logger.log("Weight of the added product is : " + str(flag_data))
        data_lbs, data_products = self.update_data(1, flag_data)
        self.logger.log("Updated lbs is " + str(data_lbs) + " and number of products is " + str(data_products))
        self.screen_calc()

        self.logger.log("*********************************")
        self.logger.log("Selecting item")
        m1 = self.driver.find_elements_by_id("rlRoot")[2]
        m1.click()
        self.logger.log("Item selected is : ")
        flag_data = self.decide_product(self.driver.find_elements_by_id("rlRoot")[2])
        self.logger.log("Weight of the added product is : " + str(flag_data))
        data_lbs, data_products = self.update_data(1, flag_data)
        self.logger.log("Updated lbs is " + str(data_lbs) + " and number of products is " + str(data_products))
        self.screen_calc()

        self.logger.log("*********************************")
        self.logger.log("Selecting item")
        m1 = self.driver.find_elements_by_id("rlRoot")[3]
        m1.click()
        self.logger.log("Item selected is : ")
        flag_data = self.decide_product(self.driver.find_elements_by_id("rlRoot")[3])
        self.logger.log("Weight of the added product is : " + str(flag_data))
        data_lbs, data_products = self.update_data(1, flag_data)
        self.logger.log("Updated lbs is " + str(data_lbs) + " and number of products is " + str(data_products))
        self.screen_calc()

        self.logger.log("*********************************")
        self.logger.log("Selecting item to remove")
        m1 = self.driver.find_elements_by_id("rlRoot")[2]
        m1.find_element_by_id("ivDecrease").click()
        self.logger.log("Item selected is : ")
        flag_data = self.decide_product(self.driver.find_elements_by_id("rlRoot")[2])
        self.logger.log("Weight of the added product is : " + str(flag_data))
        data_lbs, data_products = self.update_data(0, flag_data)
        self.logger.log("Updated lbs is " + str(data_lbs) + " and number of products is " + str(data_products))
        self.screen_calc()

        self.logger.log("***********************************")
        p1 = self.driver.find_element_by_id("tvAICost").text
        p2 = self.driver.find_element_by_id("tvUpsCost").text
        p3 = self.driver.find_element_by_id("tvFedexCost").text
        self.logger.log("Price of Amerikadaniste is " + p1)
        sleep(1)
        self.logger.log("Price of Ups is: " + p2)
        sleep(1)
        self.logger.log("Price of FEDEX is: " + p3)
        sleep(1)

        self.logger.log("**********************************")
        self.logger.log("Scrolling down to read the information")
        element2 = self.driver.find_element_by_class_name("android.widget.HorizontalScrollView")
        touch_actions = TouchActions(self.driver)
        touch_actions.flick_element(element2, 0, -1600, 100).perform()
        sleep(2)
        # touch_actions.perform()
        sleep(3)
        self.logger.log("Scrolling Up")
        flag = 0
        while flag == 0:
            try:
                self.driver.find_element_by_id("tvSupport")
                flag = 1
            except NoSuchElementException:
                flag = 0
            if flag == 1:
                self.logger.log("Clicking Support button")
                self.driver.find_element_by_id("tvSupport").click()
                sleep(3)
                self.driver.back()
                self.driver.back()
                self.logger.log("TEST FINISHED", "green", 1, 2, self.appium_worker.logger.getFileName())

            if flag == 0:
                element2 = self.driver.find_element_by_class_name("android.widget.ScrollView")
                touch_actions = TouchActions(self.driver)
                touch_actions.flick_element(element2, 0, 1000, 100).perform()


            if flag_err == 0:
                self.logger.log("Test FINISHED without errors \n")
            else:
                self.logger.log("Test FINISHED with  %d errors \n" % flag_err)