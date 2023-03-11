import pytest
from NYRenderer.youtube import get_time_info
from NYRenderer.custom_exception import InvalideURLException

validate_url_data = [
    ("https://youtu.be/yuH4iRcggMw", 0),
    ("https://www.youtube.com/watch?v=yuH4iRcggMw", 0),
    ("https://www.youtube.com/watch?v=yuH4iRcggMw&t=60s", 60),
]

invalid_url_data = [
    ("https://youtu.be/yuH4iRcggMwdfg"),  # exception
    ("https://www.youtube.com/watch?v=yuH4iRcggMwds"),  # exception
    ("https://www.youtube.com/watch?v=yuH4iRcggMw&t==22s"),  # exception
    ("https://www.youtube.com/watch?v==yuH4iRcggMw&t=60s"),
]


@pytest.mark.parametrize("url, response", validate_url_data)
def test_get_time_info(url, response):
    """
     Test get_time_info with correct response.
     This is a wrapper around get_time_info to make sure we don't accidentally 
     get the same response for different url

     @param url - youtube video link
     @param response - video duration
    """
    assert get_time_info(url) == response


@pytest.mark.parametrize("url", invalid_url_data)
def test_get_time_info_failed(url):
    """
     Test get_time_info fails with InvalideURLException. 
     This is a test to make sure we don't get an exception when the URL is invalid

     @param URL - URL to get time
    """
    with pytest.raises(InvalideURLException):
        get_time_info(url)
