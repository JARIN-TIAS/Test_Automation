from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Chrome_WDM_config():

    def chrome_wdm_test(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://www.google.com/')
        print('this worked properly')
test_obj = Chrome_WDM_config()
test_obj.chrome_wdm_test()