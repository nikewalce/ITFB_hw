from ..pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage(BasePage):
    INPUT_FIRSTNAME = By.ID, "input-firstname"
    INPUT_LASTNAME = By.ID, "input-lastname"
    INPUT_EMAIL = By.ID, "input-email"
    INPUT_PASSWORD = By.ID, "input-password"
    CHECKBOX_AGREE = By.NAME, "agree"
    CONTINUE_BUTTON = By.XPATH, "//button[text()='Continue']"

    def enter_firstname(self, firstname):
        self.input_value(self.INPUT_FIRSTNAME, firstname)
        return self

    def enter_lastname(self, lastname):
        self.input_value(self.INPUT_LASTNAME, lastname)
        return self

    def enter_email(self, email):
        self.input_value(self.INPUT_EMAIL, email)
        return self

    def enter_password(self, password):
        self.input_value(self.INPUT_PASSWORD, password)
        return self

    def click_checkbox(self):
        self.get_element(self.CHECKBOX_AGREE).click()
        return self

    def click_continue(self):
        self.get_element(self.CONTINUE_BUTTON).click()
        return self