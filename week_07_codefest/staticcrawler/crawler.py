from download import Downloader, DownloadError
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self, host, paths=('/',)):
        self.host = host
        self.paths = paths

    def images(self):
        yield from self.resources('img')

    def resources(self, tag):
        for path in self.paths:
            sources = self.extract_sources(path, tag)

            for src_path in sources:
                try:
                    resource = Downloader(self.host, src_path).get()
                except DownloadError as e:
                    print(f'* Error during resource download: {e}')
                    continue
                yield src_path, resource

    def extract_sources(self, path, tag):
        try:
            html = Downloader(self.host, path).get().data.decode('utf-8')
        except DownloadError as e:
            print(f'* Error during page download: {e}')
            return set()
        soup = BeautifulSoup(html, 'html.parser')

        resources = [resource['src'] for resource in soup(tag)
                     if not resource['src'].startswith('http')]

        return set(resources)


def test_Crawler():
    list(Crawler('www.netside.net').images())
