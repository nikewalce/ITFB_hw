import re

from ..pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage(BasePage):
    INPUT_USERNAME = By.ID, "input-username"
    INPUT_PASSWORD = By.ID, "input-password"
    SUBMIT_BUTTON = By.CSS_SELECTOR, "button[type='submit']"
    MENU_CATALOG = By.ID, "menu-catalog"
    MENU_CATALOG_PRODUCTS = By.LINK_TEXT, "Products"
    ADD_BUTTON = By.XPATH, "//a[@class='btn btn-primary']"
    INPUT_PRODUCT_NAME = By.ID, "input-name-1"
    INPUT_META_TAG_TITLE = By.ID, "input-meta-title-1"
    DATA_PAGE = By.LINK_TEXT, "Data"
    INPUT_MODEL = By.ID, "input-model"
    SEO_PAGE = By.LINK_TEXT, "SEO"
    INPUT_KEYWORD = By.ID, "input-keyword-0-1"
    SAVE_BUTTON = By.CSS_SELECTOR, 'button[form="form-product"]'
    PRODUCTS_COUNT = By.CSS_SELECTOR, 'div.col-sm-6.text-end'
    DELETE_BUTTON = By.CLASS_NAME, "btn.btn-danger"


    def login_to_admin(self, username, password):
        self.input_value(self.INPUT_USERNAME, username)
        self.input_value(self.INPUT_PASSWORD, password)
        return self

    def open_products(self):
        self.get_element(self.MENU_CATALOG_PRODUCTS).click()
        return self.get_product_count()

    def open_catalog(self):
        self.get_element(self.MENU_CATALOG).click()
        self.open_products()
        return self.get_product_count()

    def delete_product(self):
        self.get_element(self.DELETE_BUTTON).click()

    def page_add_new_product(self):
        self.get_element(self.ADD_BUTTON).click()

    def add_new_product(self, product_name, meta_tag_title, model, keyword):
        self.input_value(self.INPUT_PRODUCT_NAME, product_name)
        self.scroll_to_end()
        self.input_value(self.INPUT_META_TAG_TITLE, meta_tag_title)
        self.scroll_to_top()
        self.get_element(self.DATA_PAGE).click()
        self.input_value(self.INPUT_MODEL, model)
        self.get_element(self.SEO_PAGE).click()
        self.input_value(self.INPUT_KEYWORD, keyword)
        self.get_element(self.SAVE_BUTTON).click()

    def click_submit_button(self):
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
        return self

    def get_product_count(self):
        text = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.PRODUCTS_COUNT)
        ).text
        match = re.search(r'of (\d+)', text)
        return int(match.group(1)) if match else None

    def find_element_by_text(self, text):
        locator = (By.XPATH, "//td[text()='AName1']/preceding-sibling::td/input[@type='checkbox']")
        return self.get_element(locator)