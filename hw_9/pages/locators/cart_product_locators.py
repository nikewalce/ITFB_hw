from selenium.webdriver.common.by import By

class CartProductLocators:
    SELECT_AVAILABLE_OPTIONS_DROPDOWN_LIST = (By.XPATH, "//select[@id='input-option-226' and @class='form-select']")
    OPTION_RED = (By.XPATH, "//option[@value='15']")
    INPUT_QTY = (By.XPATH, "//input[@id='input-quantity' and @class='form-control']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@id='button-cart']")
    SHOPPING_CART_BUTTON = (By.XPATH, "//a[@title='Shopping Cart']")
    SUCCESS_ALERT = (By.XPATH, "//button[@data-bs-dismiss='alert']")