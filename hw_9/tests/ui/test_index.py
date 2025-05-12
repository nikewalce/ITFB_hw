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
    MainPage(browser).click_cameras_button()
    CatalogPage(browser).click_add_to_cart_canon_e0s5d_button()
    ProductCartPage(browser) \
                    .click_select_available_options_dropdown_button() \
                    .qty_entry() \
                    .click_add_to_cart_button() \
                    .click_shopping_cart()
    CheckoutCartPage(browser) \
                    .click_checkout_button() \
                    .click_input_register_account() \
                    .click_button_continue() \
                    .enter_firstname() \
                    .enter_lastname() \
                    .enter_email() \
                    .enter_phone() \
                    .enter_shipping_address() \
                    .enter_shipping_city() \
                    .enter_shipping_postcode() \
                    .select_shipping_county() \
                    .select_shipping_region() \
                    .enter_password() \
                    .enter_password_confirm() \
                    .click_checkbox() \
                    .click_continue() \
                    .reload_page() \
                    .click_my_account()
    AccountAccountPage(browser).click_edit_account_information()
    assert AccountInformationPage(browser).check_data() == True

@allure.feature('DIPLOM')
@allure.story('Тестирование оформления заказа')
@allure.title('Оформление заказа авторизованным пользователем со страницы сравнения')
def test_checkout_from_compare_page_authenticated_user(browser, base_url, create_user_with_address):
    browser.get(base_url)
    MainPage(browser) \
            .click_my_account_button() \
            .click_link_login()
    AccountLoginPage(browser) \
                    .enter_email() \
                    .enter_password() \
                    .click_login_button()
    AccountAccountPage(browser).click_PhonesAndPDAs()
    CatalogPage(browser) \
                .click_compare_htc_button() \
                .click_compare_iphone_button() \
                .click_compare_palm_button() \
                .enter_string_in_search() \
                .click_search_button()
    SearchPage(browser) \
                .click_samsung_compare() \
                .click_total_compare_link()
    compare_product_page = CompareProductPage(browser)
    compare_product_page \
                        .click_remove_htc_button() \
                        .click_add_to_cart_iphone() \
                        .click_add_to_cart_palm() \
                        .click_shopping_cart_link()
    CheckoutCartPage(browser) \
                    .click_remove_palm_button() \
                    .enter_quantity_iphone() \
                    .click_update_button() \
                    .click_estimate_shipping_link() \
                    .click_select_estimate_country() \
                    .click_select_estimate_region() \
                    .enter_estimate_postcode() \
                    .click_get_quotes_button() \
                    .click_cancel_modal_button() \
                    .click_checkout_button() \
                    .click_checkbox_use_existing_address() \
                    .click_continue_button_payment_address() \
                    .click_checkbox_use_existing_shipping_address() \
                    .click_continue_button_shipping_address() \
                    .enter_comment_textarea() \
                    .click_continue_button_shipping_method() \
                    .click_checkbox() \
                    .click_continue_button_payment_method() \
                    .click_confirm_order_button()
    CheckoutSuccessPage(browser) \
                                .click_my_account_button() \
                                .click_order_history_button()
    assert AccountOrderPage(browser).check_customer_info()


@allure.feature('DIPLOM')
@allure.story('Тестирование заявки на возврат товара')
@allure.title('Заявка на возврат ранее заказанного товара')
def test_checkout_from_compare_as_authorized_user(browser, base_url, create_user_with_address):
    browser.get(base_url)
    #<Предусловие
    MainPage(browser) \
                    .click_my_account_button() \
                    .click_link_login()
    AccountLoginPage(browser) \
                            .enter_email() \
                            .enter_password() \
                            .click_login_button()
    AccountAccountPage(browser).click_main_page_logo()
    # Предусловие>
    #
    MainPage(browser) \
                    .components_mouseover() \
                    .click_monitors_link()

    CatalogPage(browser) \
                        .click_add_to_wish_list_apple() \
                        .click_add_to_wish_list_samsung() \
                        .click_wish_list()
    AccountWishlistPage(browser).click_add_to_cart_apple_button()
    ProductCartPage(browser) \
                            .click_radio_medium_checkbox() \
                            .click_checkbox3() \
                            .click_checkbox4() \
                            .enter_text_text() \
                            .click_select_available_options_dropdown() \
                            .click_yellow_available_options() \
                            .enter_textarea_available_options() \
                            .upload_file() \
                            .enter_date_time() \
                            .qty_entry() \
                            .click_add_to_cart_button() \
                            .click_cart_div() \
                            .click_cart_checkout()
    CheckoutCartPage(browser) \
                            .click_checkbox_use_existing_address() \
                            .click_continue_button_payment_address() \
                            .click_checkbox_use_existing_shipping_address() \
                            .click_continue_button_shipping_address() \
                            .enter_comment_textarea() \
                            .click_continue_button_shipping_method() \
                            .click_checkbox() \
                            .click_continue_button_payment_method() \
                            .click_confirm_order_button()
    CheckoutSuccessPage(browser) \
                                .click_my_account_button() \
                                .click_order_history_button()
    AccountOrderPage(browser) \
                            .click_view_button() \
                            .click_return_link() \
                            .enter_telephone() \
                            .click_reason_for_return_checkbox() \
                            .click_submit_button()
    assert "account/return/success" in browser.current_url, "URL не содержит 'account/return/success'"
