import time

import psutil

import Driver
from testbase import BaseTest
from utilities.globalenums import Environment, FindBy
from utilities.readproperties import ReadConfig
from utilities.seleniumUiActions import SeleniumUIAction


class LoginPage:
    url = ReadConfig.getApplicationURL()
    phone = ReadConfig.getUserPhone()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    env = ReadConfig.getEnv()

    sign_in_link_xpath = "//span[contains(text(),'Hello, Sign in')]"
    email_input_xpath = "//input[@id='ap_email']"
    continue_btn_xpath = "//input[@id='continue']"
    password_input_xpath = "//input[@id='ap_password']"
    sign_in_btn_id = "signInSubmit"
    hello_text_login_name_xpath = "//span[@id='nav-link-accountList-nav-line-1']"
    log_out_btn_xpath = "//span[text()='Sign Out']"

    @staticmethod
    def clean_and_close_browser_instances(self):
        """ Check if there is any running process
        that contains the given name processName."""
        # Iterate over the all the running process
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if "chrome".lower() in proc.name().lower():
                    proc.kill()
                elif "chromedriver".lower() in proc.name().lower():
                    proc.kill()
                else:
                    pass

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def navigate_to_login_page(self):
        if self.env.isupper() == Environment.DEV.name.isupper():
            url = self.url
            username = self.email
            password = self.password
        elif self.env == Environment.STAGING:
            url = "http://testautomationguru.com"
            username = "tag"
            password = "password"
        else:
            pass

        print(".............Launching Application URL : " + self.url)
        Driver.Instance.get(self.url)
        print("..............Maximizing browser window..............")
        BaseTest.maximize_window_size()

    def enter_username(self, username):
        print("Enter UserName/Mobile Number")
        SeleniumUIAction.Set_textbox_value(FindBy.XPATH, self.email_input_xpath, username)

    def click_continue_button(self):
        print("clicking on continue button")
        SeleniumUIAction.click_element(FindBy.XPATH, self.continue_btn_xpath)

    def enter_password(self, password):
        print("Enter Password")
        SeleniumUIAction.Set_textbox_value(FindBy.XPATH, self.password_input_xpath, password)

    def click_log_in_button(self):
        print("clicking on login button")
        SeleniumUIAction.click_element(FindBy.ID, self.sign_in_btn_id)
        time.sleep(5)

    def Login(self, userType="Normal"):
        # self.clean_and_close_browser_instances(self)
        self.navigate_to_login_page()
        self.click_sign_in_button()
        self.enter_username("9561788056")
        self.click_continue_button()
        self.enter_password("Password@1234")
        self.click_log_in_button()

    def click_logout_button(self):
        print("clicking on logout button")
        SeleniumUIAction.click_element(FindBy.XPATH, self.log_out_btn_xpath)

    def click_sign_in_button(self):
        print("clicking on Sign In button")
        SeleniumUIAction.click_element(FindBy.XPATH, self.hello_text_login_name_xpath)

    def get_logged_in_username(self):
        print("verifying logged in username")
        element = Driver.FindVisibleElement(FindBy.XPATH, self.hello_text_login_name_xpath)
        print("UserName : " + element.text)
        return element.text

    def mouse_Hover_sign_in_button(self):
        print("Mouse Hover on Sign In button")
        SeleniumUIAction.HoverMouseOver(FindBy.XPATH, self.hello_text_login_name_xpath)
        time.sleep(4)
