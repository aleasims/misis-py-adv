import logging

import zmq

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def main():
    downloader = zmq.Context()
    input_socket = downloader.socket(zmq.PULL)
    input_socket.bind('tcp://*:5555')

    while True:
        data = input_socket.recv()
        logger.info(f'Received {len(data)} bytes')

    input_socket.close()
    downloader.destroy()


if __name__ == "__main__":
    main()
