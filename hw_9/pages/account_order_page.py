from pages.base_page import BasePage
from pages.locators.account_order_page_locators import AccountOrderPageLocators as Locator
import allure

class AccountOrderPage(BasePage):
    def check_customer_info(self):
        self.get_element(Locator.VIEW_LINK, timeout=1).click()
        product_name = self.get_element(Locator.IPHONE_TD, timeout=1).text
        address_info = self.get_element(Locator.ADDDRESS_INFO, timeout=1).text
        return (product_name == "iPhone") and (self.config.register_firstname in address_info) and (self.config.register_city in address_info)