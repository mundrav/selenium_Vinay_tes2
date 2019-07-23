from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver=webdriver.Chrome()
chrome_options=Options()
#chrome_options.add_argument("....Headless browser")
#driver=webdriver.chrome(chrome_options=chrome_options)
driver.get("https://www.google.com/")
print(driver.title)
driver.close()
driver.quit()
print("Test Completed")
