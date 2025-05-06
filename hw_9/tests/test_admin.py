from pages.admin_page import AdminPage
import allure

"""Тесты панели администратора"""
@allure.feature('hw_7')
@allure.story('Тестирование панели администратора')
@allure.title('Добавление нового товара в разделе администратора')
@allure.description('Логинимся, закрываем аллерт, открываем каталог, открываем страницу добавления товара, добавляем товар')
def test_add_new_item(browser,admin_url):
    browser.get(admin_url)
    admin_page = AdminPage(browser)
    admin_page.login_to_admin().click_submit_button()
    #admin_page.close_handle_alert()
    product_count_before = admin_page.open_catalog()
    admin_page.page_add_new_product()
    admin_page.add_new_product()
    product_count_after = admin_page.open_products()
    assert product_count_after == product_count_before + 1

@allure.feature('hw_7')
@allure.story('Тестирование панели администратора')
@allure.title('Удаление товара из списка в разделе администартора')
@allure.description('Логинимся, закрываем аллерт, открываем каталог, выбираем товар для удаления, удаляем')
def test_delete_item(browser,admin_url):
    browser.get(admin_url)
    admin_page = AdminPage(browser)
    admin_page.login_to_admin().click_submit_button()
    admin_page.close_handle_alert()
    product_count_before = admin_page.open_catalog()
    admin_page.find_element_by_text().click()
    admin_page.delete_product()
    admin_page.allert()
    product_count_after = admin_page.open_products()
    assert product_count_after == product_count_before - 1
