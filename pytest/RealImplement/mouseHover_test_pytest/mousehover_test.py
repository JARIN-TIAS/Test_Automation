import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


@pytest.fixture()

def browser_config():
    global driver

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    print('browser lunch success')
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/index.php/pim/viewPersonalDetails/empNumber/7')
    print('URL open success')

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

    yield
    driver.close()
    print('test completed. browser closed')

def recruitement_button (browser_config):

     # reqruitment_menu
     reqruitement = driver.find_element(By.XPATH, '//*[@id="menu_recruitment_viewRecruitmentModule"]/b')
     # to keep mouse (cant click)
     actions = ActionChains(driver)
     actions.move_to_element(reqruitement).perform()
     time.sleep(2)

     candidate = driver.find_element(By.LINK_TEXT, 'Candidates')
     candidate.click()
     time.sleep(2.5)

def performance_button (browser_config):
     # perfrormnace
     performance = driver.find_element(By.XPATH, '//*[@id="menu__Performance"]')
     # to keep mouse (cant click)
     actions = ActionChains(driver)
     actions.move_to_element(performance).perform()
     time.sleep(2)

     Employee_trackers = driver.find_element(By.LINK_TEXT, 'Employee Trackers')
     Employee_trackers.click()
     time.sleep(2.5)
