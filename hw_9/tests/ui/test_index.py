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
from pages.account_wishlist_page import AccountWishlistPage
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

@allure.feature('DIPLOM')
@allure.story('Тестирование оформления заказа')
@allure.title('Оформление заказа авторизованным пользователем со страницы сравнения')
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

def test_checkout_from_compare_as_authorized_user(browser, base_url, create_user_with_address):
    browser.get(base_url)
    # Открыть главную страницу opencart
    main_page = MainPage(browser)
    #Предусловие
    main_page.click_my_account_button()
    main_page.click_link_login()
    account_login_page = AccountLoginPage(browser)
    account_login_page.enter_email()
    account_login_page.enter_password()
    account_login_page.click_login_button()
    AccountAccountPage(browser).click_main_page_logo()
    #В панели с категорией товаров навести мышкой на "Components"
    main_page.components_mouseover()
    #В выпавшем списке нажать "Monitors"
    main_page.click_monitors_link()
    #Нажать кнопку "Add to Wish List" под товаром "Apple Cinema 30
    catalog_page = CatalogPage(browser)
    catalog_page.click_add_to_wish_list_apple()
    #Нажать кнопку "Add to Wish List" под товаром "Samsung SyncMaster 941BW
    catalog_page.click_add_to_wish_list_samsung()
    #В верхней навигационной панели нажать "Wish List"
    catalog_page.click_wish_list()
    #Нажать кнопку "Add to Cart" товара "Apple Cinema 30"
    account_wishlist_page = AccountWishlistPage(browser)
    account_wishlist_page.click_add_to_cart_apple_button()
    #Выбрать чекбокс "Medium" для опции "Radio
    product_cart_page = ProductCartPage(browser)
    product_cart_page.click_radio_medium_checkbox()
    #Выбрать чекбокс "Checkbox 3" для опции "Checkbox"
    product_cart_page.click_checkbox3()
    #Выбрать чекбокс "Checkbox 3" для опции "Checkbox"
    product_cart_page.click_checkbox4()
    #Заполнить поле "Text" значением "Текст"
    product_cart_page.enter_text_text()
    #Нажать в поле "Select"
    product_cart_page.click_select_available_options_dropdown()
    #	В выпавшем списке выбрать "Yellow"
    product_cart_page.click_yellow_available_options()
    #Заполнить поле "Textarea" значением "Текст"
    product_cart_page.enter_textarea_available_options()
    #В поле "File" вставить пустой файл формата txt
    product_cart_page.upload_file()
    #Поля дат и времени заполнить любым значением
    product_cart_page.enter_date_time()
    #Заполнить поле "Qty" значением "2"
    product_cart_page.qty_entry()
    #Нажать кнопку "Add to Cart"
    product_cart_page.click_add_to_cart_button()
    #	Нажать кнопку корзины справа от поля поиска
    product_cart_page.click_cart_div()
    #В форме нажать "Checkout"
    product_cart_page.click_cart_checkout()
    #Выбрать чек-бох "I want to use an existing address"(если не выбран)
    checkout_cart_page = CheckoutCartPage(browser)
    checkout_cart_page.click_checkbox_use_existing_address()
    # Нажать "Continue"
    checkout_cart_page.click_continue_button_payment_address()
    # Выбрать чек-бох "I want to use an existing address"(если не выбран)
    checkout_cart_page.click_checkbox_use_existing_shipping_address()
    # Нажать "Continue"
    checkout_cart_page.click_continue_button_shipping_address()
    # В поле "Add Comments" добавить текст из 10 символов
    checkout_cart_page.enter_comment_textarea()
    # Нажать "Continue"
    checkout_cart_page.click_continue_button_shipping_method()
    # Активировать чекбокс "I have read and agree to the Terms & Conditions"
    checkout_cart_page.click_checkbox()
    #	Нажать "Continue"
    checkout_cart_page.click_continue_button_payment_method()
    #	Нажать "Confirm Order"
    checkout_cart_page.click_confirm_order_button()
    # В верхней навигационной панели нажать "My account"
    checkout_success_page = CheckoutSuccessPage(browser)
    checkout_success_page.click_my_account_button()
    # Выбрать "Order History"
    checkout_success_page.click_order_history_button()
    account_order_page = AccountOrderPage(browser)
    #Нажать "View" для ранее созданного заказа
    account_order_page.click_view_button()
    #Нажать кнопку "Return" для ранее заказанного товара
    account_order_page.click_return_link()
    #Заполнить поле "Telephone" любым 11-и значным номером
    account_order_page.enter_telephone()
    #В поле "Reason for Return" нажать на любой чекбокс
    account_order_page.click_reason_for_return_checkbox()
    #Нажать "Submit"
    account_order_page.click_submit_button()
    assert "account/return/success" in browser.current_url, "URL не содержит 'account/return/success'"
