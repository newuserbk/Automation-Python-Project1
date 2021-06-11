import pytest
from selenium import webdriver
import utilities.cutomLogger as cl
import logging
from utilities.genericUtils import OtherUtils as utils


# @pytest.fixture(params=["chrome", "firefox", "ie"], scope="session")
from testbase import BaseTest


@pytest.yield_fixture(autouse=True,scope="class")
def oneTimeSetUp(request,browser):
    log = cl.customLogger(logging.DEBUG)
    if browser == "chrome":
        log.info("Initializing chrome driver")
        chrome_driver_path=utils.get_project_rootDirectory()+"/SeleniumDrivers/chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
    elif browser == 'firefox':
        log.info("Initializing Firefox driver")
        driver = webdriver.Firefox()
    elif browser == 'IE':
        log.info("Initializing IE driver")
        driver = webdriver.Ie()
    # else:
    #     log.info("Initializing Default chrome driver")
    #     driver = webdriver.Chrome("C:/Personal Doc/Returns team/Selenium Drivers/chromedriver.exe")

    # Setting Driver Implicit Time out for An Element
    log.info("Applying implicit wait on driver for 3 seconds")
    driver.implicitly_wait(3)
    # Maximize the window
    log.info("Maximizing browser window")
    driver.maximize_window()

    # This will assign to Global Base Driver in Base class
    BaseTest.Driver=driver

    # Populate Data from config
    config_path = utils.get_project_rootDirectory() + "\\configurations\\config.ini"
    import configparser
    BaseTest.config = configparser.RawConfigParser()
    BaseTest.config.read(config_path)

    # # Create object so that it will call base class constructor which will populate all the required properties
    base=BaseTest()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    log.info("closing driver")
    driver.quit()
    print("Running one time tearDown")


# @pytest.fixture(params=["chrome"],scope="class")
# def setup(request):
#     if request.param == "chrome":
#         web_driver = webdriver.Chrome("../SeleniumDrivers/chromedriver.exe")
#     elif request.param == 'firefox':
#         web_driver = webdriver.Firefox()
#         print("Launching Firefox browser.........")
#     else:
#         web_driver = webdriver.Ie()
#     request.cls.driver=web_driver


# >>>>>>>>>>>>>>>>>>>>>>>>> This will get the value from CLI /hooks<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def pytest_addoption(parser):
    parser.addoption("--browser",default="chrome",help="Type in browser name e.g. Chrome OR Firefox OR IE")
    # parser.addoption("--osType", help="Type of operating system")


# >>>>>>>>>>>>>>>>>>>>>>>>># This will return the Browser value to setup method<<<<<<<<<<<<<<<<<
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


# @pytest.fixture(scope="session")
# def osType(request):
#     return request.config.getoption("--osType")