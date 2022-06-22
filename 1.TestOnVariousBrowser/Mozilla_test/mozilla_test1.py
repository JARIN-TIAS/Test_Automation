from selenium import webdriver



class Firefox_config():
    def firefox_test(self):
       driver= webdriver.Firefox(executable_path= "D:\SOFTWARE TEST QA (PEOPLEnTECH)\projects\Test_Automation\BrowserDrivers\geckodriver.exe")


test_obj = Firefox_config()
test_obj.firefox_test()