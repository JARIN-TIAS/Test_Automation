from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class ElemetId():

    def element_locator(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/index.php/pim/viewPersonalDetails/empNumber/7')
        #username
        username=driver.find_element(By.ID, 'frmLogin')
        if username is not None:
            print ('We found usename by ID')
        else:
            print('We did not find username by ID')
        print('this worked properly')
test_obj = ElemetId()
test_obj.element_locator()