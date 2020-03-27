import os
from contextlib import contextmanager


class Storage:
    def __init__(self, outdir):
        self.outdir = outdir
        os.makedirs(self.outdir, exist_ok=True)
        self.subdir = None

    @property
    def path(self):
        if self.subdir is not None:
            return os.path.join(self.outdir, self.subdir)
        return self.outdir

    def save(self, filename, data):
        filedir = os.path.join(self.path, os.path.dirname(filename))
        os.makedirs(filedir, exist_ok=True)
        with open(os.path.join(self.path, *filename.split('/')), 'wb') as f:
            f.write(data)

    @contextmanager
    def subpath(self, path):
        self.subdir = path
        os.makedirs(os.path.join(self.outdir, self.subdir), exist_ok=True)
        yield
        self.subdir = None
