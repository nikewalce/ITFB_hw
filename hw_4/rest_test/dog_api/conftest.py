import pytest

# Test API: https://dog.ceo/dog-api/

def pytest_addoption(parser):
    parser.addoption(
        "--dog-url",
        action="store",
        default="https://dog.ceo/api",
        help="Dog_API test"
    )

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--dog-url")

@pytest.fixture(params=["bulldog", "retriever", "terrier", "hound", "husky", "beagle", "pug", "saluki","germanshepherd"])
def breed(request):
    return request.param

