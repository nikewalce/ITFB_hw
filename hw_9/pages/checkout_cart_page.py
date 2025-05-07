from pages.base_page import BasePage
from pages.locators.checkout_cart_locators import CheckoutCartLocators as Locator
import allure

class CheckoutCartPage(BasePage):
    def click_checkout_button(self):
        self.get_element(Locator.CHECKOUT_BUTTON, timeout=1).click()

    def click_input_register_account(self):
        self.get_element(Locator.INPUT_REGISTER_ACCOUNT, timeout=1).click()

    def click_button_continue(self):
        self.get_element(Locator.NEW_CUSTOMER_BUTTON_CONTINUE, timeout=3).click()

    @allure.step('Ввод имени')
    def enter_firstname(self):
        self.logger.info("Ввод имени: %s", self.config.register_firstname)
        element = self.get_element(Locator.INPUT_FIRST_NAME, timeout=1)
        element.clear()
        element.send_keys(self.config.register_firstname)
        return self

    @allure.step('Ввод фамилии')
    def enter_lastname(self):
        self.logger.info("Ввод фамилии: %s", self.config.register_lastname)
        element = self.get_element(Locator.INPUT_LAST_NAME, timeout=1)
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

    @allure.step('Ввод телефона')
    def enter_phone(self):
        self.logger.info("Ввод телефона: %s", self.config.register_telephone)
        element = self.get_element(Locator.INPUT_TELEPHONE, timeout=1)
        element.clear()
        element.send_keys(self.config.register_telephone)
        return self

    @allure.step('Ввод адреса 1')
    def enter_shipping_address(self):
        self.logger.info("Ввод адреса 1")
        self.scroll_to_end(1)
        element = self.get_element(Locator.INPUT_SHIPPING_ADDRESS1, timeout=1)
        element.clear()
        element.send_keys(self.config.register_shipping_address1)
        return self

    @allure.step('Ввод города')
    def enter_shipping_city(self):
        self.logger.info("Ввод города")
        element = self.get_element(Locator.INPUT_SHIPPING_CITY, timeout=1)
        element.clear()
        element.send_keys(self.config.register_city)
        return self


    @allure.step('Ввод почтового индекса')
    def enter_shipping_postcode(self):
        self.logger.info("Ввод почтового индекса")
        element = self.get_element(Locator.INPUT_SHIPPING_POSTCODE, timeout=1)
        element.clear()
        element.send_keys(self.config.register_postcode)
        return self

    @allure.step('Выбор страны')
    def select_shipping_county(self):
        self.logger.info("Выбор страны")
        self.get_element(Locator.SELECT_INPUT_SHIPPING_COUNTY, timeout=1).click()
        self.get_element(Locator.OPTION_SHIPPING_COUNTY, timeout=1).click()
        return self


    @allure.step('Выбор региона')
    def select_shipping_region(self):
        self.logger.info("Выбор региона")
        self.get_element(Locator.SELECT_INPUT_SHIPPING_REGION, timeout=1).click()
        self.get_element(Locator.OPTION_SHIPPING_REGION, timeout=1).click()
        return self

    @allure.step('Ввод пароля')
    def enter_password(self):
        self.logger.info("Ввод пароля")
        element = self.get_element(Locator.INPUT_PASSWORD, timeout=1)
        element.clear()
        element.send_keys(self.config.register_password)
        return self

    @allure.step('Ввод подтверждения пароля')
    def enter_password_confirm(self):
        element = self.get_element(Locator.INPUT_PASSWORD_CONFIRM, timeout=1)
        element.clear()
        element.send_keys(self.config.register_password)

    @allure.step('Нажимаем на чекбокс согласия с политикой')
    def click_checkbox(self):
        self.logger.info("Клик по чекбоксу согласия с политикой")
        self.click_with_scroll(Locator.INPUT_REGISTER_AGREE, timeout=2)
        return self

    @allure.step('Нажимаем на кнопку Continue')
    def click_continue(self):
        self.logger.info("Клик по кнопке продолжения регистрации")
        self.click_with_scroll(Locator.CONTINUE_BUTTON, timeout=2)
        return self

    def reload_page(self):
        self.refresh_page()
        self.presence_of_element_located(Locator.FORM_CHECK_LABEL, timeout=2)

    def click_my_account(self):
        self.scroll_to_top(5)
        self.get_element(Locator.MY_ACCOUNT_LINK_DROPDOWN, timeout=1).click()
        self.get_element(Locator.MY_ACCOUNT_LINK, timeout=1).click()

    def click_edit_account_information(self):
        self.get_element(Locator.EDIT_ACCOUNT_INFORMATION_LINK, timeout=1).click()
    # @allure.step('Проверяем, что аккаунт создан')
    # def check_created_account(self):
    #     self.logger.info("Проверка, что аккаунт создан")
    #     return self.get_element(Locator.CREATED_ACCOUNT, timeout=2)
