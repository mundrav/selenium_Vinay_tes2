from selenium import webdriver
import time
# from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
# from webdriver_manager.firefox import GeckoDriverManager
# driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://google.com")

# SearchBox=driver.find_element_by_name("q")

# SearchBox.send_keys("Vinay")
# driver.find_element_by_name("q").send_keys("Automation Step by Step")
xyz=driver.find_elements_by_xpath("//input[@name='q'']")
xyz.

#driver.find_element_by_name("btnK").click()
# driver.find_element_by_name("btnK").click()
time.sleep(2)
print(driver.title)
driver.close()
driver.quit()