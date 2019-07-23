class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.user_dropdown_id = "user-dropdown"
        self.logout_button_id = "logoutLink"

    def click_user(self):
        self.driver.find_element_by_id(self.user_dropdown_id).click()

    def click_logout(self):
        self.driver.find_element_by_id(self.logout_button_id).click()
