from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Element_state_demo():

    def element_state(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        #username
        username = driver.find_element(By.ID, 'txtUsername')

        username_display_status=username.is_displayed()
        username_enable_status=username.is_enabled()

        if username_display_status== True and username_enable_status==True:
           username.send_keys('Admin')
           print('username typed')
           time.sleep(3)

        else:
           print('element not active. Bug founded')
           driver.close()
           print('bowser closed')

test_obj = Element_state_demo()
test_obj.element_state()