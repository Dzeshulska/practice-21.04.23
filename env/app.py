from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="Hello world")
driver.implicitly_wait(2.0)
driver.get("http://www.google.com")
time.sleep(10)

