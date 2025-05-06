from pages.base_page import BasePage
from pages.locators.cameras_catalog_page_locators import CamerasCatalogPageLocators as Locator
import allure

class CamerasCatalogPage(BasePage):
    def click_add_to_cart_canon_e0s5d_button(self):
        self.scroll_to_end(5)
        self.get_element(Locator.ADD_TO_CART_CanonEOS5D_BUTTON, timeout=1).click()
