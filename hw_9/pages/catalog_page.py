from pages.base_page import BasePage
from pages.locators.catalog_page_locators import CatalogPageLocators as Locator
import allure

class CatalogPage(BasePage):
    def click_add_to_cart_canon_e0s5d_button(self):
        self.scroll_to_end(5)
        self.get_element(Locator.ADD_TO_CART_CanonEOS5D_BUTTON, timeout=1).click()

    def click_compare_htc_button(self):
        self.get_element(Locator.COMPARE_HTC_BUTTON, timeout=5).click()
        self.scroll_to_end(3)

    def click_compare_iphone_button(self):
        self.get_element(Locator.COMPARE_IPHONE_BUTTON, timeout=10).click()
        self.scroll_to_end(3)

    def click_compare_palm_button(self):
        self.get_element(Locator.COMPARE_PALM_BUTTON, timeout=10).click()

    @allure.step('Ввод Samsung в поисковой строке')
    def enter_string_in_search(self):
        self.logger.info("Ввод Samsung в поисковой строке")
        element = self.get_element(Locator.SEARCH_INPUT, timeout=1)
        element.clear()
        element.send_keys("Samsung")
        return self

    def click_search_button(self):
        self.get_element(Locator.SEARCH_SPAN, timeout=1).click()

    def click_add_to_wish_list_apple(self):
        self.get_element(Locator.ADD_TO_WISH_LIST_APPLE_BUTTON, timeout=1).click()
        self.scroll_to_end(3)

    def click_add_to_wish_list_samsung(self):
        self.scroll_to_end(3)
        self.get_element(Locator.ADD_TO_WISH_LIST_SAMSUNG_BUTTON, timeout=1).click()

    def click_wish_list(self):
        self.scroll_to_top(3)
        self.get_element(Locator.WISH_LIST_LINK, timeout=1).click()
