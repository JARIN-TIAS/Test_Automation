import pytest
@pytest.fixture()

def browser_config():
    print ('chrome opened successfully')
    yield
    print('chrome closed successfully')

def test_login_001(browser_config):
    print('login test with valid data')
def test_login_002(browser_config):
    print('login test with invalid info done')

