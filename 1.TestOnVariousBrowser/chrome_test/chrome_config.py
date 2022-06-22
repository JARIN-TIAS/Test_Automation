from selenium import webdriver

class Chrome_config():
       def chrome_test(self):
           driver = webdriver.Firefox(executable_path= "D:\SOFTWARE TEST QA (PEOPLEnTECH)\projects\Test_Automation\BrowserDrivers\chromedriver.exe")

test_obj= Chrome_config()
test_obj.chrome_test()