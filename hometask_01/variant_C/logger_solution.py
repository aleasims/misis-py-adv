import sys
from datetime import datetime


class Logger:
    _logger = None
    template = '[{time}] {message}\n'

    def __init__(self, path: str = None):
        self.path = path
        self.set_output(path)

    def set_output(self, new_path: str = None):
        self.close()
        self.path = new_path
        if self.path is None:
            self.stream = sys.stdout
        else:
            self.stream = open(self.path, 'a')

    @classmethod
    def get_logger(cls):
        if cls._logger is None:
            cls._logger = Logger()
        return cls._logger

    def __repr__(self):
        path = 'stdout' if self.path is None else self.path
        return '<Logger {}>'.format(path)

    @staticmethod
    def time() -> str:
        return str(datetime.now())

    def write(self, message):
        message = self.template.format(time=self.time(),
                                       message=message)
        print(message, file=self.stream, end='')

    def close(self):
        if self.path is not None:
            self.stream.close()


def test():
    logger = Logger.get_logger()
    logger.write('Hello, world!')  # must print 'Hello, world!' to console
    logger.set_output('test.log')
    logger.write('Hello, world!')  # must print 'Hello, world!' to test.log
    assert repr(logger) == '<Logger test.log>'
    logger.close()


if __name__ == "__main__":
    test()
