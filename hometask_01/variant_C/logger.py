# import sys
# from datetime import datetime


class Logger:
    _logger = None
    template = '[{time}] {message}\n'

    def __init__(self, path: str = None):
        raise NotImplementedError

    def set_output(self, new_path: str = None):
        # self.stream = ?
        raise NotImplementedError

    @classmethod
    def get_logger(cls) -> 'Logger':
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    @staticmethod
    def time() -> float:
        raise NotImplementedError

    def write(self, message):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


def test():
    logger = Logger.get_logger()
    logger.write('Hello, world!')
    logger.set_output('test.log')
    logger.write('Hello, world!')
    assert repr(logger) == '<Logger test.log>'
    logger.close()


if __name__ == "__main__":
    test()
