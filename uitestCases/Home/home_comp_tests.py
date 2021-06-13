import time

import pytest
import utilities.cutomLogger as cl
import logging

from pageObjects.HomePage.homepage import homepageD
from testbase import BaseTest
from utilities.genericUtils import OtherUtils as utils
from utilities.seleniumUiActions import SeleniumUIAction


@pytest.mark.usefixtures("oneTimeSetUp")
class TestMultipleHomePageComp(object):
    log = cl.customLogger(logging.DEBUG)
    pass

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.log.info("Visited local class oneTimeSetup")
        self._homepage = homepageD()
        # self.ts = TestStatus(self.driver)
        self._baseTest = BaseTest()

    @pytest.mark.run(order=1)
    @pytest.mark.BVT
    def test_DriverLaunchTest_1(self):
        print("Test-1")
        self.log.error(utils.getTestName() + utils.getCurrentTime())
        # print("Root Directory is : "+utils.get_project_rootDirectory())
        self.log.info("Launching browser from Base Class Global Driver")
        BaseTest.go_to_url(self._baseTest.login_launch_url)
        self._homepage.WaitForPageLoad()
        self.log.info("Verify browser url")
        _Actual_URL = BaseTest.getPageURL()
        assert _Actual_URL == self._baseTest.login_launch_url
        self._homepage.select_radio_button("honda")
        self._homepage.Verify_radio_button_Is_Selected("honda")
        self._homepage.Is_OpenNewTab_button_Enabled()
        self._homepage.Is_OpenNewWindow_button_Enabled()
        self.log.info("Closing browser")
        BaseTest.CloseAllBrowserWindow()

    @pytest.mark.run(order=2)
    @pytest.mark.BVT
    def test_t1invalidLogin_2(self):
        print("Test-2")
        self.log.info("Test-1-Start : test_t1invalidLogin")

    @pytest.mark.run(order=3)
    @pytest.mark.BVT
    def test_t2validLogin_3(self):
        print("Test-3")
        self.log.info("Test-2")
        assert True is True

    @pytest.mark.run(order=4)
    @pytest.mark.BVT
    def test_selectDropDown_4(self):
        print("Test-4")
        self.log.error(utils.getTestName() + utils.getCurrentTime())
        # print("Root Directory is : "+utils.get_project_rootDirectory())
        self.log.info("Launching browser from Base Class Global Driver")
        BaseTest.go_to_url(self._baseTest.login_launch_url)
        self._homepage.WaitForPageLoad()
        self._homepage.select_DropDownClass_example_Text("Honda")
        time.sleep(20)
        self._homepage.select_DropDownClass_example_Text("BMW")

    @pytest.mark.run(order=5)
    @pytest.mark.BVT
    def test_RadioButton_5(self):
        print("Test-5")
        self._homepage.select_radio_button("honda")
        self._homepage.Verify_radio_button_Is_Selected("honda")

    @pytest.mark.run(order=6)
    @pytest.mark.BVT
    def test_DismissAlert_6(self):
        print("Test-6")

    @pytest.mark.run(order=7)
    @pytest.mark.BVT
    def test_selectCheckBox_7(self):
        print("Test-7")

    @pytest.mark.run(order=8)
    @pytest.mark.BVT
    def test_selectMultipleElement_8(self):
        print("Test-8")

    @pytest.mark.run(order=9)
    @pytest.mark.BVT
    def test_OpenNewWindow_VerifyText_9(self):
        print("Test-9")

    @pytest.mark.run(order=10)
    @pytest.mark.BVT
    def test_OpenNewTab_And_VerifyText_10(self):
        print("Test-10")

    @pytest.mark.run(order=11)
    @pytest.mark.BVT
    def test_VerifyFrameText_11(self):
        print("Test-11")
