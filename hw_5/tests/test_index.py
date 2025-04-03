from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
"""
Написать тесты проверяющие элементарное наличие элементов на разных страницах приложения opencart
Использовать методы явного ожидания элементов
"""
#Тест на проверку title
def test__title(browser, base_url):
    browser.get(base_url)
    try:
        WebDriverWait(browser, 2).until(EC.title_is("Your Store"))
        assert browser.title == "Your Store", f"Ожидался title 'Your Store', но получен '{browser.title}'"
    except TimeoutException:
        print("Элемент не появился или его нет")
        assert False, "Элемент не появился или его нет"

#Тест на проверку наличия инпута для поиска
def test_input_search(browser, base_url):
    browser.get(base_url)
    try:
        element = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.NAME, "search"))
        )
        assert element is not None
    except TimeoutException:
        print("Элемент не появился или его нет")
        assert False, "Элемент не появился или его нет"


#Тест на проверку наличия футера
def test_footer(browser, base_url):
    browser.get(base_url)
    try:
        element = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//footer"))
        )
        assert element is not None
    except TimeoutException:
        print("Элемент не появился или его нет")
        assert False, "Элемент не появился или его нет"

#Тест на наличие ссылки до вишлиста
def test_div_row(browser, base_url):
    browser.get(base_url)
    try:
        element = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//a[@id='wishlist-total']"))
        )
        assert element is not None
    except TimeoutException:
        print("Элемент не появился или его нет")
        assert False, "Элемент не появился или его нет"

def test_categories_menu(browser, base_url):
    browser.get(base_url)
    try:
        element = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//nav[@id='menu']"))
        )
        assert element is not None
    except TimeoutException:
        print("Элемент не появился или его нет")
        assert False, "Элемент не появился или его нет"

def test_carousel_div(browser,base_url):
    browser.get(base_url)
    carousel_div = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "carousel-item")))
    assert carousel_div is not None

#Тест на проверку работы поля поиска (позитив)
def test_search_functionality(browser, base_url):
    browser.get(base_url)

    search_box = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.NAME, "search"))
    )

    search_box.send_keys("MacBook")
    #имитация нажатия Enter
    search_box.send_keys(Keys.RETURN)

    try:
        results = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='product-list']"))
        )
        assert results is not None
    except TimeoutException:
        print("Поиск не вернул результаты")
        assert False, "Поиск не вернул результаты"

#тест на изменение валюты в форме form-currency
def test_currency_dropdown(browser,base_url):
    browser.get(base_url)
    currency_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//form[@id='form-currency']")))
    currency_button.click()

    pound_option = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//a[text()='£ Pound Sterling']")))
    pound_option.click()

    WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.XPATH, "//form[@id='form-currency']"), "£")
    )

    updated_currency = browser.find_element(By.XPATH, "//form[@id='form-currency']").text
    assert "£" in updated_currency, "Валюта не изменилась"

