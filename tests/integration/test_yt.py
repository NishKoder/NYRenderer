import pytest
from NYRenderer import render_youtube_video
from NYRenderer.custom_exception import InvalideURLException

class TestYoutubeVideoRendered:
    validate_url_data = [
        ("https://youtu.be/yuH4iRcggMw", "success"),
        ("https://www.youtube.com/watch?v=yuH4iRcggMw", "success"),
        ("https://www.youtube.com/watch?v=yuH4iRcggMw&t=60s", "success"),
    ]

    invalid_url_data = [
        ("https://youtu.be/yuH4iRcggMwdfg"),  # exception
        ("https://www.youtube.com/watch?v=yuH4iRcggMwds"),  # exception
        ("https://www.youtube.com/watch?v=yuH4iRcggMw&t==22s"),  # exception
        ("https://www.youtube.com/watch?v==yuH4iRcggMw&t=60s"),
    ]

    @pytest.mark.parametrize("url, response", validate_url_data)
    def test_render_yt_success(self,url, response):
        assert render_youtube_video(url) == response

    @pytest.mark.parametrize("url", invalid_url_data)
    def test_render_yt_failed(self,url):
        with pytest.raises(InvalideURLException):
            render_youtube_video(url)

