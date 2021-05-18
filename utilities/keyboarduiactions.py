from selenium.webdriver import ActionChains


# import KEYS
from selenium.webdriver.common.keys import Keys

import Driver
from testbase import BaseTest


class KeyBoardActions(BaseTest):

    @staticmethod
    def PressKey():
        # create action chain object
        action = ActionChains(Driver.Instance)
        # perform the operation
        action.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()

    @staticmethod
    def PressTab():
        KeyBoardActions.PressKey(Keys.TAB)

    @staticmethod
    def PressEscKey():
        KeyBoardActions.PressKey(Keys.ESCAPE)

    @staticmethod
    def PressEnter():
        KeyBoardActions.PressKey(Keys.ENTER)

    @staticmethod
    def PressUpKey():
        KeyBoardActions.PressKey(Keys.ARROW_UP)

    @staticmethod
    def PressDownKey():
        KeyBoardActions.PressKey(Keys.ARROW_DOWN)

    @staticmethod
    def PressDeleteKey():
        KeyBoardActions.PressKey(Keys.DELETE)



