from web3 import Web3

ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))
account_1 = '0xB17f8F8f2c4D8f7602aa335d85e032FD4e8986e7'
private_key1 = '1c54d075c700dbdedb073c86909e329a3ea0759d85773714253f0cab50766b0e'
account_2 = '0x6F8591E22cCa9091B6db06218dceD888A31b44d1'

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(50, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.sign_transaction(tx, private_key1)

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash))