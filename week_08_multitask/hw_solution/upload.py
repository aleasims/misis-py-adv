import asyncio
import logging
from collections import Counter

import aiohttp


class UploadPool:
    """Asynchronous uploading pool.

    Args:
        size: size of the pool.
        input_: input queue with data to send.
        url: output URL to post results.
        session: session to use for fetching.
        max_retry: maximum number of retries for URL in case of error.
    """
    def __init__(self, size: int, input_: asyncio.Queue, url: str,
                 session: aiohttp.ClientSession,
                 max_retry: int = 3):
        self.url = url
        self.size = size
        self.input = input_
        self.session = session
        self.max_retry = max_retry

        self.logger = logging.getLogger(__name__)
        self.tasks = [asyncio.create_task(self.upload())
                      for _ in range(self.size)]
        self.errors = Counter()
        self.total_num = 0

    def finish(self):
        """Cancel all running tasks."""
        for task in self.tasks:
            task.cancel()
        self.logger.info(f"Uploading completed "
                         f"({self.total_num} succeed, {len(self.errors)} errors)")

    async def upload(self):
        """Upload coroutine.

        Get data from `input` queue and POST it to given `url`,
        until input queue is not empty.
        """
        while True:
            data = await self.input.get()

            try:
                async with self.session.post(self.url, data=data) as resp:
                    if resp.status != 200:
                        raise aiohttp.ClientError(f"{resp.status} {resp.reason}")
                    if hash(data) in self.errors:
                        del self.errors[hash(data)]
                    else:
                        self.total_num += 1

                    self.logger.debug(f"POST {self.url} - - [{resp.status} {resp.reason}]"
                                      f" {len(data)} bytes")

            except aiohttp.ClientError as err:
                self.errors[hash(data)] += 1
                if self.errors[data] < self.max_retry:
                    self.logger.debug(f"POST {self.url} - - [ERROR: {err}] - - retrying")
                    await self.input.put(data)
                else:
                    self.logger.warning(f"POST {self.url} - - [ERROR: {err}]")
            finally:
                self.input.task_done()
