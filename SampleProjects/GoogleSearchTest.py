from selenium import webdriver
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation")
        self.driver.find_element_by_name("btnK").click()
        print(self.driver.title)

    def test_search_kapil(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Vinay Mundra")
        self.driver.find_element_by_name("btnK").click()
        print(self.driver.title)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Vinay/PycharmProjects/selenium/reports"))



