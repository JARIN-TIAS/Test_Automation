from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
class Elemet_Css():

    def element_css(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/index.php/pim/viewPersonalDetails/empNumber/7')
        #password
        password=driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        if password is not None:
            print ('We found password by CSS')
            time.sleep(3)
        else:
            print('We did not find password by CSS')
        print('this worked properly with CSS')
test_obj = Elemet_Css()
test_obj.element_css()