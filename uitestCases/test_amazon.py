import time
import unittest

import Driver
from pageObjects.HomePage.Headers.create_account_page import CreateAmazonAccount
from pageObjects.HomePage.TopToolbar.bookspage import BooksPage
from pageObjects.LoginPage.loginpage import LoginPage
from testbase import BaseTest
from utilities.otherutilities import Other_Utilities
from utilities.readproperties import ReadConfig


class Test_Login(unittest.TestCase):
    url = ReadConfig.getApplicationURL()
    phone = ReadConfig.getUserPhone()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    min_wait = ReadConfig.add_min_sleep()
    max_wait = ReadConfig.add_max_sleep()
    guid_value = Other_Utilities.generate_random_string()

    def setUp(self):
        Driver.Initialize()

    def tearDown(self):
        Driver.CloseDriver()

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
            raise Exception("....Element Not found....." + ex)

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
            print("Test Failed : "+ex)

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
            print("Test Failed : "+ex)

    def test_amazon_search_functionality(self):
        # >>>>>>>>>>>>>>>>Object Creation<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        __obj_login_page = LoginPage()
        __obj_books_page=BooksPage()

        # >>>>>>>>>>>>>>>>Test Execution<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        try:
            __obj_login_page.Login()
            logged_in_username=__obj_login_page.get_logged_in_username()
            assert "Bharat" in logged_in_username
            __obj_books_page.select_Books_dropdown_link("Books")
            __obj_books_page.set_search_book_name("success")
            __obj_books_page.click_search_button()
            __obj_books_page.verify_book_image()

        except Exception as ex:
            print("Test Failed : "+ex)


