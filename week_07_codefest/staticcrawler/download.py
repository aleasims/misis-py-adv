from urllib.parse import ParseResult, urlunparse

import pytest
import requests
from requests.exceptions import RequestException

from content import Content, ContentType


class DownloadError(Exception):
    pass


class Downloader:
    def __init__(self, host, path='/'):
        self.host = host
        self.path = path

    @property
    def url(self):
        # 'google.com', '/home' -> 'http://google.com/home'
        # scheme, netloc, path, params, query, fragment
        parts = ParseResult(scheme='http',
                            netloc=self.host,
                            path=self.path,
                            params=None,
                            query=None,
                            fragment=None)
        return urlunparse(parts)

    def get(self) -> Content:
        try:
            response = requests.get(self.url)
        except RequestException as e:
            raise DownloadError(e)

        if response.status_code != 200:
            raise DownloadError(f'Code {response.status_code}')

        return self.parse_response(response)

    def parse_response(self, reps):
        data = reps.content
        type_ = ContentType.from_str(reps.headers['content-type'])
        return Content(type=type_, data=data)


def test_Downloader():
    content = Downloader('google.com').get()
    assert content.type == ContentType.HTML


def test_Downloader_notfound():
    with pytest.raises(DownloadError):
        Downloader('google.com', 'sajdfask').get()


def test_Downloader_fail():
    with pytest.raises(DownloadError):
        Downloader('googooggoooggle.com').get()
