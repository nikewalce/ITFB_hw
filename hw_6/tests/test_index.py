from pages.main_page import MainPage
import pytest

@pytest.mark.parametrize("currency_symbol, expected_text", [
    ("£", "£"),
    ("€", "€"),
    ("$", "$")
])
def test_currency_dropdown(browser, base_url, currency_symbol, expected_text):
    browser.get(base_url)
    main_page = MainPage(browser)
    main_page.click_currency_button()
    main_page.select_currency(currency_symbol)
    updated_currency = main_page.text_in_currency_button(currency_symbol)
    assert expected_text in updated_currency.text
