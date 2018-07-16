from Tests.Android.order import Order
from Tests.Android.About_us import ABOUTUS
from Tests.Android.Settings import SETTINGS
from Tests.Android.Prices import PRICES
from Tests.Android.Log_in import LOGIN
from Tests.Android.Support import SUPPORT
from Tests.Android.HowItWorks import HOWITWORKS
from Tests.Android.Share import SHARE
from Tests.Android.MyAwards import MYAWARDS
from Tests.Android.WhatToBuy import WHATTOBUY
from Tests.Android.Contact import CONTACT
from Tests.Android.Sign_up import SIGNUP
from Tests.Android.Profile import PROFILE
from Tests.Android.Notifications import NOTIFICATIONS
from Tests.Android.BuyForMe import BUYFORME
from Tests.Android.Order_deliver import DELIVERED
from Tests.Android.Order_tracking import TRACKING
from Tests.Android.Order_waiting import WAITING
from Tests.Android.Order_new import NEWORDER
from Tests.Android.Order_inbox import INBOX
from Tests.IOS.About_us import ABOUTUSiOS
from Tests.IOS.BuyForMe import BUYFORMEIOS
from Tests.IOS.Campaigns import CAMPAIGNSIOS
from Tests.IOS.Contact import CONTACTIOS
from Tests.IOS.DeliveredPackages import DELIVEREDPACKAGESIOS
from Tests.IOS.HowItWorks import HOWITWORKSIOS
from Tests.IOS.Log_in import TestLogInIOS
from Tests.IOS.Mailbox import MAILBOXIOS
from Tests.IOS.Notifications import NOTIFICATIONSIOS
from Tests.IOS.Order_new import NEWORDERIOS
from Tests.IOS.PackageTracking import PACKAGETRACKINGIOS
from Tests.IOS.Prices import PRICESIOS
from Tests.IOS.Profile import TestMyProfileIOS
from Tests.IOS.Settings import TestSettingsIOS
from Tests.IOS.Share import SHAREIOS
from Tests.IOS.Sign_up import SIGNUPIOS
from Tests.IOS.Support import SUPPORTIOS
from Tests.IOS.WaitingPackages import WAITINGPACKAGESIOS
from Tests.IOS.WhatToBuy import WHATTOBUYIOS

from Utilities.logger import Logger
from Tests.appium_worker import AppiumWorker
from sources.device_source import DeviceSource


class TestSource(object):

    def __init__(self, appium_handler, appium_worker, logger):

        self.appium_handler = appium_handler
        self.appium_worker = appium_worker
        self.logger = logger
        self.logger.test_source = self
        print 'TestSource __init __  : after worker init'

    def send_log(self, log, log_type, status, download):
        self.appium_handler.send_log(log, log_type, status, download)

    def test(self, item):

        print 'TestSource test'

        try:
            item.test()
        except:
            self.appium_worker.main_page()
        finally:
            self.appium_worker.main_page()

    def test_login(self):
        log_in = LOGIN(self.appium_worker)
        self.test(log_in)

    def test_aboutus(self):
        test = ABOUTUS(self.appium_worker)
        self.test(test)

    def test_contact(self):
        test = CONTACT(self.appium_worker)
        self.test(test)

    def test_howitworks(self):
        test = HOWITWORKS(self.appium_worker)
        self.test(test)

    def test_myawards(self):
        test = MYAWARDS(self.appium_worker)
        self.test(test)

    def test_prices(self):
        test = PRICES(self.appium_worker)
        self.test(test)

    def test_settings(self):
        test = SETTINGS(self.appium_worker)
        self.test(test)

    def test_share(self):
        test = SHARE(self.appium_worker)
        self.test(test)

    def test_support(self):
        test = SUPPORT(self.appium_worker)
        self.test(test)

    def test_profile(self):
        test = PROFILE(self.appium_worker)
        self.test(test)

    def test_notifications(self):
        test = NOTIFICATIONS(self.appium_worker)
        self.test(test)

    def test_whattobuy(self):
        test = WHATTOBUY(self.appium_worker)
        self.test(test)

    def test_order(self):
        test = Order(self.appium_worker)
        self.test(test)

    def test_signup(self):
        test = SIGNUP(self.appium_worker)
        self.test(test)

    def test_bfm(self):
        test = BUYFORME(self.appium_worker)
        self.test(test)

    def test_delivered(self):
        test = DELIVERED(self.appium_worker)
        self.test(test)

    def test_tracking(self):
        test = TRACKING(self.appium_worker)
        self.test(test)

    def test_waiting(self):
        test = WAITING(self.appium_worker)
        self.test(test)

    def test_neworder(self):
        test = NEWORDER(self.appium_worker)
        self.test(test)

    def test_inbox(self):
        test = INBOX(self.appium_worker)
        self.test(test)

    # IOS
    def test_aboutus_ios(self):
        test = ABOUTUSiOS(self.appium_worker)
        self.test(test)

    def test_bfm_ios(self):
        test = BUYFORMEIOS(self.appium_worker)
        self.test(test)

    def test_campaigns_ios(self):
        test = CAMPAIGNSIOS(self.appium_worker)
        self.test(test)

    def test_contact_ios(self):
        test = CONTACTIOS(self.appium_worker)
        self.test(test)

    def test_delivered_ios(self):
        test = DELIVEREDPACKAGESIOS(self.appium_worker)
        self.test(test)

    def test_howitworks_ios(self):
        test = HOWITWORKSIOS(self.appium_worker)
        self.test(test)

    def test_login_ios(self):
        log_in = TestLogInIOS(self.appium_worker)
        self.test(log_in)

    def test_mailbox_ios(self):
        test = MAILBOXIOS(self.appium_worker)
        self.test(test)

    def test_notifications_ios(self):
        test = NOTIFICATIONSIOS(self.appium_worker)
        self.test(test)

    def test_order_ios(self):
        test = NEWORDERIOS(self.appium_worker)
        self.test(test)

    def test_tracking_ios(self):
        test = PACKAGETRACKINGIOS(self.appium_worker)
        self.test(test)

    def test_prices_ios(self):
        test = PRICESIOS(self.appium_worker)
        self.test(test)

    def test_profile_ios(self):
        test = TestMyProfileIOS(self.appium_worker)
        self.test(test)

    def test_settings_ios(self):
        test = TestSettingsIOS(self.appium_worker)
        self.test(test)

    def test_share_ios(self):
        test = SHAREIOS(self.appium_worker)
        self.test(test)

    def test_signup_ios(self):
        test = SIGNUPIOS(self.appium_worker)
        self.test(test)

    def test_support_ios(self):
        test = SUPPORTIOS(self.appium_worker)
        self.test(test)

    def test_waiting_ios(self):
        test = WAITINGPACKAGESIOS(self.appium_worker)
        self.test(test)

    def test_whattobuy_ios(self):
        test = WHATTOBUYIOS(self.appium_worker)
        self.test(test)

    def test_all(self):

        self.test_login()
        self.test_support()
        self.test_profile()
        self.test_notifications()
        self.test_aboutus()
        self.test_howitworks()
        self.test_share()
        self.test_myawards()
        self.test_whattobuy()
        self.test_settings()
        self.test_prices()
        self.test_contact()
        self.test_order()
        self.test_bfm()
        self.test_signup()
        self.test_delivered()
        self.test_tracking()
        self.test_waiting()
        self.test_neworder()
        self.test_inbox()
        # ios
        self.test_aboutus_ios()
        self.test_bfm_ios()
        self.test_campaigns_ios()
        self.test_contact_ios()
        self.test_delivered_ios()
        self.test_howitworks_ios()
        self.test_login_ios()
        self.test_mailbox_ios()
        self.test_notifications_ios()
        self.test_order_ios()
        self.test_tracking_ios()
        self.test_prices_ios()
        self.test_profile_ios()
        self.test_settings_ios()
        self.test_share_ios()
        self.test_signup_ios()
        self.test_support_ios()
        self.test_waiting_ios()
        self.test_whattobuy_ios()

