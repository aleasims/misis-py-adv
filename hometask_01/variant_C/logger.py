# import sys
# from datetime import datetime


class Logger:
    _logger = None
    template = '[{time}] {message}\n'

    def __init__(self, path=None):
        raise NotImplementedError

    def set_output(self, new_path=None):
        # self.stream = ?
        raise NotImplementedError

    @classmethod
    def get_logger(cls) -> 'Logger':
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    @staticmethod
    def time() -> str:
        raise NotImplementedError

    def write(self, message):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


def test():
    logger = Logger.get_logger()
    logger.write('Hello, world!')  # must print 'Hello, world!' to console
    logger.set_output('test.log')
    logger.write('Hello, world!')  # must print 'Hello, world!' to file test.log
    assert repr(logger) == '<Logger test.log>'
    logger.close()


if __name__ == "__main__":
    test()
