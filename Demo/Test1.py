import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("Automation Step by Step")
time.sleep(3)
driver.find_element_by_name("btnK").click()
driver.maximize_window()
time.sleep(3)

driver.close()


driver.quit()
print("Test Completed")
