import unittest
import block


class TestObjectBlock(unittest.TestCase):
    def setUp(self):
        l = []
        l.append({'de': 'ninguem', 'para': 'minerador', 'valor': '50.00'})
        l.append({'de': 'minerador', 'para': 'alguem', 'valor': '20.00'})
        self.block = block.Block(blockNumber=0,
                                 version='1.0',
                                 difficulty=2,
                                 timestamp='1523354307.041694',
                                 hashpreviousblock='0000000000000000000000000000000000000000000000000000000000000000',
                                 transaction=l)

    def testCountTransaction(self):
        self.assertEqual(len(self.block.transaction), 2)

    def testHashTransaction(self):
        self.assertEqual(self.block.hashTransaction, '1dc0949926b7b09341837d8fcb7b6f59b7fd4a4cd0fffca664e4665baae37c95')

    def testHashHeader(self):
        self.assertEqual(self.block.hashHeaderBlock, '9b4c54bc6074720495782a8f0d9eb11bd6dff93617f5b07cd7ad7a92d0afdc72')

    def testGetTimestamp(self):
        self.assertIsNotNone(block.get_timestamp(self))

    def testCheckTargetIsTrue(self):
        self.assertTrue(block.check_target(2, '004c54bc6074720495782a8f0d9eb11bd6dff93617f5b07cd7ad7a92d0afdc72'))

    def testCheckTargetNotTrue(self):
        self.assertFalse(block.check_target(2, '114c54bc6074720495782a8f0d9eb11bd6dff93617f5b07cd7ad7a92d0afdc72'))

    def testMine(self):
        self.assertTrue(block.mine(self.block))

if __name__ == '__main__':
    unittest.main()
