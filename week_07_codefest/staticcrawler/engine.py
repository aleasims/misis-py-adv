from typing import Iterable
from crawler import Crawler
from storage import Storage


class Engine:
    def __init__(self, hosts: Iterable, outdir='out'):
        self.storage = Storage(outdir)
        self.hosts = hosts

    def start(self):
        for host in self.hosts:
            with self.storage.subpath(host):
                self.process(host)

    def process(self, host):
        for name, content in Crawler(host).images():
            try:
                self.storage.save(name, content.data)
            except Exception as e:
                print(f'* Error during saving: {e}')


def test_Engine():
    Engine(['www.netside.net', 'www.tim.org']).start()
