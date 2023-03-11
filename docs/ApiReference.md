# API Reference

## Rendereing Youtube Video

### Short example
```python
from NYRenderer import render_youtube_video
URL = "https://youtu.be/yuH4iRcggMw"
render_youtube_video(URL, width = 780, height =600)
```


    Args:
        url (str): The URL of the Youtube video to render.
        width (int): The width of the video in pixels. Default is 780.
        height (int): The height of the video in pixels. Default is 600.

    Returns:
        Success



## Rendering reference website

```python
from NYRenderer import render_site
URL = "http://pytorch.org/"
render_site(URL, width = 780, height =600)
```

    Parameters:
    ----------
    URL : str
        The URL of the webpage to be rendered.

    Returns:
    -------
    Success

    Result:
    -------------
    Displays the rendered webpage in a window.

    Example:
    --------
    >>> from NYRenderer import render_site
    >>> URL = "http://pytorch.org/"
    >>> render_site(URL)
