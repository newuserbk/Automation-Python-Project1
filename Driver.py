# import os
# import time
# from traceback import print_stack
#
# import allure
# import self
# from allure_commons.types import AttachmentType
# from selenium import webdriver
# from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, InvalidSelectorException, \
#     TimeoutException
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# from utilities.readproperties import ReadConfig
# from utilities.seleniumUiActions import SeleniumUIAction
#
# max_wait = ReadConfig.add_max_sleep()
#
# Instance = None
#
#
# def Initialize():
#     global Instance
#     Instance = webdriver.Chrome("C:/Personal Doc/Returns Team/Selenium Drivers/chromedriver.exe")
#     Instance.implicitly_wait(5)
#     return Instance
#
#
# def Initialize_Headless():
#     global Instance
#     from selenium.webdriver.chrome.options import Options
#
#     options = Options()
#     options.add_argument('--headless')
#     options.add_argument('--disable-gpu')  # Last I checked this was necessary.
#     Instance = webdriver.Chrome("C:/Personal Doc/Returns Team/Selenium Drivers/chromedriver.exe",
#                                 chrome_options=options)
#     Instance.implicitly_wait(5)
#     return Instance
#
#
# def CloseDriver():
#     global Instance
#     print("Closing Browser")
#     Instance.quit()
#
#
# def screenShot(resultMessage):
#     """
#             Takes screenshot of the current open web page
#             """
#     fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
#     screenshotDirectory = "../screenshots/"
#     relativeFileName = screenshotDirectory + fileName
#     currentDirectory = os.path.dirname(__file__)
#     destinationFile = os.path.join(currentDirectory, relativeFileName)
#     destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
#
#     try:
#         if not os.path.exists(destinationDirectory):
#             os.makedirs(destinationDirectory)
#         self.driver.save_screenshot(destinationFile)
#         self.log.info("Screenshot save to directory: " + destinationFile)
#     except:
#         self.log.error("### Exception Occurred when taking screenshot")
#         print_stack()
#
#
# def FindElement(FindBy, search_criteria, wait_time=None):
#     element = None
#     try:
#         if wait_time == 0:
#             wait_time = max_wait
#
#         element = WebDriverWait(Instance, wait_time).until(
#             EC.presence_of_element_located(SeleniumUIAction.GenerateLocatorObject(FindBy, search_criteria))
#         )
#     except (StaleElementReferenceException, NoSuchElementException, InvalidSelectorException, TimeoutException) as ex:
#         pass
#     return element
#
#
# def FindClickableElement(FindBy, search_criteria, wait_time=5):
#     element = None
#     try:
#         if wait_time == 0:
#             wait_time = max_wait
#
#         element = WebDriverWait(Instance, wait_time).until(
#             EC.element_to_be_clickable(SeleniumUIAction.GenerateLocatorObject(FindBy, search_criteria))
#         )
#     except (StaleElementReferenceException, NoSuchElementException, InvalidSelectorException, TimeoutException) as ex:
#         pass
#     return element
#
#
# def FindVisibleElement(FindBy, search_criteria, wait_time=5):
#     element = None
#     try:
#         if wait_time == 0:
#             wait_time = max_wait
#
#         element = WebDriverWait(Instance, wait_time).until(
#             EC.visibility_of_element_located(SeleniumUIAction.GenerateLocatorObject(FindBy, search_criteria))
#         )
#     except (StaleElementReferenceException, NoSuchElementException, InvalidSelectorException, TimeoutException) as ex:
#         # allure.attach(Instance.get_screenshot_as_png(),name="logintest",Attachment_Type=AttachmentType.PNG)
#         pass
#     return element
#
#
# def WaitTillPageURLContains(expectedPartialURL, wait_time=5):
#     element = None
#     try:
#         if wait_time == 0:
#             wait_time = max_wait
#
#         element = WebDriverWait(Instance, wait_time).until(
#             EC.url_contains(expectedPartialURL)
#         )
#     except (StaleElementReferenceException, NoSuchElementException, InvalidSelectorException, TimeoutException) as ex:
#         pass
#     return element
#
#
# def WaitTillElementAppears(FindBy, search_criteria, wait_time=None):
#     has_element_appeared = None
#     try:
#         if wait_time == 0:
#             wait_time = max_wait
#
#         element = WebDriverWait(Instance, wait_time).until(
#             EC.visibility_of_any_elements_located(SeleniumUIAction.GenerateLocatorObject(FindBy, search_criteria))
#         )
#         has_element_appeared = element.displayed
#
#     except (StaleElementReferenceException, NoSuchElementException, InvalidSelectorException, TimeoutException) as ex:
#         pass
#         return has_element_appeared
#
#
# def WaitTillElementDisAppears(FindBy, search_criteria, wait_time=None):
#     has_element_appeared = None
#     try:
#         if wait_time == 0:
#             wait_time = max_wait
#
#         has_element_appeared = WebDriverWait(Instance, wait_time).until(
#             EC.invisibility_of_element_located(SeleniumUIAction.GenerateLocatorObject(FindBy, search_criteria))
#         )
#
#     except (StaleElementReferenceException, NoSuchElementException, InvalidSelectorException, TimeoutException) as ex:
#         pass
#     return has_element_appeared
