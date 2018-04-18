from secrets import token_hex
import base58
import hashlib
import binascii


class Address(object):
    pass


def privatekeytowif(private_key=None):
    """
    receive private key and return WIF (Wallet Import Format )
    :param: str private key
    (if private key parameter is not passed, private key is
     generated automatically)
    :return: str wif
    """
    version = '80'
    if private_key is None:
        key = version + token_hex(32)
    else:
        if not isinstance(private_key, str):
            raise TypeError("a str-like object is required, not '%s'" %
                            type(private_key).__name__)
        if private_key[:2] != version:
            key = version + private_key
        else:
            key = private_key

    sha1 = hashlib.sha256(bytes(bytearray.fromhex(key))).hexdigest()
    sha2 = hashlib.sha256(bytes(bytearray.fromhex(sha1))).hexdigest()

    wif = key + sha2[:8]

    encoded_string = base58.b58encode(bytes.fromhex(wif))

    return encoded_string


def wiftoprivatekey(wif):
    """
    receive WIF and return private key
    :param wif: str
    :return: str
    """
    if not isinstance(wif, str):
        raise TypeError("a str-like object is required, not '%s'" %
                        type(wif).__name__)

    first_encode = base58.b58decode(wif)

    private_key_full = binascii.hexlify(first_encode)

    private_key = private_key_full[2:-8]

    return private_key.decode()
