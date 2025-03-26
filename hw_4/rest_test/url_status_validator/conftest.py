import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="URL STATUS test"
    )
    parser.addoption(
        "--status_code",
        action="store",
        default=200,
        help="HTTP STATUS test"
    )

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope="session")
def status_code(request):
    return int(request.config.getoption("--status_code"))
