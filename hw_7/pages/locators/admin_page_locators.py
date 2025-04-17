from selenium.webdriver.common.by import By

class AdminPageLocators:
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
    POPUP_BUTTON = By.CLASS_NAME, 'btn-close'
