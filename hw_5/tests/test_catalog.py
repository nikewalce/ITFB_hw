from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
Написать тесты проверяющие элементарное наличие элементов на разных страницах приложения opencart
Использовать методы явного ожидания элементов
"""

#Проверка отображения кнопки для раскрытия категорий при уменьшенном размере экрана
def test_navbar_button(browser, base_url):
    browser.get(base_url)
    browser.set_window_size(980, 545)
    button = WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.CLASS_NAME, "navbar-toggler")))
    assert button is not None

#Проверка наличия блока категорий
def test_div_categories(browser, base_url):
    browser.get(base_url)
    menu = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#category")))
    assert menu is not None

#Проверка наличия navbar-menu
def test_navbar_menu(browser, base_url):
    browser.get(base_url)
    menu = WebDriverWait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#navbar-menu")))
    assert menu is not None

#Тест на наличие всех категорий
def test_categories(browser, base_url):
    categories_text = ['Desktops' ,'Laptops & Notebooks', 'Components', 'Tablets', 'Software', 'Phones & PDAs', 'Cameras', 'MP3 Players']
    browser.get(base_url)
    categories = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH,"//div[@id='navbar-menu']")))
    categories_in_list = [item.strip() for item in categories.text.split("\n") if item.strip()]
    assert categories_in_list == categories_text

#Тест, подтверждающий отображение списка подкатегорий (если они есть) после выбора категории
def test_open_list_category_after_click(browser, base_url, dropdown_categories):
    browser.get(base_url)
    ul_category = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.LINK_TEXT,f"{dropdown_categories}")))
    ul_category.click()
    assert "show" in ul_category.get_attribute("class"), "Атрибут class не изменился!"


#Проверка загрузки соответствующей страницы после выбора категории (у кого есть dropdown)
def test_correct_h1_dropdown_categories(browser, base_url, dropdown_categories):
    browser.get(base_url)
    ul_category = WebDriverWait(browser, 2).until(
        EC.presence_of_element_located((By.LINK_TEXT, f"{dropdown_categories}")))
    ul_category.click()
    show_link = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.LINK_TEXT, f"Show All {dropdown_categories}")))
    show_link.click()
    h1 = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert dropdown_categories == h1.text


#Проверка загрузки соответствующей страницы после выбора категории (у которой нет dropdown)
def test_go_page_category(browser, base_url, redirect_categories):
    browser.get(base_url)
    ul_category = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.LINK_TEXT,f"{redirect_categories}")))
    ul_category.click()
    assert browser.current_url != base_url, f"URL не изменился после клика! Было: {base_url}, стало: {browser.current_url}"

#Проверка наличия ссылки Show All каждой категории, которая имеет dropdown-menu
def test_presence_link_show_category_name(browser, base_url, dropdown_categories):
    browser.get(base_url)
    ul_category = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.LINK_TEXT, f"{dropdown_categories}")))
    ul_category.click()
    show_all_text = WebDriverWait(browser, 2).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'dropdown-menu') and contains(@class, 'show')]")))

    assert f"Show All {dropdown_categories}" in show_all_text.text

