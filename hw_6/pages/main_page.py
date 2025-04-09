from ..pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    CURRENCY_BUTTON = By.XPATH, "//form[@id='form-currency']"
    POUND_CURRENCY = By.XPATH, "//a[text()='£ Pound Sterling']"
    EURO_CURRENCY = By.XPATH, "//a[text()='€ Euro']"
    DOLLAR_CURRENCY = By.XPATH, "//a[text()='$ US Dollar']"
    CURRENCY_TEXT = By.XPATH, "//strong"

    def click_currency_button(self):
        self.get_element(self.CURRENCY_BUTTON).click()

    def click_pound_option(self):
        self.get_element(self.POUND_CURRENCY).click()

    def click_euro_option(self):
        self.get_element(self.EURO_CURRENCY).click()

    def click_dollar_option(self):
        self.get_element(self.DOLLAR_CURRENCY).click()

    def text_in_currency_button(self, text):
        self.get_text_in_element(self.CURRENCY_TEXT, text)
        return self.get_element(self.CURRENCY_TEXT)
