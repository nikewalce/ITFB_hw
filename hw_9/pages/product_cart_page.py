from pages.base_page import BasePage
from pages.locators.cart_product_locators import CartProductLocators as Locator
import allure

class ProductCartPage(BasePage):
    def click_select_available_options_dropdown_button(self):
        self.scroll_to_end(2)
        self.get_element(Locator.SELECT_AVAILABLE_OPTIONS_DROPDOWN_LIST, timeout=1).click()
        self.get_element(Locator.OPTION_RED, timeout=1).click()

    def qty_entry(self):
        qty = 2
        element = self.get_element(Locator.INPUT_QTY, timeout=1)
        element.clear()
        element.send_keys(qty)

    def click_add_to_cart_button(self):
        self.get_element(Locator.ADD_TO_CART_BUTTON, timeout=1).click()

    def click_shopping_cart(self):
        self.scroll_to_top(3)
        self.get_element(Locator.SHOPPING_CART_BUTTON, timeout=1).click()

    def close_success_alert(self):
        self.get_element(Locator.SUCCESS_ALERT, timeout=1).click()
