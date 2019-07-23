import unittest
from selenium import webdriver
# import HtmlTestRunner
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()
        x=self.driver.title
        print(x)
        self.assertEqual(x,"Automation step by step - Google Search")

    def test_search_2(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Vinay Mundra")
        self.driver.find_element_by_name("btnK").click()
        x=self.driver.title
        print(x)
        self.assertEqual(x,"Vinay Mundra - Google Search")
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Vinay/PycharmProjects/selenium/reports'))
