from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, InvalidSelectorException, \
    TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.readproperties import ReadConfig
from utilities.seleniumuiactions import SeleniumUIAction

max_wait = ReadConfig.add_max_sleep()

Instance = None


def Initialize():
    global Instance
    Instance = webdriver.Chrome("C:/Personal Doc/Returns Team/Selenium Drivers/chromedriver.exe")
    Instance.implicitly_wait(5)
    return Instance


def Initialize_Headless():
    global Instance
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    Instance = webdriver.Chrome("C:/Personal Doc/Returns Team/Selenium Drivers/chromedriver.exe", chrome_options=options)
    Instance.implicitly_wait(5)
    return Instance


def CloseDriver():
    global Instance
    print("Closing Browser")
    Instance.quit()


def FindElement(FindBy, search_criteria, wait_time=None):
    element = None
    try:
        if wait_time == 0:
            wait_time = max_wait

        element = WebDriverWait(Instance, wait_time).until(
            EC.presence_of_element_located(SeleniumUIAction.GenerateLocatorObject(FindBy, search_criteria))
        )
    except (StaleElementReferenceException, NoSuchElementException, InvalidSelectorException, TimeoutException) as ex:
        pass
    return element


def FindClickableElement(FindBy, search_criteria, wait_time=5):
    element = None
    try:
        if wait_time == 0:
            wait_time = max_wait

        element = WebDriverWait(Instance, wait_time).until(
            EC.element_to_be_clickable(SeleniumUIAction.GenerateLocatorObject(FindBy, search_criteria))
        )
    except (StaleElementReferenceException, NoSuchElementException, InvalidSelectorException, TimeoutException) as ex:
        pass
    return element


def FindVisibleElement(FindBy, search_criteria, wait_time=5):
    element = None
    try:
        if wait_time == 0:
            wait_time = max_wait

        element = WebDriverWait(Instance, wait_time).until(
            EC.visibility_of_element_located(SeleniumUIAction.GenerateLocatorObject(FindBy, search_criteria))
        )
    except (StaleElementReferenceException, NoSuchElementException, InvalidSelectorException, TimeoutException) as ex:
        pass
    return element


def WaitTillPageURLContains(expectedPartialURL, wait_time=5):
    element = None
    try:
        if wait_time == 0:
            wait_time = max_wait

        element = WebDriverWait(Instance, wait_time).until(
            EC.url_contains(expectedPartialURL)
        )
    except (StaleElementReferenceException, NoSuchElementException, InvalidSelectorException, TimeoutException) as ex:
        pass
    return element


def WaitTillElementAppears(FindBy, search_criteria, wait_time=None):
    has_element_appeared = None
    try:
        if wait_time == 0:
            wait_time = max_wait

        element = WebDriverWait(Instance, wait_time).until(
            EC.visibility_of_any_elements_located(SeleniumUIAction.GenerateLocatorObject(FindBy, search_criteria))
        )
        has_element_appeared = element.displayed

    except (StaleElementReferenceException, NoSuchElementException, InvalidSelectorException, TimeoutException) as ex:
        pass
        return has_element_appeared


def WaitTillElementDisAppears(FindBy, search_criteria, wait_time=None):
    has_element_appeared = None
    try:
        if wait_time == 0:
            wait_time = max_wait

        has_element_appeared = WebDriverWait(Instance, wait_time).until(
            EC.invisibility_of_element_located(SeleniumUIAction.GenerateLocatorObject(FindBy, search_criteria))
        )

    except (StaleElementReferenceException, NoSuchElementException, InvalidSelectorException, TimeoutException) as ex:
        pass
    return has_element_appeared
