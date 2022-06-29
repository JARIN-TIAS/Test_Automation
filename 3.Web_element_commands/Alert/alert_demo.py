from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Alert(): #3 types of alert (Normal,Confirm, Prompt)
    def alert_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        print('chrome opened')
        driver.get('https://the-internet.herokuapp.com/javascript_alerts')
        print('test URL done')

        #Normal_alert
        normal_alert=driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
        normal_alert.click()
        time.sleep(3)

        #move to alert
        driver.switch_to.alert.accept() #click on OK
        print('Normal alert OK done')


        #confirm_alert
        confirm_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
        confirm_alert.click()
        time.sleep(3)

        # move to alert
        driver.switch_to.alert.dismiss() #click CANCEL
        time.sleep(2)
        print('confirm alert cancel done')


        #prompt_alert
        prompt_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')
        prompt_alert.click()
        time.sleep(3)

        # move to alert
        driver.switch_to.alert.send_keys('test automation by MERAJ')  # typed something in input field
        driver.switch_to.alert.accept()#click on OK
        print("prompt alert typing and clicked 'OK' done")
        time.sleep(2)

        driver.close()


test_Obj = Alert()
test_Obj.alert_demo()