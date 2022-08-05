import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from framework.pages.login_page import Login_page
from framework.utils import excel_utils


class LoginTest (unittest.TestCase):

    def test_login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        time.sleep(3)

        #excel implement
        data_file='D:\SOFTWARE TEST QA (PEOPLEnTECH)\projects\Test_Automation\framework\data\login_data.xlsx'
        sheet_name= 'Sheet1'

        number_of_rows= excel_utils.get_row_count(data_file, sheet_name)
        print(number_of_rows)

        for r in range (2, number_of_rows+1):
            email=excel_utils.read_data(data_file, sheet_name, r, 1)
            password= excel_utils.read_data(data_file, sheet_name,r ,2)

            lp = Login_page(driver)
            lp.login_orange(email, password)

        #number_of_coloumn= excel_utils.get_column_count()
        driver.close()