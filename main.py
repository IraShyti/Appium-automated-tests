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
from Utilities.logger import Logger
from Tests.Android.Profile import PROFILE
from Tests.Android.BuyForMe import BUYFORME
from Tests.Android.Sign_up import SIGNUP
from Tests.Android.Notifications import NOTIFICATIONS
from Tests.appium_worker import AppiumWorker
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


class Main(object):

    def __init__(self):

        self.logger = Logger()
        self.appium_worker = AppiumWorker(self.logger)

    def test(self, item):

        try:
            item.test()
        except:
            self.appium_worker.main_page()
        finally:
            self.appium_worker.main_page()

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
        self.test_bfm()
        self.test_order()
        self.test_signup()

        self.test_aboutus_ios()
        self.test_bfm_ios()
        self.test_campaigns_ios()
        self.test_contact_ios()
        self.test_delivered_ios()
        self.test_login_ios()
        self.test_mailbox_ios()
        self.test_notifications_ios()
        self.test_order_ios()
        self.test_tracking_ios()
        self.test_prices_ios()
        self.test_profile_ios()
        self.test_settings_ios()
        self.test_share_ios()
        self.test_support_ios()
        self.test_signup_ios()
        self.test_waiting_ios()


    def test_login(self):
        Log_in = LOGIN(self.appium_worker)
        self.test(Log_in)

    def test_support(self):
        Support = SUPPORT(self.appium_worker)
        self.test(Support)

    def test_profile(self):
        Profile = PROFILE(self.appium_worker)
        self.test(Profile)

    def test_notifications(self):
        Notifications = NOTIFICATIONS(self.appium_worker)
        self.test(Notifications)

    def test_aboutus(self):
        About_us = ABOUTUS(self.appium_worker)
        self.test(About_us)

    def test_share(self):
        Share = SHARE(self.appium_worker)
        self.test(Share)

    def test_howitworks(self):
        HowItWorks = HOWITWORKS(self.appium_worker)
        self.test(HowItWorks)

    def test_myawards(self):
        MyAwards = MYAWARDS(self.appium_worker)
        self.test(MyAwards)

    def test_whattobuy(self):
        WhatToBuy = WHATTOBUY(self.appium_worker)
        self.test(WhatToBuy)

    def test_contact(self):
        Contact = CONTACT(self.appium_worker)
        self.test(Contact)

    def test_bfm(self):
        BuyForMe = BUYFORME(self.appium_worker)
        self.test(BuyForMe)

    def test_order(self):
        order = Order(self.appium_worker)
        self.test(order)

    def test_settings(self):
        Settings = SETTINGS(self.appium_worker)
        self.test(Settings)

    def test_prices(self):
        Prices = PRICES(self.appium_worker)
        self.test(Prices)

    def test_signup(self):
        Sign_up = SIGNUP(self.appium_worker)
        self.test(Sign_up)


    # IOS
    def test_login_ios(self):
        Log_in = TestLogInIOS(self.appium_worker)
        self.test(Log_in)

    def test_aboutus_ios(self):
        About_us = ABOUTUSiOS(self.appium_worker)
        self.test(About_us)

    def test_bfm_ios(self):
        BuyForMe = BUYFORMEIOS(self.appium_worker)
        self.test(BuyForMe)

    def test_campaigns_ios(self):
        Campaigns = CAMPAIGNSIOS(self.appium_worker)
        self.test(Campaigns)

    def test_contact_ios(self):
        Contact = CONTACTIOS(self.appium_worker)
        self.test(Contact)

    def test_delivered_ios(self):
        Delivered = DELIVEREDPACKAGESIOS(self.appium_worker)
        self.test(Delivered)

    def test_mailbox_ios(self):
        Mailbox = MAILBOXIOS(self.appium_worker)
        self.test(Mailbox)

    def test_notifications_ios(self):
        Notifications = NOTIFICATIONSIOS(self.appium_worker)
        self.test(Notifications)

    def test_order_ios(self):
        Order = NEWORDERIOS(self.appium_worker)
        self.test(Order)

    def test_tracking_ios(self):
        Tracking = PACKAGETRACKINGIOS(self.appium_worker)
        self.test(Tracking)

    def test_prices_ios(self):
        Prices = PRICESIOS(self.appium_worker)
        self.test(Prices)

    def test_profile_ios(self):
        Profile = TestMyProfileIOS(self.appium_worker)
        self.test(Profile)

    def test_settings_ios(self):
        Settings = TestSettingsIOS(self.appium_worker)
        self.test(Settings)

    def test_share_ios(self):
        Share = SHAREIOS(self.appium_worker)
        self.test(Share)

    def test_support_ios(self):
        Support = SUPPORTIOS(self.appium_worker)
        self.test(Support)

    def test_signup_ios(self):
        SignUp = SIGNUPIOS(self.appium_worker)
        self.test(SignUp)

    def test_waiting_ios(self):
        Waiting = WAITINGPACKAGESIOS(self.appium_worker)
        self.test(Waiting)



if __name__ == '__main__':
    main = Main()
    main.test_all()
