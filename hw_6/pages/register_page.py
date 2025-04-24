from pages.base_page import BasePage
from pages.locators.register_page_locators import RegisterPageLocators as Locator

class RegisterPage(BasePage):

    def enter_firstname(self):
        firstname = "firstname"
        element = self.get_element(Locator.INPUT_FIRSTNAME, timeout=1)
        element.clear()
        element.send_keys(firstname)
        return self

    def enter_lastname(self):
        lastname = "lastname"
        element = self.get_element(Locator.INPUT_LASTNAME, timeout=1)
        element.clear()
        element.send_keys(lastname)
        return self

    def enter_email(self):
        email = "13email@example.com"
        element = self.get_element(Locator.INPUT_EMAIL, timeout=1)
        element.clear()
        element.send_keys(email)
        return self

    def enter_password(self):
        password = "password"
        element = self.get_element(Locator.INPUT_PASSWORD, timeout=1)
        element.clear()
        element.send_keys(password)
        return self

    def click_checkbox(self):
        self.click_with_scroll(Locator.CHECKBOX_AGREE, timeout=2)
        return self

    def click_continue(self):
        self.click_with_scroll(Locator.CONTINUE_BUTTON, timeout=2)
        return self

    def check_created_account(self):
        return self.get_element(Locator.CREATED_ACCOUNT, timeout=2)
