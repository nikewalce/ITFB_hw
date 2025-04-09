import time
from ..pages.main_page import MainPage
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

    if currency_symbol == "£":
        main_page.click_pound_option()
    elif currency_symbol == "€":
        main_page.click_euro_option()
    elif currency_symbol == "$":
        main_page.click_dollar_option()
        time.sleep(0.3)

    updated_currency = main_page.text_in_currency_button(currency_symbol)
    assert expected_text in updated_currency.text
