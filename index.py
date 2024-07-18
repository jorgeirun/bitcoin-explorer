import re
from enum import Enum
from blockcypher import get_address_details, get_transaction_details

# Docs: https://github.com/blockcypher/blockcypher-python

class Type(Enum):
    WALLET = 'wallet'
    TXID = 'txid'

def is_wallet(string):
    """
    Checks if the wallet address is valid.
    """
    if len(string) < 26 or len(string) > 35:
        return False
    if not re.match(r'^[123bc][1-9A-HJ-NP-Za-km-z]{25,34}$', string):
        return False
    return True


def get_wallet_details(address):
    """
    Makes a request using blockcypher to get address details.
    """
    try:
        return get_address_details(address)
    except Exception as e:
            return {"error": str(e)}


def is_txid(string):
    """
    Checks if the txid is a 64-character hexadecimal string
    """
    if re.fullmatch(r'[0-9a-fA-F]{64}', string):
        return True
    else:
        return False


def get_txid_details(txid, coin_symbol = 'btc'):
    """
    Makes a request using blockcypher to get txid details. BTC by default
    """
    try:
        return get_transaction_details(txid, coin_symbol=coin_symbol)
    except Exception as e:
        return {"error": str(e)}


def display_details(type, details):
    """
    Output wallet or transaction details in console
    """
    if type == Type.WALLET:
        print(f"Address: {details['address']}")
        print(f"Balance: {details['balance'] / 1e8 } BTC")
        print(f"Total Received: {details['total_received'] / 1e8 } BTC")
        print(f"Total Sent: {details['total_sent'] / 1e8 } BTC")
        print("")
        print("Transactions:")
        print("------")
        for tx in details['txrefs'][:5]:
            print(f"Tx Hash: {tx['tx_hash']}")
            print(f"Confirmations: {tx['confirmations']}")
            print(f"Value: {tx['value'] / 1e8 } BTC")
            print(f"Confirmed: {tx['confirmed']}")
            print("")
    elif type == Type.TXID:
        print(f"Transaction ID: {details.get('hash')}")
        print(f"Block Height: {details.get('block_height')}")
        print(f"Total Amount: {details.get('total') / 1e8} BTC")  # Convert from satoshis to BTC
        print(f"Fees: {details.get('fees') / 1e8} BTC")  # Convert from satoshis to BTC
        print(f"Confirmations: {details.get('confirmations')}")
        print("------")
        print("\nInputs:")
        for inp in details.get('inputs', []):
            addresses = inp.get('addresses', [])
            value = inp.get('output_value') / 1e8  # Convert from satoshis to BTC
            print(f"  Addresses: {', '.join(addresses)}")
            print(f"  Amount: {value} BTC")
        print("\nOutputs:")
        for out in details.get('outputs', []):
            addresses = out.get('addresses', [])
            value = out.get('value') / 1e8  # Convert from satoshis to BTC
            print(f"  Addresses: {', '.join(addresses)}")
            print(f"  Amount: {value} BTC")


def main(string):
    """
    Main function
    """
    # string = "34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo" # address sample
    string = "0320ceb7b73dcc00a5b48cc853fd3dd16d0d1ca8130ad27acd15114927ad83d1" # txid sample
    # Detect if is wallet or txid
    if is_wallet(string):
        address_details = get_wallet_details(string)
        display_details(Type.WALLET, address_details)
    if is_txid(string):
        txid_details = get_txid_details(string)
        display_details(Type.TXID, txid_details)



if __name__ == "__main__":
    main("Hello, World!")
