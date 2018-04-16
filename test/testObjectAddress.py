import unittest
from address import generate_address


class TestObjectAddress(unittest.TestCase):
    def testGenerateAddress(self):
        self.assertEqual(len(generate_address()), 64)
