from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
import logging
import allure
from config import Config
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BasePage:
    """Базовый класс"""
    def __init__(self, browser):
        self.browser = browser
        self.config = Config()
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

    def get_element(self, locator, timeout):
        self.logger.info("Получение элемента")
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def text_to_be_present_in_element(self,  locator, text, timeout):
        self.logger.info("Проверка на то, что текст есть в элементе")
        return WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(locator, text))

    def scroll_to_top(self, timeout):
        self.logger.debug("Скроллинг вверх через ActionChains (несколько раз Page Up)")
        actions = ActionChains(self.browser)
        for _ in range(2):
            actions.send_keys(Keys.PAGE_UP).pause(0.2).perform()
        self.logger.debug("Скроллинг вверх завершен")

    def scroll_to_end(self, timeout):
        self.logger.debug("Скроллинг вниз через ActionChains (несколько раз Page Down)")
        actions = ActionChains(self.browser)
        for _ in range(5):
            actions.send_keys(Keys.PAGE_DOWN).pause(0.2).perform()
        self.logger.debug("Скроллинг вниз завершен")

    def click_with_scroll(self, locator, timeout):
        self.logger.debug("Ожидание элемента для клика с прокруткой: %s", locator)
        element = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(self.browser)
        actions.move_to_element(element).pause(0.2).perform()
        element.click()
        self.logger.info("Клик выполнен по элементу: %s", locator)
