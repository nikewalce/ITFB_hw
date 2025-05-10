from pages.base_page import BasePage
from pages.locators.checkout_success_page_locators import CheckoutSuccessPageLocators as Locator
import allure

class CheckoutSuccessPage(BasePage):
    def click_my_account_button(self):
        self.scroll_to_top(2)
        self.get_element(Locator.MY_ACCOUNT_LINK, timeout=5).click()

    def click_order_history_button(self):
        self.get_element(Locator.ORDER_HISTORY_LINK, timeout=5).click()
