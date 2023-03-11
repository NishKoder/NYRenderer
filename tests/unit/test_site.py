import pytest
from NYRenderer.site import is_valid

test_data = [
    ("http://github.com/", True),
    ("https://github.com/", True),
    ("https://github/", False),
    ("http://github/", False),
    ("http:/github", False),
    ("https:/github", False),
    ("https/github", False),
    ("https:/github", False),
    ("github/", False),
]


@pytest.mark.parametrize('url, response', test_data)
def test_is_valid(url, response):
    assert is_valid(url) == response
