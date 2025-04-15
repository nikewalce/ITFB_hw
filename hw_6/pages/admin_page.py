import re
from ..pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators.admin_page_locators import AdminPageLocators as Locator

class AdminPage(BasePage):
    TIMEOUT = 5

    def login_to_admin(self):
        username = 'admin1'
        password = 'admin'

        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_USERNAME)
        ).send_keys(username)

        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_PASSWORD)
        ).send_keys(password)
        return self

    def open_products(self):
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.MENU_CATALOG_PRODUCTS)
        ).click()
        return self.get_product_count()

    def open_catalog(self):
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.MENU_CATALOG)
        ).click()
        self.open_products()
        return self.get_product_count()

    def delete_product(self):
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.DELETE_BUTTON)
        ).click()

    def page_add_new_product(self):
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.ADD_BUTTON)
        ).click()

    def add_new_product(self):
        product_name = "AName1"
        meta_tag_title = "Tag"
        model = "model"
        keyword = "keywordA"

        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_PRODUCT_NAME)
        ).send_keys(product_name)

        self.scroll_to_end()

        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_META_TAG_TITLE)
        ).send_keys(meta_tag_title)

        self.scroll_to_top()

        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.DATA_PAGE)
        ).click()

        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_MODEL)
        ).send_keys(model)

        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.SEO_PAGE)
        ).click()

        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_KEYWORD)
        ).send_keys(keyword)

        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.SAVE_BUTTON)
        ).click()


    def click_submit_button(self):
        WebDriverWait(self.browser, self.TIMEOUT).until(EC.element_to_be_clickable(Locator.SUBMIT_BUTTON)).click()
        return self

    def get_product_count(self):
        text = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(Locator.PRODUCTS_COUNT)
        ).text
        match = re.search(r'of (\d+)', text)
        return int(match.group(1)) if match else None

    def find_element_by_text(self):
        text = "AName1"
        locator = (By.XPATH, f"//td[text()='{text}']/preceding-sibling::td/input[@type='checkbox']")
        return WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.presence_of_element_located(locator)
        )

    def handle_alert(self):
        self.allert()
        close_button = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.POPUP_BUTTON)
        )
        close_button.click()
        self.allert()  # Закрыть повторный alert, если он появляется
