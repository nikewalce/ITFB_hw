from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.product_cart_page import ProductCartPage
from pages.checkout_cart_page import CheckoutCartPage
from pages.account_information_page import AccountInformationPage
from pages.account_login_page import AccountLoginPage
from pages.account_account_page import AccountAccountPage
from pages.search_page import SearchPage
from pages.compare_product_page import CompareProductPage
from pages.checkout_success_page import CheckoutSuccessPage
from pages.account_order_page import AccountOrderPage
import allure

@allure.feature('DIPLOM')
@allure.story('Тестирование регистрации')
@allure.title('Регистрация пользователя при оформление товара')
def test_user_registration_at_checkout_product(browser, base_url, clean_test_data):
    browser.get(base_url)
    #Открыть главную страницу opencart
    main_page = MainPage(browser)
    #В панели с категорией товаров нажать "Cameras"
    main_page.click_cameras_button()
    #На карточке товара "Canon EOS 5D" нажать "Add to Cart"(иконка корзины)
    CatalogPage(browser).click_add_to_cart_canon_e0s5d_button()
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
    AccountAccountPage(browser).click_edit_account_information()
    assert AccountInformationPage(browser).check_data() == True

def test_checkout_from_compare_page_authenticated_user(browser, base_url, create_user_with_address):
    browser.get(base_url)
    # Открыть главную страницу opencart
    main_page = MainPage(browser)
    #В верхней навигационной панели нажать "My account"
    main_page.click_my_account_button()
    #Выбрать "Login"
    main_page.click_link_login()
    #Заполнить поле "E-Mail" значением
    account_login_page = AccountLoginPage(browser)
    account_login_page.enter_email()
    #Заполнить поле "Password" значением
    account_login_page.enter_password()
    #Нажать "Login"
    account_login_page.click_login_button()
    #	В панели с категорией товаров нажать "Phones & PDAs"
    AccountAccountPage(browser).click_PhonesAndPDAs()
    #На карточке товара "HTC Touch HD" нажать "Compare this Product"(добавить к сравнению)
    catalog_page = CatalogPage(browser)
    catalog_page.click_compare_htc_button()
    #На карточке товара "iPhone" нажать "Compare this Product"(добавить к сравнению)
    catalog_page.click_compare_iphone_button()
    #На карточке товара "Palm Treo Pro" нажать "Compare this Product"(добавить к сравнению)
    catalog_page.click_compare_palm_button()
    #	В поисковой строке вверху страницы ввести в поисковую строку "Samsung"
    catalog_page.enter_string_in_search()
    #Нажать кнопку поиск
    catalog_page.click_search_button()
    #На карточке товара "Samsung Galaxy Tab 10.1" нажать "Compare this Product"(добавить к сравнению)
    search_page = SearchPage(browser)
    search_page.click_samsung_compare()
    #Над карточками товаров нажать "Product Compare"
    search_page.click_total_compare_link()
    #Нажать кнопку "Remove" под товаром "HTC Touch HD"
    compare_product_page = CompareProductPage(browser)
    compare_product_page.click_remove_htc_button()
    #Нажать кнопку "Add to Cart" под товаром "iPhone"
    compare_product_page.click_add_to_cart_iphone()
    #Нажать кнопку "Add to Cart" под товаром "Palm Treo Pro"
    compare_product_page.click_add_to_cart_palm()
    #В верхней навигационной панели нажать "Shopping Cart"
    compare_product_page.click_shopping_cart_link()
    #Нажать кнопку удаления товара "Palm Treo Pro"
    checkout_cart_page = CheckoutCartPage(browser)
    checkout_cart_page.click_remove_palm_button()
    #В поле "Quantity" ввести значение "2" для товара "Iphone"
    checkout_cart_page.enter_quantity_iphone()
    #Нажать кнопку "Update" для количества товара "Iphone"
    checkout_cart_page.click_update_button()
    #	Нажать на вкладку "Estimate Shipping & Taxes"
    checkout_cart_page.click_estimate_shipping_link()
    #Выбрать в поле "Country" значение "Antigua and Barbuda"
    checkout_cart_page.click_select_estimate_country()
    #Выбрать в поле "Region / State" значение "Barbuda"
    checkout_cart_page.click_select_estimate_region()
    #Заполнить поле "Post Code" значением "123456"
    checkout_cart_page.enter_estimate_postcode()
    #Нажать кнопку "Get Quotes"
    checkout_cart_page.click_get_quotes_button()
    #Нажать кнопку закрытия формы
    checkout_cart_page.click_cancel_modal_button()
    #Нажать кнопку "Checkout"
    checkout_cart_page.click_checkout_button()
    #Выбрать чек-бох "I want to use an existing address"(если не выбран)
    checkout_cart_page.click_checkbox_use_existing_address()
    #Нажать "Continue"
    checkout_cart_page.click_continue_button_payment_address()
    #Выбрать чек-бох "I want to use an existing address"(если не выбран)
    checkout_cart_page.click_checkbox_use_existing_shipping_address()
    # Нажать "Continue"
    checkout_cart_page.click_continue_button_shipping_address()
    #В поле "Add Comments" добавить текст из 10 символов
    checkout_cart_page.enter_comment_textarea()
    #Нажать "Continue"
    checkout_cart_page.click_continue_button_shipping_method()
    #Активировать чекбокс "I have read and agree to the Terms & Conditions"
    checkout_cart_page.click_checkbox()
    #	Нажать "Continue"
    checkout_cart_page.click_continue_button_payment_method()
    #	Нажать "Confirm Order"
    checkout_cart_page.click_confirm_order_button()
    #В верхней навигационной панели нажать "My account"
    checkout_success_page = CheckoutSuccessPage(browser)
    checkout_success_page.click_my_account_button()
    #Выбрать "Order History"
    checkout_success_page.click_order_history_button()
    assert AccountOrderPage(browser).check_customer_info()