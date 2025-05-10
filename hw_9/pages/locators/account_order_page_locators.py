from selenium.webdriver.common.by import By

class AccountOrderPageLocators:
    ORDER_CUSTOMER_NAME = (By.XPATH, "//tr/td[2]")
    VIEW_LINK = (By.XPATH, "//a[@data-original-title='View']")
    IPHONE_TD = (By.XPATH, "//td[contains(text(), 'iPhone')]")
    ADDDRESS_INFO = (By.XPATH, "//table[@class='table table-bordered table-hover']//td[text()='Payment Address']/ancestor::table")

