import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BSUtils(object):

    @staticmethod
    def launch_BS_Remote_Driver():
        # desired_cap = {
        #     'os_version': '10',
        #     'resolution': '1920x1080',
        #     'browser': 'Chrome',
        #     'browser_version': '90.0',
        #     'os': 'Windows',
        #     'name': 'BStack-[Python] Sample Test',  # test name
        #     'build': 'BStack Build Number 1'  # CI/CD job or build name
        # }
        # driver = webdriver.Remote(
        #     command_executor='https://pravachandk_yNi7uf:xzrJ93h6wTosgxmaLBDy@hub-cloud.browserstack.com/wd/hub',
        #     desired_capabilities=desired_cap)
        username = os.getenv("BROWSERSTACK_USERNAME")
        access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
        build_name = os.getenv("BROWSERSTACK_BUILD_NAME")
        browserstack_local = os.getenv("BROWSERSTACK_LOCAL")
        browserstack_local_identifier = os.getenv("BROWSERSTACK_LOCAL_IDENTIFIER")

        desired_cap = {
            'os': 'Windows',
            'os_version': '10',
            'browser': 'chrome',
            'browser_version': 'latest',
            # 'browser_version': '90.0',
            'w3c': 'false',
            'name': 'BStack-[Jenkins] Sample Test',  # test name
            'build': build_name,  # CI/CD job name using BROWSERSTACK_BUILD_NAME env variable
            'browserstack.local': browserstack_local,
            'browserstack.localIdentifier': browserstack_local_identifier,
            'browserstack.user': username,
            'browserstack.key': access_key
        }
        driver = webdriver.Remote(
            command_executor='https://hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=desired_cap)
        return driver
        # driver.get("https://www.google.com")
        # if not "Google" in driver.title:
        #     raise Exception("Unable to load google page!")
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("BrowserStack")
        # elem.submit()
        # try:
        #     WebDriverWait(driver, 5).until(EC.title_contains("BrowserStack"))
        #     """
        #     Setting the status of test as 'passed' or 'failed' based on the condition;
        #      if title of the web page starts with 'BrowserStack'
        #      """
        #
        #     driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
        # except TimeoutException:
        #     driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')
        # print(driver.title)
        # driver.quit()
