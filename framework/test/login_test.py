import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from framework.pages.login_page import Login_page


class LoginTest (unittest.TestCase):

    def test_valid_login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        time.sleep(3)

        lp=Login_page(driver)
        lp.login_orange('Admin', 'admin123')

        driver.close()

    def test_invalid_login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        time.sleep(3)

        lp = Login_page(driver)
        lp.login_orange('Admin alom', 'admin15523')

        driver.close()