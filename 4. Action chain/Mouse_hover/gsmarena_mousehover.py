from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

class gsmreana_hovering():
    def gsmarena_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        print('chrome opened')
        driver.get('https://www.gsmarena.com/')
        print('test URL done')



        #Samsung
        Samsung= driver.find_element(By.XPATH,'//*[@id="body"]/aside/div[1]/ul/li[1]/a')
        #to keep mouse (cant click)
        actions = ActionChains(driver)
        actions.move_to_element(Samsung).perform()
        time.sleep(2)

        #Apple
        Apple= driver.find_element(By.XPATH,'//*[@id="body"]/aside/div[1]/ul/li[2]/a')
        Apple.click()
        time.sleep(2)

        driver.close()
        print('test completed')

test_obj= gsmreana_hovering()
test_obj.gsmarena_demo()