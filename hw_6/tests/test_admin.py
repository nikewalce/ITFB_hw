from selenium.webdriver.common.by import By
from ..pages.admin_page import AdminPage

#Добавление нового товара в разделе администратора
def test_add_new_item(browser,admin_url):
    browser.get(admin_url)
    admin_page = AdminPage(browser)
    admin_page.login_to_admin('admin1', 'admin').click_submit_button()

    #закрывает уведомление о безопасности
    admin_page.allert()
    admin_page.get_element((By.CLASS_NAME, 'btn-close')).click()
    admin_page.allert()

    product_count_before = admin_page.open_catalog()
    admin_page.page_add_new_product()
    admin_page.add_new_product("AName1", "Tag", "model", "keywordA")
    product_count_after = admin_page.open_products()

    assert product_count_after == product_count_before + 1

#Удаление товара из списка в разделе администартора
def test_delete_item(browser,admin_url):
    browser.get(admin_url)
    admin_page = AdminPage(browser)
    admin_page.login_to_admin('admin1', 'admin').click_submit_button()

    # закрывает уведомление о безопасности
    admin_page.allert()
    admin_page.get_element((By.CLASS_NAME, 'btn-close')).click()
    admin_page.allert()

    product_count_before = admin_page.open_catalog()

    admin_page.find_element_by_text("AName1").click()
    admin_page.delete_product()
    admin_page.allert()
    product_count_after = admin_page.open_products()

    assert product_count_after == product_count_before - 1

