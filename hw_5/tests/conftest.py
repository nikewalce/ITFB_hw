import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService


def pytest_addoption(parser):
    parser.addoption("--url", default="http://opencart/")
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true",default=False)

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
    return 'http://opencart/admin/'

@pytest.fixture()
def register_url():
    return 'http://opencart/index.php?route=account/register'

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument(argument="headless=new")
        driver = webdriver.Chrome(options = options,service=ChromiumService())
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
        binary_yandex_driver_file = 'yandexdriver.exe'
        if headless:
            options.add_argument(argument="headless=new")
        service = ChromiumService(binary_yandex_driver_file)
        driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    request.addfinalizer(driver.close)

    return driver

@pytest.fixture(params=["Desktops", "Laptops & Notebooks", "Components", "MP3 Players"])
def dropdown_categories(request):
    return request.param

@pytest.fixture(params=["Tablets", "Software", "Phones & PDAs", "Cameras"])
def redirect_categories(request):
    return request.param
