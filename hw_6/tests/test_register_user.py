from selenium.webdriver.support import expected_conditions as EC
from ..pages.register_page import RegisterPage
from selenium.webdriver.support.wait import WebDriverWait


# Тест на Регистрация нового пользователя в магазине opencart
def test_successful_registration(browser, register_url):
    browser.get(register_url)

    register_page = RegisterPage(browser)
    register_page.enter_firstname("firstname")
    register_page.enter_lastname("lastname")
    register_page.enter_email("3email@example.com")
    register_page.enter_password("password")
    register_page.scroll_to_end()
    register_page.click_checkbox()
    register_page.click_continue()

    WebDriverWait(browser, 2).until(EC.title_is("Your Account Has Been Created!"))

    assert "Your Account Has Been Created!" in browser.title, "Сообщение об успешной регистрации не отображается"
