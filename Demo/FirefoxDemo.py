from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
path="../Drivers/geckodriver.exe"

driver=webdriver.Firefox(executable_path=path)
driver.get("https://google.com")

driver.find_element_by_name("q").send_keys("Automation Step by Step")
#driver.find_element_by_name("btnK").click()
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(2)
print(driver.title)
driver.close()
driver.quit()
