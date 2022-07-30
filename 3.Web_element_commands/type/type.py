from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Type():

    def type_text(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print ('browser lunch success')
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/index.php/pim/viewPersonalDetails/empNumber/7')
        print('URL open success')

        #username
        username = driver.find_element(By.ID, 'txtUsername')
        #password
        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        #login
        login = driver.find_element(By.ID,'btnLogin')

        username.send_keys('Admin')
        password.send_keys('admin123')
        login.click()
        time.sleep(3.5)

        driver.close()
        print('test completed.browser closed')

test_obj = Type()
test_obj.type_text()