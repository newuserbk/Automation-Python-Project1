from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from testbase import BaseTest
from utilities.globalenums import FindBy
from utilities.seleniumuiactions import SeleniumUIAction


class CreateAmazonAccount:
    # >>>>>>>>>>>>>>>>Locators Initialization <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    amazon_logo_image_xpath = "(//div[@id='nav-logo']/a//span)[2]"
    sign_in_link_xpath = "//span[contains(text(),'Hello, Sign in')]"
    create_account_btn_id = "createAccountSubmit"
    your_name_input_xpath = "//input[@name='customerName']"
    mobile_input_xpath = "//input[@name='email']"
    email_input_xpath = "//input[@id='ap_email']"
    password_input_xpath = "//input[@name='password']"
    re_enter_input_xpath = "//input[@name='passwordCheck']"
    continue_btn_xpath = "//input[@id='continue']"
    submit_account_btn_xpath = "//span[contains(text(),'Create your Amazon account')]"

    # >>>>>>>>>>>>>>>>POM Methods <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def verify_amazon_logo_image(self):
        print("..............Verifying Amazon Logo Image ..............")
        SeleniumUIAction.IsDisplayed(FindBy.XPATH, self.amazon_logo_image_xpath)

    def select_sign_in_link(self):
        print("..............Clicking on Sign In Hello ..............")
        SeleniumUIAction.click_element(FindBy.XPATH, self.sign_in_link_xpath)

    def select_create_account_button(self):
        print("..............Clicking on Create your account button ..............")
        SeleniumUIAction.click_element(FindBy.ID, self.create_account_btn_id)

    def set_your_name(self, your_name):
        print("..............Entering your name ..............")
        SeleniumUIAction.Set_textbox_value(FindBy.XPATH, self.your_name_input_xpath, your_name)

    def set_phone(self, your_phone):
        print("..............Entering email or phone ..............")
        SeleniumUIAction.Set_textbox_value(FindBy.XPATH, self.mobile_input_xpath, your_phone)

    def set_email(self, your_email):
        print("..............Entering email or phone ..............")
        SeleniumUIAction.Set_textbox_value(FindBy.XPATH, self.email_input_xpath, your_email)

    def set_password(self, your_name):
        print("..............Entering password ..............")
        SeleniumUIAction.Set_textbox_value(FindBy.XPATH, self.password_input_xpath, your_name)

    def re_enter_password(self, your_name):
        print("..............Re-Entering password ..............")
        SeleniumUIAction.Set_textbox_value(FindBy.XPATH, self.re_enter_input_xpath, your_name)

    def select_continue_button(self):
        print("..............Select Continue Button ..............")
        SeleniumUIAction.click_element(FindBy.XPATH, self.continue_btn_xpath)

    def select_create_account_submit_button(self):
        print("..............Selecting Create Your Account Submit Button ..............")
        SeleniumUIAction.click_element(FindBy.XPATH, self.submit_account_btn_xpath)
