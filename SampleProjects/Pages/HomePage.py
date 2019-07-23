from SampleProjects.Locators.Locators import Locators

class HomePage:

    def __int__(self, driver):
        self.driver = driver

        self.user_dropdown_id = Locators.user_dropdown_id
        self.logout_button_id = Locators.logout_button_id

    def click_user(self):
        self.driver.find_element_by_id(self.user_dropdown_id).click()

    def click_logout(self):
        self.driver.find_element_by_id(self.logout_button_id).click()
