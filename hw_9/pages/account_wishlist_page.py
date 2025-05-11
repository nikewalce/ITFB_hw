from pages.base_page import BasePage
from pages.locators.account_wishlist_page_locators import AccountWishlistPageLocators as Locator
import allure

class AccountWishlistPage(BasePage):
    def click_add_to_cart_apple_button(self):
        self.get_element(Locator.ADD_TO_CART_APPLE_BUTTON, timeout=1).click()
