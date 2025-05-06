import re
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators.admin_page_locators import AdminPageLocators as Locator
import allure

class AdminPage(BasePage):
    """Страница панели администратора"""

    @allure.step('Ввод логина и пароля')
    def login_to_admin(self):
        self.logger.info("Авторизация в админку с логином: %s, паролем: %s", self.config.username, self.config.password)
        """Ввод логина"""
        self.get_element(Locator.INPUT_USERNAME, timeout=1).send_keys(self.config.username)
        """Ввод пароля"""
        self.get_element(Locator.INPUT_PASSWORD, timeout=1).send_keys(self.config.password)
        self.logger.debug("Введены логин и пароль.")
        return self

    @allure.step('Открытие страницы Products')
    def open_products(self):
        self.logger.info("Открытие страницы 'Products'")
        self.get_element(Locator.MENU_CATALOG_PRODUCTS, timeout=1).click()
        return self.get_product_count()

    @allure.step('Открытие меню Catalog')
    def open_catalog(self):
        self.logger.info("Открытие меню 'Catalog'")
        self.get_element(Locator.MENU_CATALOG, timeout=1).click()
        self.open_products()
        return self.get_product_count()

    @allure.step("Удаление продукта")
    def delete_product(self):
        self.logger.info("Удаление продукта")
        """Нажимаем на кнопку удалить"""
        self.get_element(Locator.DELETE_BUTTON, timeout=1).click()

    @allure.step("Переход на страницу добавления нового продукта")
    def page_add_new_product(self):
        self.logger.info("Переход на страницу добавления нового продукта")
        """Нажимаем на кнопку добавить"""
        self.get_element(Locator.ADD_BUTTON, timeout=1).click()

    @allure.step("Добавляем новый продукт")
    def add_new_product(self):
        self.logger.info("Добавление нового продукта: %s", self.config.product_name)
        """Ввод названия продукта"""
        self.get_element(Locator.INPUT_PRODUCT_NAME, timeout=1).send_keys(self.config.product_name)
        self.scroll_to_end(timeout=1)
        """Ввод мета-тэга"""
        self.get_element(Locator.INPUT_META_TAG_TITLE, timeout=1).send_keys(self.config.meta_tag_title)
        self.scroll_to_top(timeout=1)
        """Переход на страницу Data"""
        self.get_element(Locator.DATA_PAGE, timeout=1).click()
        """Ввод названия модели"""
        self.get_element(Locator.INPUT_MODEL, timeout=1).send_keys(self.config.model)
        """Переход на страницу СЕО"""
        self.get_element(Locator.SEO_PAGE, timeout=1).click()
        """Добавление ключевого слова"""
        self.get_element(Locator.INPUT_KEYWORD, timeout=1).send_keys(self.config.keyword)
        """Нажимаем на кнопку сохранения"""
        self.get_element(Locator.SAVE_BUTTON, timeout=1).click()
        self.logger.info("Продукт успешно добавлен.")

    @allure.step("Нажатие на кнопку Submit")
    def click_submit_button(self):
        self.logger.info("Нажатие на кнопку 'Submit'")
        self.get_element(Locator.SUBMIT_BUTTON, timeout=1).click()
        return self

    @allure.step("Получения количества продуктов")
    def get_product_count(self):
        self.logger.debug("Получение количества продуктов")
        """Находим текст с количеством продуктов"""
        text = self.get_element(Locator.PRODUCTS_COUNT, timeout=1).text
        match = re.search(r'of (\d+)', text)
        count = int(match.group(1)) if match else None
        self.logger.info("Найдено продуктов: %s", count)
        return count

    @allure.step("Находим элемент по тексту")
    def find_element_by_text(self):
        text = "AName1"
        locator = (By.XPATH, f"//td[text()='{text}']/preceding-sibling::td/input[@type='checkbox']")
        self.logger.info("Поиск элемента по тексту: %s", text)
        return self.get_element(locator, timeout=1)

    @allure.step("Обрабатываем алерты")
    def close_handle_alert(self):
        self.logger.info("Обработка всплывающих окон (alert)")
        self.allert()
        close_button = self.get_element(Locator.POPUP_BUTTON, timeout=1)
        close_button.click()
        self.logger.debug("Аллерт закрыт")
        self.allert()  # Закрыть повторный alert, если он появляется
