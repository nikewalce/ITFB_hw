from ..pages.base_page import BasePage
from .locators.main_page_locators import MainPageLocators as Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class MainPage(BasePage):
    """Главная страница"""
    TIMEOUT = 5

    @allure.step('Нажатие на кнопку выбора валюты')
    def click_currency_button(self):
        self.logger.info("Клик по кнопке выбора валюты.")

        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.CURRENCY_BUTTON)
        ).click()

    @allure.step('Выбор валюты фунта')
    def click_pound_option(self):
        self.logger.info("Выбор валюты: фунт стерлингов")

        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.POUND_CURRENCY)
        ).click()

    @allure.step('Выбор валюты евро')
    def click_euro_option(self):
        self.logger.info("Выбор валюты: евро")

        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.EURO_CURRENCY)
        ).click()

    @allure.step('Выбор валюты доллар')
    def click_dollar_option(self):
        self.logger.info("Выбор валюты: доллар")

        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.DOLLAR_CURRENCY)
        ).click()

    @allure.step('Проверка, что текст {text} присутствует в кнопке валюты')
    def text_in_currency_button(self, text):
        self.logger.debug("Проверка текста в кнопке валюты: '%s'", text)

        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.text_to_be_present_in_element(Locator.CURRENCY_TEXT, text)
        )

        self.logger.info("Текст '%s' найден в кнопке валюты.", text)
        return WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.presence_of_element_located(Locator.CURRENCY_TEXT)
        )
