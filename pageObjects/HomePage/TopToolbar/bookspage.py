from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from testbase import BaseTest
from utilities.globalenums import FindBy
from utilities.seleniumuiactions import SeleniumUIAction


class BooksPage:
    # >>>>>>>>>>>>>>>>Locators Initialization <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    search_DropdownDescription_xpath = "//div[@id='nav-search-dropdown-card']//select[@title='Search in']/option"
    search_input_textbox_id = "twotabsearchtextbox"
    search_btn_id = "nav-search-submit-button"
    chronic_image_xpath = "//img[@alt='Chronicles of Narnia (The Chronicles of Narnia)']"

    # >>>>>>>>>>>>>>>>POM Methods <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def verify_book_image(self):
        print("..............Verifying Amazon Logo Image ..............")
        SeleniumUIAction.IsDisplayed(FindBy.XPATH, self.chronic_image_xpath)

    def select_Books_dropdown_link(self,name):
        print("..............Selecting Books from drop down ..............")
        SeleniumUIAction.SelectItemByName(FindBy.XPATH, self.search_DropdownDescription_xpath,name)

    def set_search_book_name(self,bookname):
        print("..............Entering/Searching for success book ..............")
        SeleniumUIAction.Set_textbox_value(FindBy.ID, self.create_account_btn_id,bookname)

    def click_search_button(self):
        print("..............Clicking search button..............")
        SeleniumUIAction.click_element(FindBy.ID, self.search_btn_id)
