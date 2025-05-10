import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
import allure
from tests.sql_queries.sql_config_ui import delete_user_by_email as delete_user
from tests.sql_queries.sql_config_ui import delete_cart_by_product_id as delete_cart
from tests.sql_queries.sql_config_ui import create_customer_with_address as create_customer
from tests.sql_queries.sql_config_ui import delete_address_by_firstname as delete_address
from tests.sql_queries.sql_config_ui import delete_order_by_email as delete_order
from config import Config

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для добавления скриншота в отчет Allure при падении"""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        browser = item.funcargs.get("browser") 
        if browser:
            try:
                screenshot = browser.get_screenshot_as_png()
                allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(f"Не удалось сделать скриншот: {e}")

def pytest_addoption(parser):
    parser.addoption("--url", default="http://localhost/")
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true",default=False)
    parser.addoption("--remote", action="store_true", help="Запуск на Selenoid")

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    is_remote = request.config.getoption("--remote")
    #Удаленный запуск
    if is_remote:
        selenium_grid_url = "http://localhost:4444/wd/hub"
        if browser_name == "chrome":
            capabilities = {
                "browserName": "chrome",
                "enableVNC": True,
                "enableVideo": False,
            }
            options = ChromeOptions()
            if headless:
                options.add_argument("headless=new")
                options.add_argument("--disable-gpu")
            for key, value in capabilities.items():
                options.set_capability(key, value)
            driver = webdriver.Remote(command_executor=selenium_grid_url, options=options)
        elif browser_name == "firefox":
            options = FFOptions()
            options.set_capability("browserName", "firefox")
            options.set_capability("enableVNC", True)
            if headless:
                options.add_argument(argument="-headless")
            driver = webdriver.Remote(command_executor=selenium_grid_url, options=options)
        elif browser_name == "edge":
            options = EdgeOptions()
            options.set_capability("browserName", "MicrosoftEdge")
            options.set_capability("enableVNC", True)
            if headless:
                options.add_argument(argument="headless=new")
            driver = webdriver.Remote(command_executor=selenium_grid_url, options=options)
        else:
            raise ValueError(f"Unsupported browser for remote run: {browser_name}")
    #Локальный запуск
    else:
        if browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument(argument="headless=new")
            driver = webdriver.Chrome(options=options, service=ChromiumService())
        elif browser_name == "firefox":
            options = FFOptions()
            if headless:
                options.add_argument(argument="-headless")
            driver = webdriver.Firefox(options=options, service=FFService())
        elif browser_name == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument(argument="headless=new")
            driver = webdriver.Edge(options=options, service=EdgeService())
        else:
            options = webdriver.ChromeOptions()
            binary_yandex_driver_file = '../yandexdriver.exe'
            if headless:
                options.add_argument(argument="headless=new")
            service = ChromiumService(binary_yandex_driver_file)
            driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver

@pytest.fixture()
def create_user_with_address():
    """Предусловие: необходим созданный юзер с заполненым адресов в профиле"""
    config = Config()
    create_customer(
        firstname=config.register_firstname,
        lastname=config.register_lastname,
        email=config.register_email,
        phone=config.register_telephone,
        password=config.register_password,
        address_1=config.register_shipping_address1,
        city=config.register_city,
        postcode=config.register_postcode,
        country_id=config.register_country_id,
        zone_id=config.register_zone_id
    )
    yield
    delete_user(config.register_email)
    delete_address(config.register_firstname)
    delete_order(config.register_email)

@pytest.fixture()
def clean_test_data():
    """Чистим за собой бд после тестов"""
    yield
    config = Config()
    delete_user(config.register_email)
    delete_cart(30)
    delete_address(config.register_firstname)

@pytest.fixture()
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture(params=[("MacBook","http://opencart/index.php?route=product/product&language=en-gb&product_id=43"),
                        ("HTC Touch HD","http://opencart/index.php?route=product/product&language=en-gb&product_id=28&path=24"),
                        ("Samsung Galaxy Tab 10.1","http://opencart/index.php?route=product/product&language=en-gb&product_id=49&path=57")])
def card_url(request):
    return request.param

@pytest.fixture()
def admin_url():
    return 'http://localhost/administration/index.php?route=common/login'

@pytest.fixture()
def register_url():
    return 'http://localhost/opencart-master/upload/index.php?route=account/register'

@pytest.fixture(params=["Desktops", "Laptops & Notebooks", "Components", "MP3 Players"])
def dropdown_categories(request):
    return request.param

@pytest.fixture(params=["Tablets", "Software", "Phones & PDAs", "Cameras"])
def redirect_categories(request):
    return request.param
