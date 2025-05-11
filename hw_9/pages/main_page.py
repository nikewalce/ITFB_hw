from pages.base_page import BasePage
from pages.locators.main_page_locators import MainPageLocators as Locator
import allure

class MainPage(BasePage):
    """Главная страница"""
    def click_cameras_button(self):
        self.get_element(Locator.CAMERAS_BUTTON, timeout=1).click()

    def click_my_account_button(self):
        self.get_element(Locator.MY_ACCOUNT_BUTTON, timeout=1).click()

    def click_link_login(self):
        self.get_element(Locator.LINK_LOGIN, timeout=1).click()

    def components_mouseover(self):
        self.mouseover(Locator.COMPONENTS_LINK, timeout=1)

    def click_monitors_link(self):
        self.get_element(Locator.MONITOR_LINK, timeout=1).click()
