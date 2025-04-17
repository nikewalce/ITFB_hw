from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
import logging
import allure

class BasePage:
    """Базовый класс"""

    def __init__(self, browser):
        self.browser = browser
        self.logger = getattr(browser, 'logger', self._create_logger())
        self.class_name = type(self).__name__

    def _create_logger(self):
        logger = logging.getLogger("selenium_test_log")

        if not logger.hasHandlers():
            logger.setLevel(logging.DEBUG)

            # Запись в файл
            file_handler = logging.FileHandler("test_hw_7_log.log", mode='a', encoding='utf-8')
            file_handler.setLevel(logging.DEBUG)

            # Формат логов
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger

    def take_screenshot(self):
        """Сделать скриншот страницы и приложить к allure отчету"""
        allure.attach(
            body=self.browser.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )

    def allert(self):
        try:
            alert = Alert(self.browser)
            alert.accept()
            self.logger.info("Алерт принят(закрыт)")
        except NoAlertPresentException:
            self.logger.debug("Нет алерта")

    def scroll_to_top(self, timeout=1):
        self.logger.debug("Скроллинг в самый верх страницы")
        self.browser.execute_script("window.scrollTo(0, 0);")

        WebDriverWait(self.browser, timeout).until(
            lambda driver: driver.execute_script("return window.pageYOffset") == 0
        )
        self.logger.debug("Скроллинг вверх завершен")

    def scroll_to_end(self, timeout=1):
        self.logger.debug("Скроллинг в самый низ страницы")

        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                WebDriverWait(self.browser, timeout).until(
                    lambda driver: driver.execute_script("return document.body.scrollHeight") > last_height
                )
                last_height = self.browser.execute_script("return document.body.scrollHeight")
                self.logger.debug("Прокручено больше, новая высота: %s", last_height)
            except:
                self.logger.debug("Достингнут конец страницы")
                break


    def click_with_scroll(self, locator, timeout=1):
        self.logger.debug("Клик элемента после скроллинга: %s", locator)

        element = WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        try:
            element.click()
            self.logger.info("Элемент нажат: %s", locator)
        except:
            self.logger.warning("Стандартный клик не сработал. Используется JS клик для элемента: %s", locator)
            self.browser.execute_script("arguments[0].click();", element)
