from selenium.webdriver.common.by import By

class RegisterPageLocators:
    INPUT_FIRSTNAME = By.ID, "input-firstname"
    INPUT_LASTNAME = By.ID, "input-lastname"
    INPUT_EMAIL = By.ID, "input-email"
    INPUT_PASSWORD = By.ID, "input-password"
    CHECKBOX_AGREE = By.NAME, "agree"
    CONTINUE_BUTTON = By.XPATH, "//button[text()='Continue']"
    CREATED_ACCOUNT = By.XPATH, "//h1[text()='Your Account Has Been Created!']"