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
    driver.maximize_window()
    print('chrome opened')
    driver.get('https://www.gsmarena.com/')
    print('test URL done')



    yield
    driver.close()
    print('test completed. browser closed')

def test_Samsung (browser_config):
    # Samsung
    Samsung = driver.find_element(By.XPATH, '//*[@id="body"]/aside/div[1]/ul/li[1]/a')
    # to keep mouse (cant click)
    actions = ActionChains(driver)
    actions.move_to_element(Samsung).perform().click()
    time.sleep(2)


def test_Apple (browser_config):
    # Apple
    Apple = driver.find_element(By.XPATH, '//*[@id="body"]/aside/div[1]/ul/li[2]/a')
    Apple.click()
    time.sleep(2)

    driver.close()
