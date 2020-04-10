import multiprocessing as mp
from threading import Thread
import requests
import time


with open('urls.txt', 'r') as f:
    urls = [line.strip() for line in f.readlines()]  # strip '\n'


def fetch(url, result_dict):
    try:
        response = requests.get(url, timeout=3.0)  # aiohttp
    except Exception as e:
        print(f'ERROR: {e}')
    else:
        result_dict[url] = response.text


def multithtread_main():
    result_dict = {}

    threads = []
    for url in urls:
        t = Thread(target=fetch, args=(url, result_dict))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f'Fetched {len(result_dict)} of {len(urls)} urls')


def multiproc_main():
    # shared dict
    result_dict = mp.Manager().dict()

    # for url create process
    procs = []
    for url in urls:
        proc = mp.Process(target=fetch, args=(url, result_dict))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    print(f'Fetched {len(result_dict)} of {len(urls)} urls')


def sync_main():
    result_dict = {}
    for url in urls:
        fetch(url, result_dict)
    print(f'Fetched {len(result_dict)} of {len(urls)} urls')


if __name__ == "__main__":
    start = time.time()
    multithtread_main()
    end = time.time()
    print(f'Elapsed ({len(urls)} threads) {end - start}s')
