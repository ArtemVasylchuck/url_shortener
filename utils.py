def url_beatify(url: str) -> str:
    if url.startswith("http://") or url.startswith("https://"):
        return url
    else:
        return "https://{}".format(url)


def make_absolute_path_from_uri(uri: str) -> str:
    return "http://127.0.0.1:5000/s/{}".format(uri)


