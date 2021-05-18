import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import Driver
from testbase import BaseTest
from selenium.webdriver.common.by import By


class SeleniumUIAction:

    @staticmethod
    def GenerateLocatorObject(FindBy, search_criteria):
        switcher = {
            FindBy.ID:(By.ID, search_criteria),
            FindBy.XPATH: (By.XPATH, search_criteria),
            FindBy.CSS_SELECTOR: (By.CSS_SELECTOR, search_criteria),
            FindBy.CLASS_NAME: (By.CLASS_NAME, search_criteria),
        }
        # get() method of dictionary data type returns
        # value of passed argument if it is present
        # in dictionary otherwise second argument will
        # be assigned as default value of passed argument
        return switcher.get(FindBy, "No Switch Case Math/ Default Case")

    @staticmethod
    def IsDisplayed(FindBy, search_criteria):

        element = None
        is_display_element = None
        try:

            # element = Driver.Instance.find_element(FindBy, search_criteria)
            # element = Driver.Instance.find_element(SeleniumUIAction.GenerateLocatorObject(FindBy, search_criteria))
            element=Driver.FindVisibleElement(FindBy, search_criteria)
            if element is not None:
                is_display_element = True
        except Exception as ex:
            print("..Element Not Found using locator : " + search_criteria + "Exception : ")
            is_display_element = False
            return is_display_element

    @staticmethod
    def IsNotDisplayed(self, FindBy, search_criteria):
        is_display_element = None
        element = Driver.FindVisibleElement(FindBy, search_criteria)
        if element is None:
            is_display_element = False

        return is_display_element

    @staticmethod
    def IsEnabled():
        pass

    @staticmethod
    def IsDisabled():
        pass

    @staticmethod
    def click_element(FindBy, search_criteria, wait_time=5):
        try:
            element = Driver.FindClickableElement(FindBy, search_criteria)
            element.click()
        except Exception as ex:
            raise Exception(f"unable to find element using search criteria : {FindBy} and  {search_criteria}" + ex)

    @staticmethod
    def clickMultipleElements(findUsing, searchCriteria, wait_time):
        elements = Driver.Instance.FindAllPresentElements(findUsing, searchCriteria, wait_time)
        for item in elements:
            actions = ActionChains(Driver.Instance)
            actions.move_to_element(item).perform()
            item.Click()

    @staticmethod
    def ScrollToElement():
        element = Driver.Instance.find_element_by_xpath("")
        actions = ActionChains(Driver.Instance)
        actions.move_to_element(element).perform()

    @staticmethod
    def Set_textbox_value(FindBy, search_criteria, value_to_enter):
        element = Driver.FindVisibleElement(FindBy, search_criteria)
        element.click()
        element.clear()
        element.send_keys(value_to_enter)

    @staticmethod
    def GetBrowserWindowTitle():
        return Driver.Instance.title

    @staticmethod
    def GetTooltip(self, element):
        tooltip = element.GetAttribute("title")
        return tooltip

    @staticmethod
    def SelectItemByName(self, itemname):
        select = Select(Driver.Instance.find_element_by_id('fruits01'))
        select.select_by_visible_text(itemname)

    @staticmethod
    def SelectItemByIndex(self, itemIndex):
        select = Select(Driver.Instance.find_element_by_id('fruits01'))
        select.select_by_index(itemIndex)

    @staticmethod
    def SelectCheckbox(self):
        pass

    @staticmethod
    def DeselectCheckbox(self):
        pass

    @staticmethod
    def SelectRadioButton(self):
        pass

    @staticmethod
    def DeselectRadioButton(self):
        pass

    @staticmethod
    def IsElementSelected(self):
        element = Driver.Instance.find_element_by_id('fruits01')
        if element.selected:
            return True
        else:
            return False

    @staticmethod
    def GetDropDownList(self):
        select = Select(Driver.Instance.find_element_by_id('fruits01'))
        return select.options

    @staticmethod
    def GetTableElements(self):
        pass

    @staticmethod
    def SelectDateInDatePickerField(self):
        pass

    @staticmethod
    def IsPageLoadComplete(self):
        # if ((Boolean)((IJavaScriptExecutor)d).ExecuteScript("return document.readyState").Equals("complete"))
        pass
