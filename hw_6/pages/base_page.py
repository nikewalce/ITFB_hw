from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def allert(self):
        try:
            alert = Alert(self.browser)
            alert.accept()
        except NoAlertPresentException:
            pass

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

    def click_with_scroll(self, locator, timeout=1):
        element = WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        try:
            element.click()
        except:
            self.browser.execute_script("arguments[0].click();", element)
