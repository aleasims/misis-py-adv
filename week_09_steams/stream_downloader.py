import logging
import requests
import zmq

from stream_handler import StreamHandler

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class StreamDownloader(StreamHandler):
    def __init__(self, url, output):
        response = requests.get(url, stream=True)

        self.stream_end = False
        super().__init__(response.iter_content(chunk_size=self.CHUNK_SIZE),
                         output)

    def write(self, data):
        # Try sending through socket
        try:
            self.output.send(data)
        except AttributeError:
            # If output is not a socker, use defined write
            super().write(data)

    def read(self):
        # Obtain data from iterator
        try:
            data = next(self.input)
        except StopIteration:
            self.stream_end = True
            data = b''
            logger.info('Stream ended')
        return data

    def completed(self):
        return self.stream_end


def download(url, zmq_port=5555):
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.connect('tcp://localhost:5555')

    downloader = StreamDownloader(url, socket)
    downloader.run()

    socket.close()
    context.destroy()


if __name__ == "__main__":
    download('http://142.93.138.114/earth.mp4')
