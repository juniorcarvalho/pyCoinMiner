import unittest
import block
from datetime import datetime


class TestModelBlock(unittest.TestCase):
    def setUp(self):
        l = []
        l.append({'de': 'ninguem', 'para': 'minerador', 'valor': '50.00'})
        l.append({'de': 'minarador', 'para': 'alguem', 'valor': '20.00'})
        self.block = block.Block(version='1.0', difficulty=2, transaction=l)

    def testCountTransaction(self):
        self.assertEqual(len(self.block.transaction), 2)

    def testHash(self):
        self.assertEqual(self.block.hash, '02af3e9e143161063257c0924b8e5a2bc59bda0ba551a94eab0adca06b4ff823')

    def testData(self):
        self.assertNotEqual(self.block.timestamp, datetime.now())


if __name__ == '__main__':
    unittest.main()
