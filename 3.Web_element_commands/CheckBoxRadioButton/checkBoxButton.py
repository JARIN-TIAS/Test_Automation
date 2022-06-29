from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Checkbox_Radio():
    def checkbox_radio_check(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://demo.opencart.com/index.php?route=account/register&language=en-gb')

        #check_1: Newsletter radio button default 'No'

        newsletter_no= driver.find_element(By.ID, 'input-newsletter-no')
        newsletter_no_actual_status= newsletter_no.is_selected()
        newsletter_no_expected_status= True
        if newsletter_no_expected_status== newsletter_no_actual_status:
           print('default NO is selected')

        else:
            print('default NO unselected. Bug found')

        #   check_2: click Newsletter radio button 'Yes'

        newsletter_yes= driver.find_element(By.ID, 'input - newsletter - yes')
        newsletter_yes.click()


        #   check_3: 'Yes' selected or not

testObj= Checkbox_Radio()
testObj.checkbox_radio_check()