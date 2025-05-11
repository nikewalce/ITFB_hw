from pages.base_page import BasePage
from pages.locators.account_order_page_locators import AccountOrderPageLocators as Locator
import allure

class AccountOrderPage(BasePage):
    def click_view_button(self):
        self.get_element(Locator.VIEW_LINK, timeout=1).click()

    def click_return_link(self):
        self.get_element(Locator.RETURN_LINK, timeout=1).click()

    def enter_telephone(self):
        telephone = '12345678910'
        telephone_input = self.get_element(Locator.INPUT_TELEPHONE, timeout=1)
        telephone_input.clear()
        telephone_input.send_keys(telephone)

    def click_reason_for_return_checkbox(self):
        self.get_element(Locator.REASON_FOR_RETURN_CHECKBOX, timeout=1).click()

    def click_submit_button(self):
        self.get_element(Locator.SUBMIT_RETURN_BUTTON, timeout=1).click()

    def check_customer_info(self):
        self.get_element(Locator.VIEW_LINK, timeout=1).click()
        product_name = self.get_element(Locator.IPHONE_TD, timeout=1).text
        address_info = self.get_element(Locator.ADDDRESS_INFO, timeout=1).text
        return (product_name == "iPhone") and (self.config.register_firstname in address_info) and (self.config.register_city in address_info)