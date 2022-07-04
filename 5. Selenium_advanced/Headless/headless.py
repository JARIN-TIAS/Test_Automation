from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Headless():
    def headless_demo(self):
        options=webdriver.ChromeOptions()
        options.headless= True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.maximize_window()
        print('chrome opened')
        driver.get('https://www.google.com/')
        print(driver.title)
        print('test done')

        driver.close()

test_obj=Headless()
test_obj.headless_demo()
