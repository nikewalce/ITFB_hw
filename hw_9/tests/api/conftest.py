import pytest
from config import Config
from api.models import Token
import requests
from sql.sql_config_api import CartDB

@pytest.fixture(scope="session")
def db():
    """Фикстура для инициализации подключения к базе данных."""
    db_instance = CartDB()
    return db_instance

def pytest_addoption(parser):
    parser.addoption(
        "--cart",
        action="store",
        default="http://localhost/index.php?route=api",
        help="OpenCart api"
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


@pytest.fixture(scope="session")
def api_token(base_url, login_data, db):
    """Фикстура для получения и проверки токена."""
    login_response = requests.post(f"{base_url}/login", data=login_data)
    assert login_response.status_code == 200, "Ошибка авторизации"
    validated_token = Token(**login_response.json())
    assert isinstance(validated_token.api_token, str), "Токен не строка"
    yield validated_token.api_token
    #Чистим за собой
    #db.delete_cart_by_api_id(2)
    db.delete_session_by_session_id(validated_token.api_token)
    db.delete_oc_session_by_session_id(validated_token.api_token)

# @pytest.fixture(params=["b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0",
#                         "ef970757-fe42-416f-931d-722451f1f59c",
#                         "ea4f30c0-bce6-416b-8904-fab4055a7362",
#                         "5ae467af-66dc-4d7f-8839-44228f89b596",
#                         "58293321-14ae-49d7-9a7b-08436c9e63a6"])
# def breweries(request):
#     return request.param
#
# @pytest.fixture(params=["San Diego",
#                         "Jangsu-gun",
#                         "Norman",
#                         "Mount Pleasant",
#                         "Gangnam-gu"])
# def city(request):
#     return request.param

