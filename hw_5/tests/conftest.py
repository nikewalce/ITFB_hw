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
        driver = webdriver.Safari()
    driver.maximize_window()
    request.addfinalizer(driver.close)

    # driver.implicitly_wait(3)

    return driver