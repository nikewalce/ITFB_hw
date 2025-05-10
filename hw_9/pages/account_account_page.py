from pages.base_page import BasePage
from pages.locators.account_account_locators import AccountAccountLocators as Locator
import allure

class AccountAccountPage(BasePage):
    def click_edit_account_information(self):
        self.get_element(Locator.EDIT_ACCOUNT_INFORMATION_LINK, timeout=1).click()

    def click_PhonesAndPDAs(self):
        self.get_element(Locator.PHONESANDPDAS_LINK, timeout=1).click()
