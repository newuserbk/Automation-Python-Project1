import pytest
from selenium import webdriver


# @pytest.fixture(params=["chrome", "firefox", "ie"], scope="session")
# @pytest.fixture(autouse=True,scope="class")
# def init_driver(browser):
#     if browser == "chrome":
#         driver = webdriver.Chrome("C:/Personal Doc/Returns Team/Selenium Drivers/chromedriver.exe")
#     elif browser == 'firefox':
#         driver = webdriver.Firefox()
#         print("Launching Firefox browser.........")
#     else:
#         driver = webdriver.Ie()
#     return driver


# @pytest.fixture(params=["chrome"],scope="class")
# def setup(request):
#     if request.param == "chrome":
#         web_driver = webdriver.Chrome("C:/Personal Doc/Returns Team/Selenium Drivers/chromedriver.exe")
#     elif request.param == 'firefox':
#         web_driver = webdriver.Firefox()
#         print("Launching Firefox browser.........")
#     else:
#         web_driver = webdriver.Ie()
#     request.cls.driver=web_driver


# >>>>>>>>>>>>>>>>>>>>>>>>> This will get the value from CLI /hooks<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def pytest_addoption(parser):
#     parser.addoption("--browser")


# >>>>>>>>>>>>>>>>>>>>>>>>># This will return the Browser value to setup method<<<<<<<<<<<<<<<<<
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")