from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

class Mouse_hovering():
    def mouseHover_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        print('chrome opened')
        driver.get('https://opensource-demo.orangehrmlive.com/')
        print('test URL done')

        # username
        username = driver.find_element(By.ID, 'txtUsername')
        # password
        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        # login
        login = driver.find_element(By.ID, 'btnLogin')

        username.send_keys('Admin')
        password.send_keys('admin123')
        login.click()
        time.sleep(2.5)

        #reqruitment_menu
        reqruittment= driver.find_element(By.XPATH,'//*[@id="menu_recruitment_viewRecruitmentModule"]/b')
        #to keep mouse (cant click)
        actions = ActionChains(driver)
        actions.move_to_element(reqruittment).perform()
        time.sleep(2)

        candidate= driver.find_element(By.LINK_TEXT,'Candidates')
        candidate.click()
        time.sleep(2.5)


test_obj= Mouse_hovering()
test_obj.mouseHover_demo()
