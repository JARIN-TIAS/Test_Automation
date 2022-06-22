from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
class Elemet_link_text():

    def element_link_text(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/index.php/pim/viewPersonalDetails/empNumber/7')
        #forgot_password
        forgot_password=driver.find_element(By.LINK_TEXT, 'Forgot your password?')
        if forgot_password is not None:
            print ('We found password by linkText')
            forgot_password.click()
            time.sleep(5)
        else:
            print('We did not find password by linkText')
        print('this worked properly with linkText')
test_obj = Elemet_link_text()
test_obj.element_link_text()