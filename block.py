"""
  Block Object
"""
import hashlib
from datetime import datetime


class Block(object):
    def __init__(self, version, difficulty, transaction=[]):
        self.version = version
        self.difficulty = difficulty
        self.transaction = transaction
        self.get_timestamp()
        self.get_hash()

    def get_hash(self):
        str = ''
        for l in self.transaction:
            for v in l.values():
                str += v

        h = hashlib.sha256()
        h.update(str.encode())
        self.hash = h.hexdigest()

    def get_timestamp(self):
        dtbase = datetime(1970, 1, 1, 0, 0, 0)
        dtnow = datetime.now()
        self.timestamp = (dtnow - dtbase).total_seconds()

    def get_nonce(self):
        self.nonce = None
