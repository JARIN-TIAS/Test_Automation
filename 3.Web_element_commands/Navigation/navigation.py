from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Navigation():
    def navigation_check(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')

        #navigate to google
        driver.get('https://www.google.com/')
        time.sleep(3)

        #backToOrangeHRM
        driver.back()
        time.sleep(1)

        #Forward to google
        driver.forward()
        time.sleep(1)

        # backToOrangeHRM
        driver.back()
        time.sleep(2)

        username = driver.find_element(By.ID, 'txtUsername')

        username_display_status = username.is_displayed()
        username_enable_status = username.is_enabled()

        if username_display_status == True and username_enable_status == True:
            username.send_keys('Admin is ABUillaa')
            print('username typed')
            time.sleep(3)

        else:
            print('element not active. Bug founded')

            #refresh
            driver.refresh()

            driver.close()
            print('bowser closed')

testObj= Navigation()
testObj.navigation_check()
