import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from Framework.pages.login_page import LoginPage
from Framework.utils import excel_utils


class LoginTest(unittest.TestCase):

    def test_login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)

        # Excel implementation
        file = 'D:\SOFTWARE TEST QA (PEOPLEnTECH)\projects\Test_Automation\Framework\data\login_data.xlsx'
        sheet = 'Sheet1'

        number_of_rows = excel_utils.get_row_count(file, sheet)
        print(number_of_rows)

        for r in range(2, number_of_rows + 1):
            username = excel_utils.read_data(file, sheet, r, 1)
            password = excel_utils.read_data(file, sheet, r, 2)

            lp = LoginPage(driver)
            lp.login_orange(username, password)

        driver.close()
