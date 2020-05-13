import asyncio
import logging
from typing import Callable
from collections import Counter

import aiohttp


class FetchPool:
    """Asynchronous fetching pool.

    Args:
        size: size of the pool.
        input_: input queue with URLs to fetch from.
        output: output queue to store results.
        session: session to use for fetching.
        processor: post-download processing function (if needed).
        max_retry: maximum number of retries for URL in case of error.
    """
    def __init__(self, size: int, input_: asyncio.Queue, output: asyncio.Queue,
                 session: aiohttp.ClientSession,
                 processor: Callable = None,
                 max_retry: int = 3):
        self.size = size
        self.input = input_
        self.output = output
        self.session = session
        self.processor = processor
        self.max_retry = max_retry
        self.logger = logging.getLogger(__name__)
        self.tasks = [asyncio.create_task(self.fetch())
                      for _ in range(self.size)]
        self.errors = Counter()
        self.total_num = 0

    async def run(self):
        """Main coroutine.

        Gathers all coroutines in pool.
        """
        self.logger.info(f"Start fetching ({len(self.tasks)} workers)")
        await asyncio.gather(*self.tasks)
        self.logger.info(f"Fetching completed "
                         f"({self.total_num} fetched, {len(self.errors)} errors)")

    async def fetch(self):
        """Fetch coroutine.

        Get URL from `input` queue, fetch, and put in `output` queue,
        until input queue is not empty.
        """
        while True:
            try:
                url = self.input.get_nowait()
            except asyncio.QueueEmpty:
                break

            try:
                async with self.session.get(url) as resp:
                    if resp.status != 200:
                        raise aiohttp.ClientError(f"{resp.status} {resp.reason}")
                    if url in self.errors:
                        del self.errors[url]
                    else:
                        self.total_num += 1

                    data = await resp.read()

                    if self.processor is not None:
                        size = len(data)
                        try:
                            data = self.processor(data)
                            self.logger.debug(f"GET {url} - - [{resp.status} {resp.reason}]"
                                              f" {size} bytes -> {len(data)} bytes")
                        except Exception as e:
                            self.logger.warning(f"GET {url} - - [PROCESSING ERROR: {e}]")
                            self.errors[url] += 1
                    else:
                        self.logger.debug(f"GET {url} - - [{resp.status} {resp.reason}]"
                                          f" {len(data)} bytes")

                    await self.output.put(data)

            except aiohttp.ClientError as err:
                self.errors[url] += 1
                if self.errors[url] < self.max_retry:
                    self.logger.debug(f"GET {url} - - [ERROR: {err}] - - retrying")
                    await self.input.put(url)
                else:
                    self.logger.warning(f"GET {url} - - [ERROR: {err}]")
