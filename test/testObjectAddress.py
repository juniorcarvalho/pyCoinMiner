import unittest
from address import privatekeytowif, wiftoprivatekey


class TestPrivateKeyToWif(unittest.TestCase):
    def setUp(self):
        self.private_key = '0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D'
        self.wif = '5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ'

    def testPrivateKeyToWif(self):
        wif = privatekeytowif(self.private_key)
        self.assertEqual(wif, self.wif)

    def testTypeParamError(self):
        self.assertRaises(TypeError, lambda: privatekeytowif(1))


class TestWifToPrivateKey(unittest.TestCase):
    def setUp(self):
        self.private_key = '0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D'
        self.wif = '5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ'

    def testWifToPrivateKey(self):
        private_key = wiftoprivatekey(self.wif)
        self.assertEqual(private_key.upper(), self.private_key)

    def testTypeParamError(self):
        self.assertRaises(TypeError, lambda: wiftoprivatekey(1))
