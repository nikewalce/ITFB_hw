import re
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators.admin_page_locators import AdminPageLocators as Locator

class AdminPage(BasePage):

    def login_to_admin(self):
        username = 'admin1'
        password = 'admin'
        self.get_element(Locator.INPUT_USERNAME, timeout=1).send_keys(username)
        self.get_element(Locator.INPUT_PASSWORD, timeout=1).send_keys(password)
        return self

    def open_products(self):
        self.get_element(Locator.MENU_CATALOG_PRODUCTS, timeout=1).click()
        return self.get_product_count()

    def open_catalog(self):
        self.get_element(Locator.MENU_CATALOG, timeout=1).click()
        self.open_products()
        return self.get_product_count()

    def delete_product(self):
        self.get_element(Locator.DELETE_BUTTON, timeout=1).click()

    def page_add_new_product(self):
        self.get_element(Locator.ADD_BUTTON, timeout=1).click()

    def add_new_product(self):
        product_name = "AName1"
        meta_tag_title = "Tag"
        model = "model"
        keyword = "keywordA"
        self.get_element(Locator.INPUT_PRODUCT_NAME, timeout=1).send_keys(product_name)
        self.scroll_to_end(timeout=1)
        self.get_element(Locator.INPUT_META_TAG_TITLE, timeout=1).send_keys(meta_tag_title)
        self.scroll_to_top(timeout=1)
        self.get_element(Locator.DATA_PAGE, timeout=1).click()
        self.get_element(Locator.INPUT_MODEL, timeout=1).send_keys(model)
        self.get_element(Locator.SEO_PAGE, timeout=1).click()
        self.get_element(Locator.INPUT_KEYWORD, timeout=1).send_keys(keyword)
        self.get_element(Locator.SAVE_BUTTON, timeout=1).click()


    def click_submit_button(self):
        self.get_element(Locator.SUBMIT_BUTTON, timeout=1).click()
        return self

    def get_product_count(self):
        text = self.get_element(Locator.PRODUCTS_COUNT, timeout=1).text
        match = re.search(r'of (\d+)', text)
        return int(match.group(1)) if match else None

    def find_element_by_text(self):
        text = "AName1"
        locator = (By.XPATH, f"//td[text()='{text}']/preceding-sibling::td/input[@type='checkbox']")
        return self.get_element(locator, timeout=1)

    def close_handle_alert(self):
        self.allert()
        close_button = self.get_element(Locator.POPUP_BUTTON, timeout=1)
        close_button.click()
        self.allert()  # Закрыть повторный alert, если он появляется
