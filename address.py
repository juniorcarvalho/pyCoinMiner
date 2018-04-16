from secrets import token_hex


class Address(object):
    pass


def generate_address():
    """
    generete wallet address with 32 bytes
    :return: str
    """
    address = token_hex(32)
    return address.upper()
