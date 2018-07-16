from Utilities.logger import Logger
from appium import webdriver
import unittest
import random
import IOS
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
from sources.device_source import DeviceSource


user1 = ""
pass1 = ""

class AppiumWorker(object):

    '''
    def __init__(self, device, start, logger=None):
        self.device = device
        self.start = start
        self.logger = logger
        print str(self.start)
        self.logger.newFile(self.__class__.__name__)
        print str(self.start)
        if int(self.start) == 1:
            self.setUp()
    '''

    def __init__(self):
        self.device = None
        self.logger = None

    def setDevice(self, device_name):
        print 'start of set device'
        if not self.device or self.device['device_name'] != device_name:
            self.device = DeviceSource().get_device(device_name)
            self.setUp()
            print 'ktu'
        print 'end of set device'

    def setLogger(self, logger):
        self.logger = logger
        self.logger.newFile(self.__class__.__name__)

    def screenshot(self, name):
        screenshot_name = str(self.screenshot_count) + "_" + name + ".png"
        self.driver.save_screenshot(self.screenshot_dir + "/" + screenshot_name)
        sleep(0.5)
        self.logger.log(screenshot_name, 'green', 2)
        self.screenshot_count += 1


    def setUp(self):

        print 'setUp : ' + self.device['platform_name']
        print 'setUp : ' + self.device['platform_version']
        print 'setUp : ' + self.device['device_name']

        desired_caps = {}
        desired_caps['platformName'] = self.device['platform_name']
        desired_caps['platformVersion'] = self.device['platform_version']
        desired_caps['deviceName'] = self.device['device_name']
        print 'setUp : 1'
        desired_caps['app'] = os.path.abspath(r'/Users/macbookpro/Desktop/App-debug.apk')

        print 'setUp : 2'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print 'setUp : 3'
        self.screenshot_dir = os.environ.get('TESTDROID_SCREENSHOTS') or os.getcwd() + "/static/Screenshots"
        print 'setUp : 4'
        self.screenshot_count = 1

        #print 'setUp : 1'
        #desired_caps['app'] = IOS.path.abspath(r'/Users/macbookpro/Desktop/AmerikadanIste-IPA/AI1/Amerikadaniste.app')

    def bekle_android(self, item):
        fl1 = 0
        while fl1 == 0:
            try:
                self.driver.find_element_by_id(item)
                fl1 = 1
            except NoSuchElementException:
                self.logger.log("Wait")
                fl1 = 1

    def bekle_ios(self, item):
        fl1 = 0
        while fl1 == 0:
            try:
                self.driver.find_element_by_xpath(item)
                fl1 = 1
            except NoSuchElementException:
                self.logger.log("Wait")
                fl1 = 1

    def home_menu(self):
        flag = 0
        try:
            self.driver.find_element_by_id("ivSubmenuHome")
            flag = 1
        except NoSuchElementException:
            self.driver.back()
            try:
                self.driver.find_element_by_id("ivSubmenuHome")
                flag = 1
            except NoSuchElementException:
                self.driver.back()
                try:
                    self.driver.find_element_by_id("ivSubmenuHome")
                    flag = 1
                except NoSuchElementException:
                    self.driver.back()
        if flag == 1:
            self.driver.find_element_by_id("ivSubmenuHome").click()

    def entrance_android(self):
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
            self.logger.log("Clicking Log In")
            self.driver.find_element_by_id("tvLogin").click()
            self.logger.log("Entering email " + user1)
            self.driver.find_element_by_id("etEmail").send_keys(user1)
            sleep(1)
            flag1 = 0
            while flag1 == 0:
                m1 = self.driver.find_element_by_id("etEmail").text
                if str(m1) == user1:
                    sleep(0.5)
                    flag1 = 1
                else:
                    flag1 = 0
                    self.logger.log("Mail was entered incorrect")
                    self.driver.find_element_by_id("etEmail").clear()
                    self.logger.log("Entering email " + str(user1), 'blue')
                    self.driver.find_element_by_id("etEmail").send_keys(user1)
            self.logger.log("Entering Password " + pass1)
            self.driver.find_element_by_id("etPassword").send_keys(pass1)
            self.driver.find_element_by_id("btnSend").click()
            #
        if flag == 2:
            self.logger.log("Clicking Log In")
            self.driver.find_element_by_id("tvLogin").click()
            self.logger.log("Entering email " + user1)
            self.driver.find_element_by_id("etEmail").send_keys(user1)
            flag1 = 0
            while flag1 == 0:
                if str(m1) == user1:
                    sleep(0.5)
                    flag1 = 1
                else:
                    flag1 = 0
                    self.logger.log("Mail was entered incorrect")
                    self.driver.find_element_by_id("etEmail").clear()
                    self.logger.log("Entering email " + str(user1), 'blue')
                    self.driver.find_element_by_id("etEmail").send_keys(user1)
            self.logger.log("Entering Password " + pass1)
            self.driver.find_element_by_id("etPassword").send_keys(pass1)
            self.logger.log("********************************s")
            self.driver.find_element_by_id("btnSend").click()

        if flag == 3:
            sleep(1)

    def entrance_ios(self):
        user1 = 'cihangok@yahoo.com'
        pass1 = '1q2w3e4r'
        flag = 0
        while flag == 0:
            try:
                self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1][@name='Skip']")
                flag = 1
            except NoSuchElementException:
                try:
                    self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1][@name='Login']")
                    flag = 2
                except NoSuchElementException:
                    try:
                        self.driver.find_element_by_xpath(
                            "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1][@name='leftMenu']")
                        flag = 3
                    except NoSuchElementException:
                        sleep(1)
                        self.logger.log("Wait")
                        flag = 0
        if flag == 1:
            self.logger.log('Pressing pass')
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
            self.logger.log("Clicking Log In")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
            self.logger.log("Entering email " + user1)
            self.driver.find_element_by_id("etEmail").send_keys(user1)
            sleep(1)
            flag1 = 0
            while flag1 == 0:
                m1 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").text
                if str(m1) == user1:
                    sleep(0.5)
                    flag1 = 1
                else:
                    flag1 = 0
                    self.logger.log("Mail was entered incorrect")
                    self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").clear()
                    self.logger.log("Entering email " + str(user1))
                    self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys(
                        user1)
            self.logger.log("Entering Password " + pass1)
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]").send_keys(pass1)
            self.logger.log("Clicking LogIn")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
            #
        if flag == 2:
            self.logger.log("Clicking Log In")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
            self.logger.log("Entering email " + user1)
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys(user1)
            flag1 = 0
            while flag1 == 0:
                m1 = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").text
                if str(m1) == user1:
                    sleep(0.5)
                    flag1 = 1
                else:
                    flag1 = 0
                    self.logger.log("Mail was entered incorrect")
                    self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").clear()
                    self.logger.log("Entering email " + str(user1))
                    self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys(
                        user1)
            self.logger.log("Entering Password " + pass1)
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]").send_keys(pass1)
            self.logger.log("Clicking LogIn")
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()

        if flag == 3:
            sleep(1)

    def submenu(self):
        el1 = self.driver.find_elements_by_class_name("android.widget.LinearLayout")[1]
        el2 = el1.find_element_by_id("tvDrawerListItem")
        if el2.text == "Prices" or el2.text == "What To Buy?" or el2.text == "About Us" or el2.text == "Campaigns" or el2.text == "Ne Alsam?" or el2.text == "Kurumsal":
            drawer = 2
        else:
            drawer = 1
        return drawer

    def tearDown(self):
        self.driver.quit()

    def main_page(self):
        pass
