import re
from ..pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators.admin_page_locators import AdminPageLocators as Locator
import allure

class AdminPage(BasePage):
    """Страница панели администратора"""
    TIMEOUT = 5

    @allure.step('Ввод логина и пароля')
    def login_to_admin(self):
        username = 'admin1'
        password = 'admin'

        self.logger.info("Авторизация в админку с логином: %s, паролем: %s", username, password)
        """Ввод логина"""
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_USERNAME)
        ).send_keys(username)
        """Ввод пароля"""
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_PASSWORD)
        ).send_keys(password)

        self.logger.debug("Введены логин и пароль.")

        return self

    @allure.step('Открытие страницы Products')
    def open_products(self):
        self.logger.info("Открытие страницы 'Products'")

        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.MENU_CATALOG_PRODUCTS)
        ).click()
        return self.get_product_count()

    @allure.step('Открытие меню Catalog')
    def open_catalog(self):
        self.logger.info("Открытие меню 'Catalog'")

        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.MENU_CATALOG)
        ).click()
        self.open_products()
        return self.get_product_count()

    @allure.step("Удаление продукта")
    def delete_product(self):
        self.logger.info("Удаление продукта")

        """Нажимаем на кнопку удалить"""
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.DELETE_BUTTON)
        ).click()

    @allure.step("Переход на страницу добавления нового продукта")
    def page_add_new_product(self):
        self.logger.info("Переход на страницу добавления нового продукта")
        """Нажимаем на кнопку добавить"""
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.ADD_BUTTON)
        ).click()

    @allure.step("Добавляем новый продукт")
    def add_new_product(self):
        product_name = "AName1"
        meta_tag_title = "Tag"
        model = "model"
        keyword = "keywordA"

        self.logger.info("Добавление нового продукта: %s", product_name)

        """Ввод названия продукта"""
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_PRODUCT_NAME)
        ).send_keys(product_name)

        self.scroll_to_end()

        """Ввод мета-тэга"""
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_META_TAG_TITLE)
        ).send_keys(meta_tag_title)

        self.scroll_to_top()

        """Переход на страницу Data"""
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.DATA_PAGE)
        ).click()

        """Ввод названия модели"""
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_MODEL)
        ).send_keys(model)

        """Переход на страницу СЕО"""
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.SEO_PAGE)
        ).click()

        """Добавление ключевого слова"""
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(Locator.INPUT_KEYWORD)
        ).send_keys(keyword)

        """Нажимаем на кнопку сохранения"""
        WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.SAVE_BUTTON)
        ).click()

        self.logger.info("Продукт успешно добавлен.")

    @allure.step("Нажатие на кнопку Submit")
    def click_submit_button(self):
        self.logger.info("Нажатие на кнопку 'Submit'")

        WebDriverWait(self.browser, self.TIMEOUT).until(EC.element_to_be_clickable(Locator.SUBMIT_BUTTON)).click()
        return self

    @allure.step("Получения количества продуктов")
    def get_product_count(self):
        self.logger.debug("Получение количества продуктов")

        """Находим текст с количеством продуктов"""
        text = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(Locator.PRODUCTS_COUNT)
        ).text
        match = re.search(r'of (\d+)', text)
        count = int(match.group(1)) if match else None

        self.logger.info("Найдено продуктов: %s", count)
        return count

    @allure.step("Находим элемент по тексту")
    def find_element_by_text(self):
        text = "AName1"
        locator = (By.XPATH, f"//td[text()='{text}']/preceding-sibling::td/input[@type='checkbox']")

        self.logger.info("Поиск элемента по тексту: %s", text)
        return WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Обрабатываем алерты")
    def handle_alert(self):
        self.logger.info("Обработка всплывающих окон (alert)")

        self.allert()
        close_button = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(Locator.POPUP_BUTTON)
        )
        close_button.click()
        self.logger.debug("Аллерт закрыт")
        self.allert()  # Закрыть повторный alert, если он появляется
