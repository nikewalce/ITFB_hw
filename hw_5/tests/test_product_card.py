from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

#Проверка алерта после нажатия кнопки add_to_wish_list
def test_add_to_wish_list(browser, card_url):
    product_name, url = card_url
    browser.get(url)

    wishlist_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='content']/div[1]/div[2]/form/div/button[1]")))
    wishlist_button.click()

    alert_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-dismissible"))
    )

    assert f"You must login or create an account to save {product_name} to your wish list!" == alert_message.text

#Проверка алерта после нажатия кнопки Compare this Product
def test_compare(browser, card_url):
    product_name, url = card_url
    browser.get(url)

    compare_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='content']/div[1]/div[2]/form/div/button[2]")))
    compare_button.click()

    alert_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-dismissible"))
    )

    assert f"Success: You have added {product_name} to your product comparison!" == alert_message.text

def test_add_to_cart(browser, card_url):
    product_name, url = card_url
    browser.get(url)

    add_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.ID, "button-cart")))
    add_button.click()

    alert_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-dismissible"))
    )

    assert f"Success: You have added {product_name} to your shopping cart!" == alert_message.text

#Проверка ввода данных в input
@pytest.mark.parametrize('quantity', ["1", "2", "10", "100"])
def test_input_quantity(browser, card_url, quantity):
    product_name, url = card_url
    browser.get(url)

    input_quantity = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "input-quantity")))
    input_quantity.clear()
    input_quantity.send_keys(quantity)

    entered_text = input_quantity.get_attribute("value")
    assert entered_text == quantity

#Проверка, что после клика на изображение оно увеличивается
def test_image_enlargement(browser, card_url):
    product_name, url = card_url
    browser.get(url)

    thumbnail_image = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img.img-thumbnail"))
    )
    #URL маленького изображения
    original_image_url = thumbnail_image.get_attribute("src")
    thumbnail_image.click()

    enlarged_image = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img.mfp-img"))
    )
    # URL увеличенного изображения
    enlarged_image_url = enlarged_image.get_attribute("src")

    assert original_image_url != enlarged_image_url