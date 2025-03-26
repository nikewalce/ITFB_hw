import requests
import pytest
from .models import (
    BreedListResponse,
    RandomImageResponse,
    MultipleImagesResponse,
    BreedSubListResponse,
)



# Тест на получение списка всех пород
@pytest.mark.dogs
def test_get_all_breeds(base_url):
    response = requests.get(f"{base_url}/breeds/list/all")
    assert response.status_code == 200

    validated_response = BreedListResponse(**response.json())
    assert validated_response.status == "success"
    assert isinstance(validated_response.message, dict)
    # assert "message" in response.json()
    # assert isinstance(response.json()["message"], dict)
    # assert response.json()["status"] == "success"


# Получение случайного изображения конкретной породы (параметр через фикстуру)
@pytest.mark.dogs
def test_get_random_image_by_breed(base_url, breed):
    response = requests.get(f"{base_url}/breed/{breed}/images/random")
    assert response.status_code == 200

    validated_response = RandomImageResponse(**response.json())
    assert validated_response.status == "success"
    assert str(validated_response.message).startswith("https://images.dog.ceo")


# Показать несколько случайных изображений из всей коллекции собак (параметр через mark.parametrize)
@pytest.mark.dogs
@pytest.mark.parametrize('number_images', [1, 2, 3, 25, 49, 50])
def test_get_multiple_random_image_by_breed(base_url, number_images):
    response = requests.get(f'{base_url}/breeds/image/random/{number_images}')
    assert response.status_code == 200

    validated_response = MultipleImagesResponse(**response.json())
    assert validated_response.status == "success"
    assert len(validated_response.message) == number_images


# Тест на получение списка подвидов породы (если есть подвиды)
@pytest.mark.dogs
def test_get_breed_sub_list(base_url, breed):
    response = requests.get(f"{base_url}/breed/{breed}/list")
    assert response.status_code == 200

    validated_response = BreedSubListResponse(**response.json())
    assert validated_response.status == "success"
    assert isinstance(validated_response.message, list)


#Тест на возвращение массива всех изображений определенной породы
@pytest.mark.dogs
def test_array_of_all_the_images_from_breed(base_url, breed):
    response = requests.get(f"{base_url}/breed/{breed}/images")
    assert response.status_code == 200

    validated_response = MultipleImagesResponse(**response.json())
    assert validated_response.status == "success"
    assert isinstance(validated_response.message, list)
    for image in validated_response.message:
        assert str(image).startswith(f"https://images.dog.ceo/breeds/{breed}")


# Негативный тест с несуществующей породой
@pytest.mark.dogs
def test_invalid_breed(base_url):
    response = requests.get(f"{base_url}/breed/invalid_breed/images/random")
    assert response.status_code == 404

