import unittest
from block import Block, get_timestamp, check_target, mine


class TestObjectBlock(unittest.TestCase):
    def setUp(self):
        l = [{'de': 'minerador', 'para': 'alguem', 'valor': '2.00'}]
        self.block = Block(blocknumber=1,
                           version='1.0',
                           difficulty=2,
                           timestamp='1523354307.041694',
                           hashpreviousblock='0' * 64,
                           transaction=l)

    def testCountTransaction(self):
        self.assertEqual(len(self.block.transaction), 2)

    def testHashTransaction(self):
        self.assertEqual(self.block.hashTransaction, '07e0214b39f6681bda0f4dbd3a828a912ed8155fb289b3f892c92f537766ec95')

    def testHashHeader(self):
        self.assertEqual(self.block.hashHeaderBlock, '0c5f1c48651a310e2f0d3630e5dc63af1cbd9c0bea5009376ee15ece109f024e')

    def testGetTimestamp(self):
        self.assertIsNotNone(get_timestamp())

    def testCheckTargetIsTrue(self):
        self.assertTrue(check_target(2, '004c54bc6074720495782a8f0d9eb11bd6dff93617f5b07cd7ad7a92d0afdc72'))

    def testCheckTargetNotTrue(self):
        self.assertFalse(check_target(2, '114c54bc6074720495782a8f0d9eb11bd6dff93617f5b07cd7ad7a92d0afdc72'))

    def testMine(self):
        self.assertTrue(mine(self.block))


if __name__ == '__main__':
    unittest.main()
