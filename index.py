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


def convert_to_json(type, details):
    """
    """
    if type == Type.WALLET:
        json_response =  {
            "address": details.get("address"),
            "btc_balance": (details.get("balance") / 1e8),
            "total_btc_received": (details.get("total_received") / 1e8),
            "total_btc_sent": (details.get("total_sent") / 1e8),
            "transactions": []
        }
        for tx in details['txrefs'][:5]:
            transaction = {
                "tx_hash": tx.get("tx_hash"),
                "confirmations": tx.get("confirmations"),
                "btc_value": tx.get("value") / 1e8,
                "confirmed": tx.get("confirmed")
            }
            json_response["transactions"].append(transaction)

    elif type == Type.TXID:
        json_response = {
            "transaction_id": details.get('hash'),
            "block_height": details.get('block_height'),
            "total": details.get('total'),
            "fees": details.get('fees'),
            "confirmations": details.get('confirmations'),
            "inputs": [],
            "outputs": []
        }
        
        for inp in details.get('inputs', []):
            input = {
                "addresses": ', '.join(inp.get('addresses', [])),
                "btc_amount": inp.get('output_value')
            }
            json_response["inputs"].append(input)
            
            
        for out in details.get('outputs', []):
            output = {
                "addresses": ', '.join(out.get('addresses', [])),
                "btc_amount": out.get('value')
            }
            json_response["outputs"].append(output)
    
    print(json_response) # to display in console
    return json_response


def main(string):
    """
    Main function
    """
    string = "34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo" # wallet address sample
    # string = "0320ceb7b73dcc00a5b48cc853fd3dd16d0d1ca8130ad27acd15114927ad83d1" # txid sample
    # Detect if is wallet or txid
    if is_wallet(string):
        address_details = get_wallet_details(string)
        return convert_to_json(Type.WALLET, address_details)
    if is_txid(string):
        txid_details = get_txid_details(string)
        return convert_to_json(Type.TXID, txid_details)



if __name__ == "__main__":
    main("Hello, World!")
