from pages.locators.account_login_locators import AccountLoginPageLocators as Locator
from pages.base_page import BasePage
import allure

class AccountLoginPage(BasePage):
    """Страница логина"""
    @allure.step('Ввод email')
    def enter_email(self):
        self.logger.info("Ввод email: %s", self.config.register_email)
        element = self.get_element(Locator.EMAIL_INPUT, timeout=1)
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

    def click_login_button(self):
        self.get_element(Locator.LOGIN_INPUT, timeout=1).click()
