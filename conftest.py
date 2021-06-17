import os

import pytest
from selenium import webdriver
import utilities.cutomLogger as cl
import logging
from utilities.genericUtils import OtherUtils as utils

# @pytest.fixture(params=["chrome", "firefox", "ie"], scope="session")
from testbase import BaseTest
from utilities.readproperties import ReadConfig
from utilities.BrowserstackUtility import BSUtils


@pytest.fixture(autouse=True, scope="class")
def oneTimeSetUp(request, browser):
    log = cl.customLogger(logging.DEBUG)
    # Populate Data from config

    BaseTest.common_dic_data_details = get_Common_TEST_Data()
    # ENV=os.getenv("TEST_ENV")  # Comment this line for local run
    ENV = BaseTest.common_dic_data_details['TEST_ENV']  # Comment this line while commit
    BaseTest.env_dic_data_details = get_Specific_ENV_Details(ENV)
    bs_value = BaseTest.common_dic_data_details['UseBrowserstack']
    if str(bs_value).lower() == str("True").lower():
        bs_obj = BSUtils()
        driver = BSUtils.launch_BS_Remote_Driver()
    else:
        if browser == "chrome":
            log.info("Initializing chrome driver")
            chrome_driver_path = utils.get_project_rootDirectory() + "/SeleniumDrivers/chromedriver.exe"
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

    # This will assign to Global Base Driver in Base class
    BaseTest.Driver = driver

    # Maximize the window
    log.info("Maximizing browser window")
    BaseTest.maximize_window_size()
    # driver.maximize_window()

    # # Create object so that it will call base class constructor which will populate all the required properties
    base = BaseTest()

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
    parser.addoption("--browser", default="chrome", help="Type in browser name e.g. Chrome OR Firefox OR IE")
    # parser.addoption("--osType", help="Type of operating system")


# >>>>>>>>>>>>>>>>>>>>>>>>># This will return the Browser value to setup method<<<<<<<<<<<<<<<<<
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


# @pytest.fixture(scope="session")
# def osType(request):
#     return request.config.getoption("--osType")

def read_Config_Data():
    import configparser
    config_path = utils.get_project_rootDirectory() + "\\configurations\\config.ini"
    BaseTest.config = configparser.RawConfigParser()
    BaseTest.config.read(config_path)


def get_Common_TEST_Data() -> object:
    common_dic_data = {}
    read_Config_Data()
    value = BaseTest.config.get('common info', 'TEST_ENV')
    common_dic_data['TEST_ENV'] = value
    value = BaseTest.config.get('common info', 'UseBrowserstack')
    common_dic_data['UseBrowserstack'] = value
    value = BaseTest.config.get('common info', 'min_wait')
    common_dic_data['min_wait'] = value
    value = BaseTest.config.get('common info', 'medium_wait')
    common_dic_data['medium_wait'] = value
    value = BaseTest.config.get('common info', 'max_wait')
    common_dic_data['max_wait'] = value
    return common_dic_data


def get_Specific_ENV_Details(environment):
    import configparser
    env_dic_data = {}
    read_Config_Data()
    env_value = BaseTest.config.get(environment, 'app_URL')
    env_dic_data['app_URL'] = env_value
    env_value = BaseTest.config.get(environment, 'base_url')
    env_dic_data['base_url'] = env_value
    env_value = BaseTest.config.get(environment, 'user_phone')
    env_dic_data['user_phone'] = env_value
    env_value = BaseTest.config.get(environment, 'password')
    env_dic_data['password'] = env_value
    return env_dic_data
