import pytest
import utilities.cutomLogger as cl
import logging
from pageObjects.HomePage.homepage import homepageD
from testbase import BaseTest
from utilities.genericUtils import OtherUtils as utils


@pytest.mark.usefixtures("oneTimeSetUp")
class TestRegisterMultipleCourses(object):
    log = cl.customLogger(logging.DEBUG)
    pass

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.log.info("Visited local class oneTimeSetup")
        self._homepage = homepageD()
        # self.ts = TestStatus(self.driver)
        self._baseTest = BaseTest()

    @pytest.mark.run(order=12)
    @pytest.mark.BVT
    def test_class2_1(self):
        print("Test-15")
        self.log.error(utils.getTestName() + utils.getCurrentTime())
        # print("Root Directory is : "+utils.get_project_rootDirectory())
        self.log.info("Launching browser from Base Class Global Driver")
        BaseTest.go_to_url('https://courses.letskodeit.com/')
        # self._homepage.WaitForPageLoad()
        self.log.info("Verify browser url")
        _Actual_URL = BaseTest.getPageURL()
        assert _Actual_URL == 'https://courses.letskodeit.com/'
        # self._baseTest.CloseAllBrowserWindow()

    @pytest.mark.run(order=13)
    @pytest.mark.BVT
    def test_class2_2(self):
        print("Test-16")
        self.log.error(utils.getTestName() + utils.getCurrentTime())
        # print("Root Directory is : "+utils.get_project_rootDirectory())
        self.log.info("Launching browser from Base Class Global Driver")
        BaseTest.go_to_url('https://courses.letskodeit.com/courses')
        # self._homepage.WaitForPageLoad()
        self.log.info("Verify browser url")
        _Actual_URL = BaseTest.getPageURL()
        assert _Actual_URL == 'https://courses.letskodeit.com/courses'
        self._baseTest.CloseAllBrowserWindow()
