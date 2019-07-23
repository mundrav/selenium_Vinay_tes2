from selenium import webdriver
import time
import unittest
import HtmlTestRunner

# test comment vinay
# To run from commnad line when content in different folder i.e Page Object model
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from SampleProjects.Pages.LoginPage import LoginPage
from SampleProjects.Pages.HomePage import HomePage


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path='C:/Users/Vinay/PycharmProjects/selenium/Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://kabirmundra-trials65.orangehrmlive.com/")

        login = LoginPage()
        login.__int__(driver)
        login.enter_username("Admin")
        login.enter_password("lZK@sO9Md6")
        login.click_login()

        homepage = HomePage()
        homepage.__int__(driver)
        homepage.click_user()
        homepage.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("TestCompleted")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner("C:/Users/Vinay/PycharmProjects/selenium/reports"))
