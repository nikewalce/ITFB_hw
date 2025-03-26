import pytest

# Test API: https://jsonplaceholder.typicode.com/.

def pytest_addoption(parser):
    parser.addoption(
        "--jsonplaceholder-url",
        action="store",
        default="https://jsonplaceholder.typicode.com",
        help="JSONPlaceholder_API test"
    )

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--jsonplaceholder-url")

@pytest.fixture(params=[({
                            "title": "one",
                            "body": "someTestonee",
                            "userId": 20
                        }, 201),
                        ({
                            "title": "two",
                            "body": "someTextTwo",
                            "userId": 25
                        },201),
                        ({
                            "title": "three",
                            "body": "someTextThreee",
                            "userId": 10000,
                            "error": "error"
                        },201),
                        ])
def post_body(request):
    return request.param

@pytest.fixture(params=[({
                            "id": 101,
                            "title": 'three_rename',
                            "body": 'rename',
                            "userId": 1000
                        }, 500),
                        ({
                             "id": 1,
                             "title": 'foo',
                             "body": 'bar',
                             "userId": 1
                         }, 200),
                        ])
def put_body(request):
    return request.param