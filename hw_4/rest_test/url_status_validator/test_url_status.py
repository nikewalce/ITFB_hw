import requests
from .models import URLStatusModel
import pytest


@pytest.mark.urlstatus
def test_url_status(base_url, status_code):
    validated_response = URLStatusModel.validate(base_url, status_code)

    response = requests.get(base_url)
    assert response.status_code == validated_response.status_code, f"Expected {validated_response.status_code}, got {response.status_code}"

