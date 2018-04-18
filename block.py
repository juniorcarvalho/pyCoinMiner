"""
  Block Object
  Utility Methods
"""
import hashlib
from datetime import datetime


class Block(object):
    def __init__(self, blocknumber, version, difficulty, timestamp,
                 hashpreviousblock, transaction=[]):
        self.blockNumber = blocknumber
        self.version = version
        self.difficulty = difficulty
        self.timestamp = timestamp
        self.transaction = transaction
        self.hashPreviousBlock = hashpreviousblock
        self.nonce = 0
        self.hashTransaction = ''
        self.hashHeaderBlock = ''
        self.get_hash()
        # reward transaction for the miner
        if blocknumber != 0:
            self.transaction.append({'de': 'ninguem', 'para': 'minerador', 'valor': '25'})

    def get_hash(self):
        """generates hash"""
        temp = ''
        for l in self.transaction:
            for v in l.values():
                temp += v

        self.hashTransaction = hashlib.sha256(temp.encode()).hexdigest()

        temp = (self.version + self.hashPreviousBlock + self.hashTransaction +
                str(self.timestamp) + str(self.difficulty) + str(self.nonce))

        self.hashHeaderBlock = hashlib.sha256(temp.encode()).hexdigest()


def get_timestamp():
    """returns number of seconds so far"""
    dtbase = datetime(1970, 1, 1, 0, 0, 0)
    dtnow = datetime.now()
    return (dtnow - dtbase).total_seconds()


def mine(block):
    """mining process
        :param Block block: block to mine
        :return bol
    """
    ok = False
    i = 0
    while ok is not True:
        block.nonce = i
        block.get_hash()
        if check_target(block.difficulty, block.hashHeaderBlock):
            return True
        else:
            i += 1


def check_target(difficulty, hash):
    """checks whether hash contains a certain number of zeros at the beginning
        params:
        :param int difficulty: difficulty applied
        :param str hash: hash to test
        :return bol
    """
    return hash[:difficulty] == ('0' * difficulty)
