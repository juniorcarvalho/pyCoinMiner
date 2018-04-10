"""
  Block Object
"""
import hashlib
from datetime import datetime


class Block(object):
    def __init__(self, blockNumber, version, difficulty, timestamp, hashpreviousblock, transaction=[]):
        self.blockNumber = blockNumber
        self.version = version
        self.difficulty = difficulty
        self.timestamp = timestamp
        self.transaction = transaction
        self.hashPreviousBlock = hashpreviousblock
        self.nonce = 0
        self.get_hash()

    def get_hash(self):
        temp = ''
        for l in self.transaction:
            for v in l.values():
                temp += v

        h = hashlib.sha256()
        h.update(temp.encode())
        self.hashTransaction = h.hexdigest()

        h = hashlib.sha256()
        temp = self.version + self.hashPreviousBlock + self.hashTransaction + \
               str(self.timestamp) + str(self.difficulty) + str(self.nonce)
        h.update(temp.encode())
        self.hashHeaderBlock = h.hexdigest()


def get_timestamp(self):
    dtbase = datetime(1970, 1, 1, 0, 0, 0)
    dtnow = datetime.now()
    return (dtnow - dtbase).total_seconds()


def mine(block):
    ok = False
    i = 0
    while ok != True:
        block.nonce = i
        block.get_hash()
        if check_target(block.difficulty, block.hashHeaderBlock):
            return True
        else:
            i += 1


def check_target(difficulty, hash):
    return hash[:difficulty] == ('0' * difficulty)
