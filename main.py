from web3 import Web3
from web3.middleware import geth_poa_middleware
from account_info import abi,contract_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract = w3.eth.contract(abi=abi,address=contract_address)
print(contract_address)
print(w3.eth.get_balance('0xfdE422E791E0999a10AA3800daF781b6B585Cf4f'))
print(w3.eth.get_balance('0xc47314E1A287150CCc0Ac2CC7b334B1Ff0e3bB91'))
print(w3.eth.get_balance('0x6ac3A303F1bfc15E2F578e6EEDa27c7fd3f5cAbb'))
print(w3.eth.get_balance('0xA7dF977c51B05a1fBa85adb8891250401f5f54F2'))
print(w3.eth.get_balance('0xce29EB0B780E1b94772Ac4C0a1be3daF3Eea705F'))