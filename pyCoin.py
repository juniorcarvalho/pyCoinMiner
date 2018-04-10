import block


def main():
    transactions = []
    transactions.append({'de': 'ninguem', 'para': 'minerador', 'valor': '100.00'})

    ## bloco genesis
    block0 = block.Block(blockNumber=0, version='1.0', difficulty=2, timestamp=block.get_timestamp(0),
                         transaction=transactions,
                         hashpreviousblock='0000000000000000000000000000000000000000000000000000000000000000')

    if block.mine(block0):
        print('Bloco 0 minerado - nonce: '+str(block0.nonce))
    else:
        print('Bloco 0 inválido')

    ## bloco 1
    transactions = []
    transactions.append({'de': 'ninguem', 'para': 'minerador', 'valor': '50'})
    transactions.append({'de': 'minerador', 'para': 'joao', 'valor': '1.00'})
    transactions.append({'de': 'minerador', 'para': 'maria', 'valor': '5.00'})
    transactions.append({'de': 'minerador', 'para': 'helena', 'valor': '1.00'})

    block1 = block.Block(blockNumber=0, version='1.0', difficulty=2, timestamp=block.get_timestamp(0),
                         transaction=transactions,
                         hashpreviousblock=block0.hashHeaderBlock)

    if block.mine(block1):
        print('Bloco 1 minerado - nonce: '+str(block1.nonce))
    else:
        print('Bloco 1 inválido')










if __name__ == '__main__':
    main()
