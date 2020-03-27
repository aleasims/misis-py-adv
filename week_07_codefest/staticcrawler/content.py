from collections import namedtuple
from enum import Enum, auto


Content = namedtuple('Content', ['type', 'data'])


class ContentType(Enum):
    HTML = auto()
    IMAGE = auto()

    @classmethod
    def from_str(cls, value):
        type_ = value.split(';')[0]
        if type_ == 'text/html':
            return cls.HTML
        elif type_.startswith('image/'):
            return cls.IMAGE
        else:
            ValueError(value)


def test_Content():
    Content(type=ContentType.HTML, data='Hello, world')
