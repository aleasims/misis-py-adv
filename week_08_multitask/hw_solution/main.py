import argparse
import asyncio
import logging
import time
from io import BytesIO

import aiohttp
import requests
from PIL import Image, ImageOps

from fetch import FetchPool
from upload import UploadPool


def process(data: bytes) -> bytes:
    """Image processing function."""
    image = Image.open(BytesIO(data))
    image_mirror = ImageOps.mirror(image)
    buffer = BytesIO()
    image_mirror.save(buffer, format=image.format)
    return buffer.getvalue()


async def main(url: str, fetchers: int, uploaders: int):
    if not url.endswith('/'):
        url = url + '/'
    logger = logging.getLogger(__name__)

    try:
        response = requests.get(url)
        assert response.status_code == 200, f"{response.status_code} {response.reason}"
        images = response.text.split('\n')
    except (requests.RequestException, AssertionError) as err:
        logger.warning(f"Querying images - - [{err}]")
        return

    logger.info(f"Querying images - - [{response.status_code} {response.reason}]"
                f" found {len(images)} images")

    post_queue = asyncio.Queue()
    urls_queue = asyncio.Queue()
    for img in images:
        await urls_queue.put(url + img)

    async with aiohttp.ClientSession() as session:
        fetch_pool = FetchPool(fetchers, urls_queue, post_queue, session, process)
        upload_pool = UploadPool(uploaders, post_queue, url, session)
        start = time.perf_counter()
        await fetch_pool.run()
        await post_queue.join()
        passed = time.perf_counter() - start
        upload_pool.finish()
        logger.info(f"Passed {round(passed, 2)} sec")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help="url to find images")
    parser.add_argument('-v', help="enable verbosity", action='store_true')
    parser.add_argument('-f', '--fetchers', default=8, type=int,
                        help="number of fetchers (defaults to 8)")
    parser.add_argument('-u', '--uploaders', default=8, type=int,
                        help="number of uploaders (defaults to 8)")
    return parser.parse_args()


def setup_logger(verbosity: bool):
    level = logging.DEBUG if verbosity else logging.INFO
    log_format = "[ %(name)s ] - %(levelname)s - %(message)s"
    logging.basicConfig(level=level, format=log_format)


if __name__ == "__main__":
    args = parse_args()
    setup_logger(args.v)
    try:
        asyncio.run(main(args.url, args.fetchers, args.uploaders))
    except KeyboardInterrupt:
        print('Interrupted...')
