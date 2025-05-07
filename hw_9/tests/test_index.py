from pages.main_page import MainPage
from pages.cameras_catalog_page import CamerasCatalogPage
from pages.product_cart_page import ProductCartPage
from pages.checkout_cart_page import CheckoutCartPage
from pages.account_information_page import AccountInformationPage
from tests.sql_config import delete_user_by_email as delete_user
import pytest
import allure

@allure.feature('DIPLOM')
@allure.story('Тестирование регистрации')
@allure.title('Регистрация пользователя при оформление товара')
def test_user_registration_at_checkout_product(browser, base_url):
    browser.get(base_url)
    #Открыть главную страницу opencart
    main_page = MainPage(browser)
    #В панели с категорией товаров нажать "Cameras"
    main_page.click_cameras_button()
    #На карточке товара "Canon EOS 5D" нажать "Add to Cart"(иконка корзины)
    CamerasCatalogPage(browser).click_add_to_cart_canon_e0s5d_button()
    #В разделе "Available Options" в поле "Select" выбрать цвет "Red"
    product_cart_page = ProductCartPage(browser)
    product_cart_page.click_select_available_options_dropdown_button()
    #В разделе "Available Options" в поле "Qty" ввести количество товара "2"
    product_cart_page.qty_entry()
    #Добавить товар в корзину. Нажать кнопку "Add to Cart"
    product_cart_page.click_add_to_cart_button()
    #В верхней навигационной панели нажать "Shopping Cart"
    product_cart_page.click_shopping_cart()
    #Нажать "Checkout"
    checkout_cart_page = CheckoutCartPage(browser)
    checkout_cart_page.click_checkout_button()
    #Выбрать "Register Account"
    checkout_cart_page.click_input_register_account()
    #Нажать "Continue"
    checkout_cart_page.click_button_continue()
    #Заполнить поле "First Name" значением "Testname"
    checkout_cart_page.enter_firstname()
    checkout_cart_page.enter_lastname()
    checkout_cart_page.enter_email()
    checkout_cart_page.enter_phone()
    checkout_cart_page.enter_shipping_address()
    checkout_cart_page.enter_shipping_city()
    checkout_cart_page.enter_shipping_postcode()
    checkout_cart_page.select_shipping_county()
    checkout_cart_page.select_shipping_region()
    checkout_cart_page.enter_password()
    checkout_cart_page.enter_password_confirm()
    checkout_cart_page.click_checkbox()
    #Нажать "Continue"
    checkout_cart_page.click_continue()
    #Обновить страницу
    checkout_cart_page.reload_page()
    #В верхней навигационной панели нажать "My account"
    #В выпавшем списке нажать "My account"
    checkout_cart_page.click_my_account()
    #Нажать "Edit your account information"
    checkout_cart_page.click_edit_account_information()
    assert AccountInformationPage(browser).check_data() == True
    #Чистим за собой
    delete_user("test@test.ru")
