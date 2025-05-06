import pytest
from config import Config

def pytest_addoption(parser):
    parser.addoption(
        "--cart",
        action="store",
        default="http://localhost/index.php?route=api",
        help="OpenCart API"
    )

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--cart")

@pytest.fixture(scope="session")
def login_data():
    config = Config()
    login_data = {
        'username': config.token_username,
        'key': config.token_key,
    }
    return login_data

@pytest.fixture(params=["b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0",
                        "ef970757-fe42-416f-931d-722451f1f59c",
                        "ea4f30c0-bce6-416b-8904-fab4055a7362",
                        "5ae467af-66dc-4d7f-8839-44228f89b596",
                        "58293321-14ae-49d7-9a7b-08436c9e63a6"])
def breweries(request):
    return request.param

@pytest.fixture(params=["San Diego",
                        "Jangsu-gun",
                        "Norman",
                        "Mount Pleasant",
                        "Gangnam-gu"])
def city(request):
    return request.param

