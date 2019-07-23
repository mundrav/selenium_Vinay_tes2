from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
#implict wait

# driver.implicitly_wait(1)

driver.get("https://google.com/")
driver.find_element_by_name("q").send_keys("Automation")

wait=WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable((By.NAME,"btnK")))
print("Element is clickable")
driver.find_element_by_name("btnK").click()

print("Test Completed")
driver.close()
driver.quit()

