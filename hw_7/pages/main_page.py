from pages.base_page import BasePage
from pages.locators.main_page_locators import MainPageLocators as Locator
import allure

class MainPage(BasePage):
    """Главная страница"""

    @allure.step('Нажатие на кнопку выбора валюты')
    def click_currency_button(self):
        self.logger.info("Клик по кнопке выбора валюты")
        self.get_element(Locator.CURRENCY_BUTTON, timeout=1).click()

    @allure.step('Выбор валюты')
    def select_currency(self, symbol):
        self.logger.info("Выбор валюты по символу: %s", symbol)
        currency_map = {
            "£": Locator.POUND_CURRENCY,
            "€": Locator.EURO_CURRENCY,
            "$": Locator.DOLLAR_CURRENCY
        }
        locator = currency_map.get(symbol)
        if not locator:
            self.logger.error("Неизвестный символ валюты: %s", symbol)
            raise ValueError(f"Unknown currency symbol: {symbol}")
        self.logger.debug("Получен локатор для символа %s: %s", symbol, locator)
        self.get_element(locator, timeout=1).click()
        self.logger.info("Валюта '%s' успешно выбрана", symbol)

    @allure.step('Проверка, что текст {text} присутствует в кнопке валюты')
    def text_in_currency_button(self, text):
        self.logger.debug("Проверка текста в кнопке валюты: '%s'", text)
        self.text_to_be_present_in_element(Locator.CURRENCY_TEXT, text, timeout=1)
        self.logger.info("Текст '%s' найден в кнопке валюты.", text)
        return self.get_element(Locator.CURRENCY_TEXT,timeout=1)
