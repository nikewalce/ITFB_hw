from pages.register_page import RegisterPage
import allure

@allure.feature('hw_7')
@allure.story('Тестирование страницы регистрации')
@allure.title('Тест на Регистрация нового пользователя в магазине opencart')
@allure.description('Вводим имя, фамилию, почту, пароль, нажимаем на чекбокс и кнопку продолжить')
def test_successful_registration(browser, register_url):
    browser.get(register_url)
    register_page = RegisterPage(browser)
    register_page.enter_firstname()
    register_page.enter_lastname()
    register_page.enter_email()
    register_page.enter_password()
    register_page.click_checkbox()
    register_page.click_continue()
    register_page.check_created_account()
    assert "account/success" in browser.current_url, f"Ожидался URL, содержащий 'account/success', но получен {browser.current_url}"
