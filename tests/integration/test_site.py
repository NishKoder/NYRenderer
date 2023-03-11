import pytest
from NYRenderer.site import render_site
from NYRenderer.custom_exception import InvalideURLException


class TestRenderSite:
    valide_test_data = [
        ("http://github.com/", "success"),
        ("https://github.com/", "success"),
    ]

    invalid_test_data = [
        ("https://github/"),
        ("http://github/"),
        ("http:/github"),
        ("https:/github"),
        ("https/github"),
        ("https:/github"),
        ("github/"),
    ]

    @pytest.mark.parametrize("url, response", valide_test_data)
    def test_render_site_success(self, url, response):
        assert render_site(url) == response

    @pytest.mark.parametrize("url", invalid_test_data)
    def test_render_site_failed(self, url):
        with pytest.raises(InvalideURLException):
            render_site(url)
