import time
from traceback import print_stack

import requests
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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
            FindBy.ID: (By.ID, search_criteria),
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
    def getByType(locatorType):
        locator_type = locatorType.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        else:
            print("locator type " + locator_type + " is not correct or supported")
        return False

    @staticmethod
    def wait_for_element(self, locator, locatorType="id", timeout=10, poll_frequency=0.5):
        element: None
        try:
            byType=SeleniumUIAction.getByType(locatorType)
            print("waiting for maximum :: " + str(timeout) + " :: for seconds to element clickable")
            wait=WebDriverWait(Driver.Instance,timeout,poll_frequency=1,ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException])
            element=wait.until(EC.element_to_be_clickable(byType,""))
            print("element appeared on the web page")
        except:
            print("element IS NOT appeared on the web page")
            print_stack()
        return element

    @staticmethod
    def IsDisplayed(FindBy, search_criteria):

        element = None
        is_display_element = None
        try:

            # element = Driver.Instance.find_element(FindBy, search_criteria)
            # element = Driver.Instance.find_element(SeleniumUIAction.GenerateLocatorObject(FindBy, search_criteria))
            element = Driver.FindVisibleElement(FindBy, search_criteria)
            if element.displayed():
                is_display_element = True
        except Exception as ex:
            print("..Element Not Found using locator : " + search_criteria + "Exception : " + ex)
            is_display_element = False
            return is_display_element

    @staticmethod
    def IsNotDisplayed(FindBy, search_criteria):
        is_display_element = None
        element = Driver.FindVisibleElement(FindBy, search_criteria)
        if element is None:
            is_display_element = False

        return is_display_element

    @staticmethod
    def IsEnabled(FindBy, search_criteria):
        is_enabled = None
        try:
            element = Driver.FindVisibleElement(FindBy, search_criteria)
            is_enabled = element.enabled

        except Exception as ex:
            print("..Element Not Found using locator : " + search_criteria + "Exception : " + ex)
        return is_enabled

    @staticmethod
    def IsDisabled(FindBy, search_criteria):
        is_disabled = None
        try:
            element = Driver.FindVisibleElement(FindBy, search_criteria)
            if element.enabled() != False:
                is_disabled = True

        except Exception as ex:
            print("..Element Not found using locator : " + search_criteria + "Exception : " + ex)
        return is_disabled

    @staticmethod
    def IsSelected(FindBy, search_criteria):
        is_selected = None
        try:
            element = Driver.FindVisibleElement(FindBy, search_criteria)
            is_selected = element.is_selected

        except Exception as ex:
            print("..Element Not found using locator : " + search_criteria + "Exception : " + ex)
        return is_selected

    @staticmethod
    def IsNotSelected(FindBy, search_criteria):
        is_not_elected = None
        try:
            element = Driver.FindVisibleElement(FindBy, search_criteria)
            is_not_elected = element.is_selected
            if not is_not_elected:
                print("Element is not Selected")
            else:
                print("Error: Element is  selected")

        except Exception as ex:
            print("..Element Not found using locator : " + search_criteria + "Exception : " + ex)
        return is_not_elected

    @staticmethod
    def GetCSSValues(FindBy, search_criteria):
        list_css_details = None
        try:
            element = Driver.FindVisibleElement(FindBy, search_criteria)

            if element is not None:
                list_css_details.append(element.GetCssValue("font-type"))
                list_css_details.append(element.GetCssValue("font-family"))
                list_css_details.append(element.GetCssValue("font-size"))
                list_css_details.append(element.GetCssValue("background-color"))

        except Exception as ex:
            print("..Element Not found using locator : " + search_criteria + "Exception : " + ex)
        return list_css_details

    @staticmethod
    def Get_Text(FindBy, search_criteria):
        element_text = None
        try:
            element = Driver.FindVisibleElement(FindBy, search_criteria)
            if element is not None:
                element_text = element.text

        except Exception as ex:
            print("..Element Not found using locator : " + search_criteria + "Exception : " + ex)
        return element_text

    @staticmethod
    def GetAttributeValue(FindBy, search_criteria, attribute_name):
        attribute_value = None
        element = Driver.FindVisibleElement(FindBy, search_criteria)
        attribute_value = element.get_attribute(attribute_name)
        return attribute_value

    @staticmethod
    def IsTooltipCorrect(FindBy, search_criteria, expected_tooltip):
        actual_tooltip = None
        actual_tooltip = SeleniumUIAction.GetAttributeValue(FindBy, search_criteria, "title")
        if actual_tooltip == expected_tooltip:
            print("Tooltip is correct")
            return True
        else:
            print("Tooltip is not correct")
            return False

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
    def ScrollToElement(FindBy, search_criteria):
        element = Driver.FindVisibleElement(FindBy, search_criteria)
        actions = ActionChains(Driver.Instance)
        actions.move_to_element(element).perform()

    @staticmethod
    def scrollDown(value):
        Driver.Instance.execute_script("window.scrollBy(0," + str(value) + ")")

    # Scroll down the page
    @staticmethod
    def scrollDownAllTheWay(driver):
        old_page = Driver.Instance.page_source
        while True:
            print("Scrolling loop")
            for i in range(2):
                SeleniumUIAction.scrollDown(2)
                time.sleep(2)
            new_page = Driver.Instance.page_source
            if new_page != old_page:
                old_page = new_page
            else:
                break
        return True

    @staticmethod
    def HoverMouseOver(FindBy, search_criteria):
        element = Driver.FindVisibleElement(FindBy, search_criteria)
        actions = ActionChains(Driver.Instance)
        actions.move_to_element(element).perform()
        time.sleep(3)

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
    def GetTooltip(element):
        tooltip = element.GetAttribute("title")
        return tooltip

    @staticmethod
    def SelectItemByName(FindBy, search_criteria, item_name):
        element = None
        try:
            element = Driver.FindClickableElement(FindBy,
                                                  "//div[@id='nav-search-dropdown-card']//select[@title='Search in']/option[text(),'Books']")
            element.click()
            # drop = Select(element)
            # drop.select_by_visible_text(item_name)
            # drp_element = Driver.FindClickableElement(FindBy,search_criteria)
            # action = ActionChains(Driver.Instance)
            # action.click(on_element=drp_element).perform()
        except Exception as ex:
            print("..Element Not Found using locator : " + search_criteria + "Exception : " + ex)

    @staticmethod
    def SelectItemByIndex(FindBy, search_criteria, itemIndex):
        element = Driver.FindClickableElement(FindBy, search_criteria)
        select = Select(element)
        select.select_by_visible_text(itemIndex)

    @staticmethod
    def SelectCheckbox(FindBy, search_criteria):
        element = Driver.FindClickableElement(FindBy, search_criteria)
        if element.is_selected():
            element.click()

    @staticmethod
    def DeselectCheckbox(FindBy, search_criteria):
        element = Driver.FindClickableElement(FindBy, search_criteria)
        if element.is_selected():
            element.click()

    @staticmethod
    def SelectRadioButton(FindBy, search_criteria):
        element = Driver.FindClickableElement(FindBy, search_criteria)
        if element.is_selected():
            element.click()

    @staticmethod
    def DeselectRadioButton(FindBy, search_criteria):
        element = Driver.FindClickableElement(FindBy, search_criteria)
        if element.is_selected():
            element.click()

    @staticmethod
    def IsElementSelected(FindBy, search_criteria):
        element = Driver.FindClickableElement(FindBy, search_criteria)
        if element.selected:
            return True
        else:
            return False

    @staticmethod
    def GetDropDownList(FindBy, search_criteria):
        element = Driver.FindClickableElement(FindBy, search_criteria)
        select = Select(element)
        return select.options

    @staticmethod
    def SwitchToFrame(FindBy, search_criteria):
        try:
            frame = Driver.FindVisibleElement(FindBy, search_criteria)
            Driver.Instance.switch_to_frame(frame)
        except Exception as ex:
            print("Failed to switch to frame. Error:-  " + ex)

    @staticmethod
    def GetTableElements(FindBy, search_criteria):
        element = Driver.FindClickableElement(FindBy, search_criteria)

    @staticmethod
    def get_header_column_values(driver):
        table = Driver.Instance.find_element_by_xpath("//table")
        head_data = []
        for td in table.find_elements_by_tag_name('th'):
            head_data.append(td.text)
        print(head_data)

    @staticmethod
    def get_row_count(self):
        table = Driver.Instance.find_element_by_xpath("//table")
        return len(table.find_elements_by_tag_name("tr")) - 1

    @staticmethod
    def get_column_count(self):
        table = Driver.Instance.find_element_by_xpath("//table")
        return len(table.find_elements_by_tag_name("//tr[2]/td"))

    # get rowdata and return it as list
    @staticmethod
    def row_data(self, row_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")

        row_number = row_number + 1
        table = Driver.Instance.find_element_by_xpath("//table")
        row = table.find_elements_by_xpath("//tr[" + str(row_number) + "]/td")
        r_data = []
        for webElement in row:
            r_data.append(webElement.text)

        return r_data

    # get the column data and return as list
    @staticmethod
    def column_data(self, column_number):
        table = Driver.Instance.find_element_by_xpath("//table")
        col = table.find_elements_by_xpath("//tr/td[" + str(column_number) + "]")
        r_data = []
        for webElement in col:
            r_data.append(webElement.text)
        return r_data

    @staticmethod
    def get_column_data_values(driver):
        table = Driver.Instance.find_element_by_xpath("//table")
        col_data = []
        for td in table.find_elements_by_tag_name('td'):
            col_data.append(td.text)
        print(col_data)

    @staticmethod
    def get_row_data_values(driver):
        table = Driver.Instance.find_element_by_xpath("//table")
        row_data = []
        for td in table.find_elements_by_tag_name('tr'):
            row_data.append(td.text)
        print(row_data)

    @staticmethod
    def get_all_data():
        table = Driver.Instance.find_element_by_xpath("//table")
        # get number of rows
        noOfRows = len(table.find_elements_by_xpath("//tr")) - 1
        # get number of columns
        noOfColumns = len(table.find_elements_by_xpath("//tr[2]/td"))
        allData = []
        # iterate over the rows, to ignore the headers we have started the i with '1'
        for i in range(2, noOfRows):
            # reset the row data every time
            ro = []
            # iterate over columns
            for j in range(1, noOfColumns):
                # get text from the i th row and j th column
                ro.append(table.find_element_by_xpath("//tr[" + str(i) + "]/td[" + str(j) + "]").text)

            # add the row data to allData of the self.table
            allData.append(ro)

        return allData

    @staticmethod
    def get_cell_data(row_number, column_number):
        table = Driver.Instance.find_element_by_xpath("//table")
        if row_number == 0:
            raise Exception("Row number starts from 1")

        rowNumber = row_number + 1
        cellData = table.find_element_by_xpath("//tr[" + str(rowNumber) + "]/td[" + str(column_number) + "]").text
        return cellData

    @staticmethod
    def IsNewTabOpened():
        is_new_tab_opened = None
        tabs = Driver.Instance.window_handles
        if tabs.count() == 2:
            is_new_tab_opened = True
        return is_new_tab_opened

    @staticmethod
    def SelectDateInDatePickerField(FindBy, search_criteria):
        date_input = Driver.FindClickableElement(FindBy, search_criteria)
        date_input.click()
        # date_input.send_keys(Keys.CONTROL, "a")  # Select all pre-existing text/input value
        # date_input.send_keys(Keys.BACKSPACE)  # Remove that text
        date_input.send_keys("01012011")

    @staticmethod
    def is_page_load_complete(FindBy, search_criteria):
        print("Checking if {} page is loaded.".format(Driver.Instance.current_url))
        element = Driver.FindVisibleElement(FindBy, search_criteria)
        while not SeleniumUIAction.page_is_loading():
            continue

    @staticmethod
    def page_is_loading():
        while True:
            state = Driver.Instance.execute_script("return document.readyState")
            if state == "complete":
                return True
            else:
                yield False
