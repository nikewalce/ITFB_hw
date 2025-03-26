import pytest

# Test API: https://www.openbrewerydb.org/.

def pytest_addoption(parser):
    parser.addoption(
        "--brewery-url",
        action="store",
        default="https://api.openbrewerydb.org/v1/breweries",
        help="Breweries_API test"
    )

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--brewery-url")

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

