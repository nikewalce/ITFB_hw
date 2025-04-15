from ..pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators.register_page_locators import RegisterPageLocators as Locator


class RegisterPage(BasePage):
    TIMEOUT = 5

    def enter_firstname(self):
        firstname = "firstname"

        element = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_FIRSTNAME)
        )
        element.clear()
        element.send_keys(firstname)
        return self

    def enter_lastname(self):
        lastname = "lastname"
        element = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_LASTNAME)
        )
        element.clear()
        element.send_keys(lastname)
        return self

    def enter_email(self):
        email = "11email@example.com"
        element = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_EMAIL)
        )
        element.clear()
        element.send_keys(email)
        return self

    def enter_password(self):
        password = "password"
        element = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_PASSWORD)
        )
        element.clear()
        element.send_keys(password)
        return self

    def click_checkbox(self):
        self.click_with_scroll(Locator.CHECKBOX_AGREE)
        return self

    def click_continue(self):
        self.click_with_scroll(Locator.CONTINUE_BUTTON)
        return self

    def check_created_account(self):
        return WebDriverWait(self.browser, self.TIMEOUT).until(
        EC.presence_of_element_located(Locator.CREATED_ACCOUNT)
    )
