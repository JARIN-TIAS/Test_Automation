from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Scroll_demo():
    def scroll(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        print('chrome opened')
        driver.get('https://apple.com')
        print('test URL done')
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        print('test completed successfully')

        time.sleep(5)
        driver.close()

object= Scroll_demo()
object.scroll()