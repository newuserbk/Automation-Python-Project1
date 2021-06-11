import time

import pytest
import utilities.cutomLogger as cl
import logging

from testbase import BaseTest
from utilities.genericUtils import OtherUtils as utils


@pytest.mark.usefixtures("oneTimeSetUp")
class TestMultipleHomePageComp(object):
    log = cl.customLogger(logging.DEBUG)
    pass

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.log.info("Visited local class oneTimeSetup")
        # self.courses = RegisterCoursesPage(self.driver)
        # self.ts = TestStatus(self.driver)
        self._baseTest=BaseTest()

    @pytest.mark.run(order=1)
    @pytest.mark.BVT
    def test_DriverLaunchTest_1(self):
        self.log.error(utils.getTestName() +utils.getCurrentTime())
        # print("Root Directory is : "+utils.get_project_rootDirectory())
        self.log.info("Launching browser from Base Class Global Driver")
        BaseTest.go_to_url(self._baseTest.login_launch_url)
        time.sleep(5)
        self.log.info("Verify browser url")
        actualURL=BaseTest.getPageURL()
        assert actualURL==self._baseTest.login_launch_url
        self.log.info("Closing browser")
        BaseTest.CloseAllBrowserWindow()

    @pytest.mark.run(order=2)
    @pytest.mark.BVT
    def test_t1invalidLogin_2(self):
        self.log.info("Test-1-Start : test_t1invalidLogin")
        self.log.info("Launching browser from Base Class Global Driver")
        BaseTest.go_to_url(BaseTest.login_launch_url)
        self.log.info("Closing browser")
        BaseTest.CloseAllBrowserWindow()

    @pytest.mark.run(order=3)
    @pytest.mark.BVT
    def test_t2validLogin_3(self):
        print("Test-2")
        self.log.info("Test-2")
        self.log.info("test_t2validLogin")
        self.log.info("*#" * 20)
        self.log.info("test_t1invalidLogin started")
        self.log.info("*#" * 20)
        assert True is True
