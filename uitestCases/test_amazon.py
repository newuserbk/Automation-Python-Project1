import time
import unittest
import  allure
import pytest
from allure_commons.types import AttachmentType

from utilities.genericUtils import OtherUtils as utils
import Driver
from pageObjects.HomePage.Headers.create_account_page import CreateAmazonAccount
from pageObjects.HomePage.TopToolbar.bookspage import BooksPage
from pageObjects.LoginPage.loginpage import LoginPage
from testbase import BaseTest
from utilities.genericUtils import OtherUtils
from utilities.readproperties import ReadConfig


class Test_Login(object):
    url = ReadConfig.getApplicationURL()
    phone = ReadConfig.getUserPhone()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    min_wait = ReadConfig.add_min_sleep()
    max_wait = ReadConfig.add_max_sleep()
    guid_value = OtherUtils.generate_random_string()

    def setUp(self):
        # Driver.Initialize()
        pass

    def tearDown(self):
        # Driver.CloseDriver()
        pass

    @pytest.mark.bvt
    @allure.description("test_verify_Amazon_homepage")
    @allure.severity(severity_level="CRITICAL")
    def test_verify_Amazon_homepage(self):
        # >>>>>>>>>>>>>>>>Object Creation<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        __obj_create_account = CreateAmazonAccount()

        # >>>>>>>>>>>>>>>>Test Execution<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        try:
            BaseTest.go_to_url(self.url)
            BaseTest.maximize_window_size()
            BaseTest.IsCorrectPageStatusCode("https://avatax.qa.avalara.io/")
            BaseTest.refresh_browser()
            time.sleep(5)
            __obj_create_account.verify_amazon_logo_image()
        except Exception as ex:
            testName = utils.getTestName()
            allure.attach(BaseTest.Driver.get_screenshot_as_png(), name=testName, Attachment_Type=AttachmentType.PNG)
            raise Exception("....Element Not found....." + ex)

    @pytest.mark.bvt
    @allure.description("test_amazon_create_account_successful")
    @allure.severity(severity_level="CRITICAL")
    def test_amazon_create_account_successful(self):
        # >>>>>>>>>>>>>>>>Object Creation<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        __obj_create_account = CreateAmazonAccount()

        # >>>>>>>>>>>>>>>>Test Execution<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        try:
            BaseTest.go_to_url(self.url)
            BaseTest.maximize_window_size()
            BaseTest.IsPageURLCorrect(self.url)
            __obj_create_account.verify_amazon_logo_image()
            __obj_create_account.select_sign_in_link()
            __obj_create_account.select_create_account_button()
            __obj_create_account.set_your_name("Test_" + self.guid_value)
            __obj_create_account.set_phone(self.phone)
            format_email=self.guid_value+"@gmail.com"
            __obj_create_account.set_email(format_email)
            __obj_create_account.set_password(self.password + self.guid_value)
            # __obj_create_account.re_enter_password(self.password + self.guid_value)
            __obj_create_account.select_continue_button()
            # __obj_create_account.select_create_account_submit_button()

        except Exception as ex:
            testName = utils.getTestName()
            allure.attach(BaseTest.Driver.get_screenshot_as_png(), name=testName, Attachment_Type=AttachmentType.PNG)
            print("Test Failed : "+ex)

    @pytest.mark.bvt
    @allure.description("test_page_http_Status_code")
    @allure.severity(severity_level="NORMAL")
    def test_page_http_Status_code(self):
        # >>>>>>>>>>>>>>>>Object Creation<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        __obj_create_account = CreateAmazonAccount()
        url="https://stackoverflow.com"
        # >>>>>>>>>>>>>>>>Test Execution<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        try:
            BaseTest.go_to_url(url)
            BaseTest.maximize_window_size()
            status_code=BaseTest.check_http_status_code_page(url)
            print(status_code)  # 200

        except Exception as ex:
            testName = utils.getTestName()
            allure.attach(BaseTest.Driver.get_screenshot_as_png(), name=testName, Attachment_Type=AttachmentType.PNG)
            print("Test Failed : "+ex)

    def test_amazon_login_logout(self):
        # >>>>>>>>>>>>>>>>Object Creation<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        __obj_login_page = LoginPage()

        # >>>>>>>>>>>>>>>>Test Execution<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        try:
            __obj_login_page.Login()
            logged_in_username=__obj_login_page.get_logged_in_username()
            assert "Bharat" in logged_in_username
            __obj_login_page.mouse_Hover_sign_in_button()
            __obj_login_page.click_logout_button()
        except Exception as ex:
            testName = utils.getTestName()
            allure.attach(BaseTest.Driver.get_screenshot_as_png(), name=testName, Attachment_Type=AttachmentType.PNG)
            print("Test Failed : "+ex)




