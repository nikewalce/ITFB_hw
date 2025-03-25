import requests
import pytest
from .models import (ListJsonPlaceholder, SingleJsonPlaceholder)

#Тест на вывод всех постов
@pytest.mark.jsonplaceholder
def test_listing_all_resources(base_url):
    response = requests.get(f'{base_url}/posts')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    validated_response = ListJsonPlaceholder(message = response.json())
    assert len(validated_response.message) > 0 and len(validated_response.message) < 101

#Тест на вывод определенного поста по ID
@pytest.mark.jsonplaceholder
@pytest.mark.parametrize('postId', [1, 2, 10, 100])
def test_number_resources(base_url, postId):
    response = requests.get(f'{base_url}/posts/{postId}')
    assert response.status_code == 200

    validated_response = SingleJsonPlaceholder(message = response.json())
    assert validated_response.message.id == postId


#Тест на проверку несуществующего номера поста
@pytest.mark.jsonplaceholder
@pytest.mark.parametrize('postId', [-1, 101])
def test_non_existent_post_number(base_url, postId):
    response = requests.get(f'{base_url}/posts/{postId}')
    assert response.status_code == 404
    assert not response.json()

# Добавление нового поста через Post запрос
@pytest.mark.jsonplaceholder
def test_creating_resource(base_url, post_body):
    headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }
    body_json, expected_status = post_body
    response = requests.post(base_url + "/posts",
        json=body_json, headers=headers)
    assert response.status_code == expected_status

    validated_response = SingleJsonPlaceholder(message = response.json())
    assert validated_response.message.userId == body_json['userId']


#Отправка PUT-запроса
@pytest.mark.jsonplaceholder
def test_update_resource(base_url, put_body):
    body_json, expected_status = put_body
    response = requests.put(base_url + f"/posts/{body_json["id"]}", json=body_json)
    assert response.status_code == expected_status

    #Проверка на то, что put изменил данные и отличается от стандартных
    if expected_status == 200:
        response_get = requests.get(base_url + f"/posts/{body_json["id"]}")
        print(response_get.json())
        assert response_get.status_code == 200
        assert response_get.json() != response.json()

#Проверка отправки PATCH запроса, изменение title
@pytest.mark.jsonplaceholder
def test_patch_resource(base_url):
    data = {
        "title": "Обновленный заголовок"
    }
    response_get = requests.get(base_url+ "/posts/1")
    validated_response_get = SingleJsonPlaceholder(message = response_get.json())
    assert response_get.status_code == 200

    response_patch = requests.patch(base_url + "/posts/1", json=data)
    validated_response_patch = SingleJsonPlaceholder(message = response_patch.json())
    assert response_patch.status_code == 200
    assert validated_response_patch.message.title != validated_response_get.message.title

