import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@pytest.fixture()

def browser_config():
    global driver

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    print('browser lunch success')
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/index.php/pim/viewPersonalDetails/empNumber/7')
    print('URL open success')

    yield
    driver.close()
    print('test completed.browser closed')

def test_login_valid (browser_config):
    # username
    username = driver.find_element(By.ID, 'txtUsername')
    # password
    password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
    # login
    login = driver.find_element(By.ID, 'btnLogin')

    username.send_keys('Admin')
    password.send_keys('admin123')
    login.click()
    time.sleep(3.5)

def test_login_invalid (browser_config):
    # username
    username = driver.find_element(By.ID, 'txtUsername')
    # password
    password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
    # login
    login = driver.find_element(By.ID, 'btnLogin')

    username.send_keys('Adminpoop')
    password.send_keys('admin123pee')
    login.click()
    time.sleep(3.5)

