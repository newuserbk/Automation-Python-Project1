import pytest


@pytest.mark.usefixtures("oneTimeSetUp")
class RegisterMultipleCoursesTests(object):
    pass

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        # self.courses = RegisterCoursesPage(self.driver)
        # self.ts = TestStatus(self.driver)
        pass
