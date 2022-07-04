from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class File_upload():
    def upload_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        print('chrome opened')
        driver.get('https://the-internet.herokuapp.com/upload')
        print('test URL done')

        choose_file_button=driver.find_element(By.ID,'file-upload')
        choose_file_button.send_keys ('C:\\Users\\USER\\Desktop\\Screenshot (308).png')
        time.sleep(3)
        driver.close()


test_obj=File_upload()
test_obj.upload_demo()
