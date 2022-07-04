from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

class Screenshot_demo():
    def capture_screenshot(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        print('chrome opened')
        driver.get('https://www.google.com/')
        print('test URL done')

        driver.save_screenshot("D:\\SOFTWARE TEST QA (PEOPLEnTECH)\\projects\\Test_Automation\\5. Selenium_advanced\\screenshot\\google.png")
        print('screenshot captured')

        driver.close()
test_obj=Screenshot_demo()
test_obj.capture_screenshot()