import time

from selenium.webdriver.common.by import By

class Login_page():
    def __int__(self, driver):
        self.driver=  driver

    def login_orange(self, username, password):
        user_name_field= self.driver.find_element(By.ID, 'frmLogin')
        user_name_field.clear()
        user_name_field.send_keys(username)
        time.sleep(3)

        password_name_field= self.driver.find_element(By.ID, 'txtPassword')
        password_name_field.clear()
        password_name_field.send_keys(password)
        time.sleep(3)

        login_button= self.driver.find_element(By.ID, 'btnLogin')
        login_button.click()
        time.sleep(3)