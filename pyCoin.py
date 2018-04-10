from block import Block, get_timestamp, mine


def main():
    transactions = [{'de': 'ninguem', 'para': 'minerador', 'valor': '100.00'}]

    # block genesis
    block0 = Block(blocknumber=0, version='1.0', difficulty=2,
                   timestamp=get_timestamp(),
                   transaction=transactions,
                   hashpreviousblock='0000000000000000000000000000000000000000000000000000000000000000')

    mine(block0)
    print('Bloco 0 minerado - nonce: ' + str(block0.nonce))

    # block 1
    transactions = [{'de': 'minerador', 'para': 'joao', 'valor': '1.00'},
                    {'de': 'minerador', 'para': 'maria', 'valor': '5.00'},
                    {'de': 'minerador', 'para': 'helena', 'valor': '1.00'}]

    block1 = Block(blocknumber=0, version='1.0', difficulty=2,
                   timestamp=get_timestamp(),
                   transaction=transactions,
                   hashpreviousblock=block0.hashHeaderBlock)
    mine(block1)
    print('Bloco 1 minerado - nonce: '+str(block1.nonce))


if __name__ == '__main__':
    main()
