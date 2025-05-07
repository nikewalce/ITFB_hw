import requests
import pytest
from .models import (Token)

@pytest.mark.api_cart
def test_get_token(base_url, login_data):
    response = requests.post(f"{base_url}/login", data=login_data)
    assert response.status_code == 200
    validated_response = Token(**response.json())
    assert isinstance(validated_response.api_token, str)

def test_add_to_cart(base_url, login_data):
    login_response = requests.post(f"{base_url}/login", data=login_data)
    assert login_response.status_code == 200

    # Проверяем правильность получения токена
    validated_response = Token(**login_response.json())
    assert isinstance(validated_response.api_token, str)

    ADD_TO_CART_URL = f'{base_url}/cart/add&api_token={validated_response.api_token}'

    add_payload = {
        'product_id': 40,  # ID товара
        'quantity': 1,
    }


    response = requests.post(ADD_TO_CART_URL, data=add_payload)
    print(response.json())
    #
    # # Шаг 2: Данные для добавления товара в корзину
    # cart_data = {
    #     'product_id': 40,  # ID товара
    #     'quantity': 2,  # Количество товара
    #     'option': {},  # Опции (если есть)
    #     'subscription_plan_id': 0  # ID плана подписки (если есть)
    # }
    # print(validated_response.api_token)
    # # URL для добавления товара в корзину с токеном
    # cart_url = f'{base_url}/cart/add&api_token={validated_response.api_token}'

    # # Отправляем POST-запрос с данными товара
    # cart_response = requests.post(cart_url, data=cart_data)
    #
    # # Проверяем ответ от API
    # if cart_response.status_code == 200:
    #     print(cart_response.json())  # Выводим ответ от API
    # else:
    #     print(f"Error: {cart_response.status_code}")  # В случае ошибки выводим код статуса

