from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def allert(self):
        try:
            alert = Alert(self.browser)
            alert.accept()
        except NoAlertPresentException:
            pass

    def get_element(self, locator, timeout=3):
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(locator)
            )

            actions = ActionChains(self.browser)
            actions.move_to_element(element).perform()

            WebDriverWait(self.browser, timeout).until(EC.visibility_of(element))
            return element
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_text_in_element(self, locator, text, timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(locator, text))

    def input_value(self, locator: tuple, text: str):
        element = self.get_element(locator)
        try:
            element.click()
            element.clear()
            for l in text:
                element.send_keys(l)
        except ElementClickInterceptedException:
            self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
            ActionChains(self.browser).move_to_element(element).click().perform()
            element.clear()
            for l in text:
                element.send_keys(l)


    def scroll_to_top(self, timeout=1):
        self.browser.execute_script("window.scrollTo(0, 0);")

        WebDriverWait(self.browser, timeout).until(
            lambda driver: driver.execute_script("return window.pageYOffset") == 0
        )

    def scroll_to_end(self, timeout=1):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                WebDriverWait(self.browser, timeout).until(
                    lambda driver: driver.execute_script("return document.body.scrollHeight") > last_height
                )
                last_height = self.browser.execute_script("return document.body.scrollHeight")
            except:
                break