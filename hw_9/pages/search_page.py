from pages.base_page import BasePage
from pages.locators.search_page_locators import SearchPageLocators as Locator
import allure

class SearchPage(BasePage):
    def click_samsung_compare(self):
        self.get_element(Locator.COMPARE_SAMSUNG_BUTTON, timeout=1).click()

    def click_total_compare_link(self):
        self.get_element(Locator.COMPARE_TOTAL_LINK, timeout=1).click()