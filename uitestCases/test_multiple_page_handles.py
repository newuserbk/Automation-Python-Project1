import time
import unittest

from selenium import webdriver

import Driver
from utilities import keyboarduiactions, pdfutilities
from utilities.otherutilities import Other_Utilities
from utilities.readproperties import ReadConfig


class Test_Login(unittest.TestCase):
    url = 'https://www.incometaxindiaefiling.gov.in/home'
    phone = ReadConfig.getUserPhone()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    min_wait = ReadConfig.add_min_sleep()
    max_wait = ReadConfig.add_max_sleep()
    guid_value = Other_Utilities.generate_random_string()

    def setUp(self):
        Driver.Initialize()


    def tearDown(self):
        Driver.CloseDriver()

    def test_switch_window_and_download_pdf(self):
        download_dir = "C:\\Users"
        options = webdriver.ChromeOptions()
        root_path = Other_Utilities.get_project_root_path()
        print("Root Project path : " + root_path)
        profile = {"plugins.plugins_list": [{"enabled": False,
                                             "name": "Chrome PDF Viewer"}],
                   # Disable Chrome's PDF Viewer
                   "download.default_directory": download_dir,
                   "download.extensions_to_open": "applications/pdf",
                   "download.prompt_for_download": False,  # To auto download the file
                   "download.directory_upgrade": True,
                   "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
                   }
        options.add_experimental_option("prefs", profile)
        driver = webdriver.Chrome('C:/Personal Doc/Returns Team/Selenium Drivers/chromedriver.exe',
                                  chrome_options=options)  # Optional argument, if not specified will search path.

        print("Downloading PDF")
        get_pdf_url = ""
        driver.get('https://www.incometaxindiaefiling.gov.in/eFiling/Portal/StaticPDF/ITD_CALENDER_2021_final%20JANUARY2.pdf')
        print("Saving  PDF")
        # KeyBoardActions.PressEnter()
        print("Opened new window")
        print("Downloading PDF")
        print("Download Completed")
        print("Reading PDF")
        pdf_path="C:/Users/bharat.kodalkar/Downloads/ITD_CALENDER_2021_final JANUARY2.pdf"
        # pdfutilities.PDFUtilities.read_pdf_content_of_page(pdf_path,1)
        page_count= pdfutilities.PDFUtilities.get_count_of_pdf_pages(pdf_path)
        print("Page Count is : "+page_count)





