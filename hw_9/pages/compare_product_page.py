from pages.base_page import BasePage
from pages.locators.compare_product_locators import CompareProductLocators as Locator
import allure

class CompareProductPage(BasePage):
    def click_remove_htc_button(self):
        self.scroll_to_end(2)
        self.get_element(Locator.REMOVE_HTC_BUTTON, timeout=5).click()

    def click_add_to_cart_iphone(self):
        self.get_element(Locator.ADD_TO_CART_IPHONE_BUTTON, timeout=5).click()
        self.scroll_to_end(2)

    def click_add_to_cart_palm(self):
        self.scroll_to_end(2)
        self.get_element(Locator.ADD_TO_CART_PALM_BUTTON, timeout=5).click()

    def click_shopping_cart_link(self):
        self.scroll_to_top(2)
        self.get_element(Locator.SHOPPING_CART_LINK, timeout=5).click()
