from utilities.seleniumUiActions import SeleniumUIAction
from utilities.globalenums import FindBy


class homepageD:

    # >>>>>>>>>>>>>>>>Locators Initialization <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    bmw_radioBtn_id = "bmwradio"
    bmw_radioBtn_id = "benzradio"
    bmw_radioBtn_id = "hondaradio"
    carselction_drpdwn_id="carselect"
    radio_btn_xpath="//legend[contains(text(),'Radio Button')]/parent::fieldset//label//input[contains(@id,'{0}')]"
    multiple_select_xpath = "//select[@id='multiple-select-example']//option[contains(text(),'{0}')]"
    bmw_check_id = "bmwcheck"
    bmw_check_id = "benzcheck"
    bmw_check_id = "hondacheck"
    open_new_window_btn_id="openwindow"
    open_tab_lnk_xapth="//a[text()='Open Tab']"
    enter_name_txtbox_xpath="//input[@id='name'][contains(@placeholder,'Enter Your Name')]"
    mouse_hover_btn_id="mousehover"
    frame_text_xpath="//h1[contains(text(),'Complete Test Automation Bundle')]"
    frame_id="courses-iframe"
    alert_btn_id="alertbtn"


    """
    Below are action methods
    """

    def verify_frame_text_complete_text_automation_bundle(self):
        print("..............Verifying text inside frame complete automation frame text ..............")
        SeleniumUIAction.SwitchToFrame(FindBy.ID,self.frame_id)
        SeleniumUIAction.IsDisplayed(FindBy.XPATH, self.frame_text_xpath)

    def select_radio_button(self,radioButtonName):
        print("..............Selecting Radio Button .............."+radioButtonName)
        SeleniumUIAction.click_element(FindBy.XPATH, self.radio_btn_xpath.format(radioButtonName))

    def Verify_radio_button_Is_Selected(self, radioButtonName):
        print("..............Verifying  Radio Button ....." + radioButtonName+" is selected")
        SeleniumUIAction.IsSelected(FindBy.XPATH, self.radio_btn_xpath.format(radioButtonName))

    def select_Multiple_Values(self,values_to_select):
        print("..............Selecting Multiple values .............."+values_to_select)
        SeleniumUIAction.clickMultipleElements(FindBy.XPATH, self.multiple_select_xpath.format(values_to_select))

    def select_DropDownClass_example_Text(self,className):
        print(".......Selecting drop value .........."+className)
        SeleniumUIAction.SelectItemByText(FindBy.ID, self.carselction_drpdwn_id,className)

    def EnterValue(self, value_to_enter):
        print(".............Entering value in textbox........."+value_to_enter)
        SeleniumUIAction.Set_textbox_value(FindBy.XPATH, self.enter_name_txtbox_xpath, value_to_enter)

    def select_OpenNewWindow_button(self):
        print("..............Select Open New Window Button ..............")
        SeleniumUIAction.click_element(FindBy.ID, self.open_new_window_btn_id)

    def Is_OpenNewWindow_button_Enabled(self):
        print("..............Verifying Open New Window Button is enabled..............")
        SeleniumUIAction.IsEnabled(FindBy.ID, self.open_new_window_btn_id)

    def Is_OpenNewTab_button_Enabled(self):
        print("..............Verifying Open Tab Button is enabled..............")
        SeleniumUIAction.IsEnabled(FindBy.XPATH, self.open_tab_lnk_xapth)

    def select_OpenTab_button(self):
        print("..............Select Open Tab Button ..............")
        SeleniumUIAction.click_element(FindBy.XPATH, self.open_tab_lnk_xapth)

    def Click_Alert_button(self):
        print(".............Click Alert Button ..............")
        SeleniumUIAction.click_element(FindBy.ID, self.alert_btn_id)

    def WaitForPageLoad(self):
        _Load_Status = SeleniumUIAction.is_page_load_complete(FindBy.ID,self.carselction_drpdwn_id)
        print(_Load_Status)

