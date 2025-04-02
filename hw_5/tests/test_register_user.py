from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Тест на успешную регистрацию нового пользователя
def test_successful_registration(browser, register_url):
    browser.get(register_url)

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "input-firstname"))
    ).send_keys("Данил")

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "input-lastname"))
    ).send_keys("Васильев")

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "input-email"))
    ).send_keys("nikewa3lce123@example.com")

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "input-password"))
    ).send_keys("password123")

    checkbox = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.NAME, "agree"))
    )
    browser.execute_script("arguments[0].scrollIntoView();", checkbox)
    time.sleep(3)
    checkbox.click()

    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']"))
    )
    button.click()

    WebDriverWait(browser, 2).until(EC.title_is("Your Account Has Been Created!"))

    assert "Your Account Has Been Created!" in browser.title, "Сообщение об успешной регистрации не отображается"

# Повторное использование почты, проверка алерта
def test_REregistration(browser, register_url):
    browser.get(register_url)

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "input-firstname"))
    ).send_keys("Данил")

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "input-lastname"))
    ).send_keys("Васильев")

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "input-email"))
    ).send_keys("nikewa3lce123@example.com")

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "input-password"))
    ).send_keys("password123")

    checkbox = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.NAME, "agree"))
    )
    browser.execute_script("arguments[0].scrollIntoView();", checkbox)
    time.sleep(3)
    checkbox.click()

    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']"))
    )
    button.click()

    alert_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-dismissible"))
    )

    assert "Warning: E-Mail Address is already registered!" == alert_message.text, "Сообщение о том, что почта уже зарегистрирована не отображается"



# Тест на проверку наличия ссылки на политику конфиденциальности
def test_privacy_policy_link(browser, register_url):
    browser.get(register_url)

    privacy_policy_link = WebDriverWait(browser,5).until(EC.presence_of_element_located((By.LINK_TEXT, "Privacy Policy")))
    assert privacy_policy_link.is_displayed(), "Ссылка на политику конфиденциальности не отображается"


# Тест на проверку работы ссылки login page
def test_login_page(browser, register_url):
    browser.get(register_url)
    login_page = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "login page")))
    login_page.click()

    WebDriverWait(browser, 2).until(EC.title_is("Account Login"))
    assert browser.title == "Account Login", "При переходе по ссылке на страницу входа, она либо ведет не в то место, либо вовсе не работает"

#Тест на наличие правильных полей в меню list_group
def test_right_list_group(browser, register_url):
    browser.get(register_url)
    list_group_list = [
    "Login",
    "Register",
    "Forgotten Password",
    "My Account",
    "Payment Methods",
    "Address Book",
    "Wish List",
    "Order History",
    "Downloads",
    "Subscriptions",
    "Reward Points",
    "Returns",
    "Transactions",
    "Newsletter"
    ]
    list_group = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='list-group mb-3']")))

    for element_list in list_group_list:
        assert element_list in list_group.text
