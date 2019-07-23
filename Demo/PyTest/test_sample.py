from selenium import webdriver

def test_setup():
    global driver
    driver = webdriver.Chrome(
        executable_path='C:/Users/Vinay/PycharmProjects/selenium/Drivers/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_login():
    driver.get("https://kabirmundra-trials65.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("lZK@sO9Md6")
    driver.find_element_by_id("btnLogin").click()

def test_teardown():
    driver.close()
    driver.quit()
    print("Test completed ")



