from ..pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators.register_page_locators import RegisterPageLocators as Locator
import allure

class RegisterPage(BasePage):
    """Страница регистрации"""
    TIMEOUT = 5

    @allure.step('Ввод имени')
    def enter_firstname(self):
        firstname = "firstname"
        self.logger.info("Ввод имени: %s", firstname)

        element = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_FIRSTNAME)
        )
        element.clear()
        element.send_keys(firstname)
        return self

    @allure.step('Ввод фамилии')
    def enter_lastname(self):
        lastname = "lastname"
        self.logger.info("Ввод фамилии: %s", lastname)

        element = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_LASTNAME)
        )
        element.clear()
        element.send_keys(lastname)
        return self

    @allure.step('Ввод почты')
    def enter_email(self):
        email = "12email@example.com"
        self.logger.info("Ввод email: %s", email)

        element = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_EMAIL)
        )
        element.clear()
        element.send_keys(email)
        return self

    @allure.step('Ввод пароля')
    def enter_password(self):
        password = "password"
        self.logger.info("Ввод пароля.")

        element = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_PASSWORD)
        )
        element.clear()
        element.send_keys(password)
        return self

    @allure.step('Нажимаем на чекбокс согласия с политикой')
    def click_checkbox(self):
        self.logger.info("Клик по чекбоксу согласия с политикой")

        self.click_with_scroll(Locator.CHECKBOX_AGREE)
        return self

    @allure.step('Нажимаем на кнопку Continue')
    def click_continue(self):
        self.logger.info("Клик по кнопке продолжения регистрации")

        self.click_with_scroll(Locator.CONTINUE_BUTTON)
        return self

    @allure.step('Проверяем, что аккаунт создан')
    def check_created_account(self):
        self.logger.info("Проверка, что аккаунт создан")

        return WebDriverWait(self.browser, self.TIMEOUT).until(
        EC.presence_of_element_located(Locator.CREATED_ACCOUNT)
    )
