import requests
import pytest
from .models import (ListBrewery,
                     SingleBrewery,)


# Тест на получение всех пивоварен
@pytest.mark.brewery
def test_get_list_brewery(base_url):
    response = requests.get(f"{base_url}/")
    assert response.status_code == 200

    validated_response = ListBrewery(message = response.json())
    assert isinstance(validated_response.message, list)
    assert len(validated_response.message) > 0

# Тест на получение одной пивоварни
@pytest.mark.brewery
def test_get_single_brewery(base_url, breweries):
    response = requests.get(f"{base_url}/{breweries}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

    validated_response = SingleBrewery(message = response.json())
    assert validated_response.message.id == breweries


# Тест на фильтрацию по городу
@pytest.mark.brewery
def test_get_city_brewery(base_url, city):
    response = requests.get(base_url,
                    params={'by_city': city})
    assert response.status_code == 200

    validated_response = ListBrewery(message = response.json())
    for brewery in validated_response.message:
        assert brewery.city == city

#Тест на вовзрат рандомной пивоварни
@pytest.mark.brewery
def test_random_brewery(base_url):
    response = requests.get(f"{base_url}/random")
    assert response.status_code == 200

    response1 = requests.get(f"{base_url}/random")
    assert response1.status_code == 200

    validated_response = SingleBrewery(message = response.json()[0])
    validated_response1 = SingleBrewery(message = response1.json()[0])

    assert validated_response1.message.id != validated_response.message.id

#Вывод определенного кол-ва рандомных пивоварен
@pytest.mark.brewery
@pytest.mark.parametrize('number', [1, 2, 3, 25, 49, 50])
def test_number_random_breweries(base_url, number):
    response = requests.get(base_url+"/random",
                            params= {'size': number})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    validated_response = ListBrewery(message = response.json())
    assert len(validated_response.message) == number