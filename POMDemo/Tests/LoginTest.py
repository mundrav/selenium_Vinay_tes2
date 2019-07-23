from selenium import webdriver
import time
import unittest

from POMDemo.Pages.LoginPage import LoginPage
from POMDemo.Pages.HomePage import HomePage


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path='C:/Users/Vinay/PycharmProjects/selenium/Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://kabirmundra-trials65.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("lZK@sO9Md6")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_user()
        time.sleep(10)
        homepage.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
