from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Title_verify():

    def title_check(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://www.google.com/')
        actual_title=driver.title
        #case sensitive
        expected_title=('Google')

        if expected_title== actual_title:
            print('google title matched')

        else:
            print("title dint mmatch")



test_obj = Title_verify()
test_obj.title_check()