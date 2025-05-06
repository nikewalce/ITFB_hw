from pages.base_page import BasePage
from pages.locators.register_page_locators import RegisterPageLocators as Locator
import allure

class RegisterPage(BasePage):
    """Страница регистрации"""

    @allure.step('Ввод имени')
    def enter_firstname(self):
        self.logger.info("Ввод имени: %s", self.config.register_firstname)
        element = self.get_element(Locator.INPUT_FIRSTNAME, timeout=1)
        element.clear()
        element.send_keys(self.config.register_firstname)
        return self

    @allure.step('Ввод фамилии')
    def enter_lastname(self):
        self.logger.info("Ввод фамилии: %s", self.config.register_lastname)
        element = self.get_element(Locator.INPUT_LASTNAME, timeout=1)
        element.clear()
        element.send_keys(self.config.register_lastname)
        return self

    @allure.step('Ввод почты')
    def enter_email(self):
        self.logger.info("Ввод email: %s", self.config.register_email)
        element = self.get_element(Locator.INPUT_EMAIL, timeout=1)
        element.clear()
        element.send_keys(self.config.register_email)
        return self

    @allure.step('Ввод пароля')
    def enter_password(self):
        self.logger.info("Ввод пароля")
        element = self.get_element(Locator.INPUT_PASSWORD, timeout=1)
        element.clear()
        element.send_keys(self.config.register_password)
        return self

    @allure.step('Нажимаем на чекбокс согласия с политикой')
    def click_checkbox(self):
        self.logger.info("Клик по чекбоксу согласия с политикой")
        self.click_with_scroll(Locator.CHECKBOX_AGREE, timeout=2)
        return self

    @allure.step('Нажимаем на кнопку Continue')
    def click_continue(self):
        self.logger.info("Клик по кнопке продолжения регистрации")
        self.click_with_scroll(Locator.CONTINUE_BUTTON, timeout=2)
        return self

    @allure.step('Проверяем, что аккаунт создан')
    def check_created_account(self):
        self.logger.info("Проверка, что аккаунт создан")
        return self.get_element(Locator.CREATED_ACCOUNT, timeout=2)
