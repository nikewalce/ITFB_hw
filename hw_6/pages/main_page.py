from ..pages.base_page import BasePage
from .locators.main_page_locators import MainPageLocators as Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    TIMEOUT = 5

    def click_currency_button(self):
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.CURRENCY_BUTTON)
        ).click()

    def click_pound_option(self):
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.POUND_CURRENCY)
        ).click()

    def click_euro_option(self):
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.EURO_CURRENCY)
        ).click()

    def click_dollar_option(self):
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.DOLLAR_CURRENCY)
        ).click()

    def text_in_currency_button(self, text):
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.text_to_be_present_in_element(Locator.CURRENCY_TEXT, text)
        )
        return WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.presence_of_element_located(Locator.CURRENCY_TEXT)
        )
