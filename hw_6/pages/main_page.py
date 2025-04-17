from pages.base_page import BasePage
from pages.locators.main_page_locators import MainPageLocators as Locator

class MainPage(BasePage):

    def click_currency_button(self):
        self.get_element(Locator.CURRENCY_BUTTON, timeout=1).click()

    def select_currency(self, symbol):
        currency_map = {
            "£": Locator.POUND_CURRENCY,
            "€": Locator.EURO_CURRENCY,
            "$": Locator.DOLLAR_CURRENCY
        }
        locator = currency_map.get(symbol)
        if not locator:
            raise ValueError(f"Unknown currency symbol: {symbol}")
        self.get_element(locator, timeout=1).click()

    def text_in_currency_button(self, text):
        self.text_to_be_present_in_element(Locator.CURRENCY_TEXT, text, timeout=1)
        return self.get_element(Locator.CURRENCY_TEXT,timeout=1)
