from selenium.webdriver.common.by import By

class MainPageLocators:
    CURRENCY_BUTTON = (By.XPATH, "//form[@id='form-currency']")
    POUND_CURRENCY = (By.XPATH, "//a[text()='£ Pound Sterling']")
    EURO_CURRENCY = (By.XPATH, "//a[text()='€ Euro']")
    DOLLAR_CURRENCY = (By.XPATH, "//a[text()='$ US Dollar']")
    CURRENCY_TEXT = (By.XPATH, "//strong")