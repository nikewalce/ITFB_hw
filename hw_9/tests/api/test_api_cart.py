import requests
import pytest
from tests.api.models import AddCart, DeleteCart, UpdateCart, SelectCart, CurrencyChange, AddVoucher
import json

@pytest.mark.api_cart
def test_add_to_cart(base_url, api_token, db):
    add_to_cart_url = f'{base_url}/cart/add&api_token={api_token}'
    #Можно через параметризацию добавить несколько
    add_payload = {
        'product_id': 40,  # ID товара
        'quantity': 1, #кол-во товаров
    }
    response = requests.post(add_to_cart_url, data=add_payload)
    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    assert isinstance(AddCart(**response.json()), AddCart), "Валидация ответа от добавления товара в корзину не прошла"
    assert db.check_product_in_cart(api_token, add_payload['product_id'], add_payload['quantity']), "Товар не добавлен в корзину"

@pytest.mark.api_cart
def test_update_cart_item_quantity(base_url, api_token, db):
    update_cart_item_url = f'{base_url}/cart/edit&api_token={api_token}'
    # Можно через параметризацию добавить несколько
    update_payload = {
        'key': db.select_cart_id_by_session_id(api_token),  # cart_id из таблицы oc_cart
        'quantity': 2,  # кол-во товаров
    }
    response = requests.post(update_cart_item_url, data=update_payload)
    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    assert isinstance(UpdateCart(**response.json()), UpdateCart), "Валидация ответа от изменения товара в корзине не прошла"
    assert db.check_update_quantity_in_cart(update_payload['key'], api_token, update_payload['quantity']), "В базе данных в таблице oc_cart quantity не равно заданному"

@pytest.mark.api_cart
def test_select_cart_info(base_url, api_token, db):
    select_cart_info_url = f'{base_url}/cart/products&api_token={api_token}'
    response = requests.post(select_cart_info_url, data={})
    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    assert isinstance(SelectCart(**response.json()), SelectCart), "Валидация ответа от получения содержимого корзины не прошла"
    assert db.select_cart_info_by_session_id(api_token)

@pytest.mark.api_cart
def test_delete_cart(base_url, api_token, db):
    delete_cart_url = f'{base_url}/cart/remove&api_token={api_token}'
    # Можно через параметризацию добавить несколько
    delete_payload = {
        'key': db.select_cart_id_by_session_id(api_token),  # cart_id из таблицы oc_cart
    }
    response = requests.post(delete_cart_url, data=delete_payload)
    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    assert isinstance(DeleteCart(**response.json()), DeleteCart), "Валидация ответа от удаления товара из корзины не прошла"
    assert not db.select_cart_info_by_session_id(api_token)

@pytest.mark.parametrize('currency, currency_sign', [('GBP', '£'), ('USD', '$'), ('EUR', '€')])
@pytest.mark.api_cart
def test_session_currency_changes(base_url, api_token, db, currency, currency_sign):
    currency_changes_url = f'{base_url}/currency&api_token={api_token}'
    payload = {
        'currency': currency,
    }
    response = requests.post(currency_changes_url, data=payload)
    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    assert isinstance(CurrencyChange(**response.json()),CurrencyChange), "Валидация ответа при смене валюты не прошла"
    select_cart_info_url = f'{base_url}/cart/products&api_token={api_token}'
    response_cart_info = requests.post(select_cart_info_url, data={})
    assert currency_sign in response_cart_info.json()['totals'][0]['text']
    #Проверяем на вхождение подстроки в строку, т.к. второй элемент кортежа это строка ('4b00d52c16ee85f765caf8165d', '{"api_id":"2","language":"en-gb","currency":"GBP"}', datetime.datetime(2025, 5, 8, 13, 23, 47))
    assert currency in db.select_oc_session(api_token)[1]

def test_add_voucher_to_cart(base_url, api_token, db):
    add_voucher_to_cart_url = f'{base_url}/voucher/add&api_token={api_token}'
    payload = {
					"from_name": "fromNane",
					"from_email": "from@from.com",
					"to_name": "toName",
					"to_email": "to@to.com",
					"amount": "2",
					"code": "V-1111",
					"message": "strng",
				}
    response = requests.post(add_voucher_to_cart_url, data=payload)
    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    assert isinstance(AddVoucher(**response.json()), AddVoucher), "Валидация ответа при добавлении ваучера не прошла"
    assert json.loads(db.select_oc_session(api_token)[1]).get("vouchers"), "Ключ 'vouchers' отсутствует или пуст"
    select_cart_info_url = f'{base_url}/cart/products&api_token={api_token}'
    response_cart_info = requests.post(select_cart_info_url, data={})
    assert response_cart_info.json().get("vouchers"), "Ключ 'vouchers' пуст или отсутствует в ответе"
    assert isinstance(SelectCart(**response_cart_info.json()), SelectCart), "Валидация ответа от получения содержимого корзины не прошла"