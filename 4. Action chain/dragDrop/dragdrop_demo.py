from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

class DragDrop():
    def drag_drop_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        print('chrome opened')
        driver.get('https://jqueryui.com/droppable/')
        print('test URL done')
        driver.switch_to.frame(0)

        source=driver.find_element(By.ID,'draggable')
        target=driver.find_element(By.ID,'droppable')

        actions=ActionChains(driver)
        actions.drag_and_drop(source,target).perform()
        time.sleep(3)

test_obj= DragDrop()
test_obj.drag_drop_demo()
