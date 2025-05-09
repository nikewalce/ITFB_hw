from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Тест на наличие логотипа
def test_logo_displayed(browser, admin_url):
    browser.get(admin_url)
    logo = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.navbar-brand img")))
    assert logo.is_displayed(), "Логотип не отображается!"

# Тест на наличие формы логина
def test_login_form_displayed(browser, admin_url):
    browser.get(admin_url)
    form = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "form-login")))
    assert form.is_displayed(), "Форма логина не отображается!"

# Тест на наличие поля ввода имени пользователя
def test_username_field(browser,admin_url):
    browser.get(admin_url)
    username_field = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "input-username")))
    assert username_field.is_displayed(), "Поле для ввода имени пользователя не отображается!"

# Тест на наличие поля ввода пароля
def test_password_field(browser,admin_url):
    browser.get(admin_url)
    password_field = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "input-password")))

    assert password_field.is_displayed(), "Поле для ввода пароля не отображается!"

# Тест на наличие кнопки входа
def test_login_button(browser, admin_url):
    browser.get(admin_url)
    login_button = WebDriverWait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

    assert login_button.is_displayed(), "Кнопка входа не отображается!"

# Тест на наличие footer
def test_footer_displayed(browser, admin_url):
    browser.get(admin_url)
    footer = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "footer")))

    assert footer.is_displayed(), "Footer не отображается!"


#Проверка входа с корректными данными
def test_login_to_admin(browser, admin_url):
    browser.get(admin_url)
    admin_titile = browser.title

    username = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located(
            (By.ID, "input-username")))
    username.send_keys('admin1')

    password = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located(
            (By.ID, "input-password")))
    password.send_keys('admin')

    button = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    button.click()

    WebDriverWait(browser, 2).until(EC.title_is("Dashboard"))
    assert admin_titile != browser.title

#Проверка алерта после ввода неверных данных
def test_invalid_login(browser, admin_url):
    browser.get(admin_url)

    username = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located(
            (By.ID, "input-username")))
    username.send_keys('invalidlogin')

    password = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located(
            (By.ID, "input-password")))
    password.send_keys('invalidpassword')

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    button.click()

    error_message = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'No match for Username and/or Password')]"))
    )

    assert "No match for Username and/or Password" in error_message.text, "Сообщение об ошибке не появилось."

#Проверка, что логотип OpenCart ведет на страницу логина
def test_logo_redirect(browser, admin_url):
    browser.get(admin_url)

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='OpenCart']")))
    button.click()

    assert browser.current_url == "http://opencart/admin/index.php?route=common/login", "логотип ведет на другую ссылку"

# Проверка наличия формы
def test_login_form(browser, admin_url):
    browser.get(admin_url)

    form = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "form-login")))
    assert form.is_displayed(), "Форма логина не отображается"

