# Bitcoin Address and Transaction Checker

This Python script allows you to check the details of a Bitcoin wallet address or transaction ID using the BlockCypher API. It validates the input and fetches the relevant details, displaying them in json format.

## Features

- Validate Bitcoin wallet addresses and transaction IDs.
- Fetch and display wallet details such as balance, total received, total sent, and recent transactions.
- Fetch and display transaction details including inputs, outputs, and fees.

## Requirements

- Python 3.6+
- `requests` library
- `blockcypher` library

## Installation

1. Clone the repository:
    ```git clone https://github.com/yourusername/bitcoin-checker.git```
   
    ```cd bitcoin-checker```

3. Install the required libraries:
    ```
    pip install requests blockcypher
    ```

## Usage

To use the script, simply run the `index` function with a Bitcoin wallet address or transaction ID as the argument.

```python index.py```

## Example
# For a wallet address
main("34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo")

# For a transaction ID
main("0320ceb7b73dcc00a5b48cc853fd3dd16d0d1ca8130ad27acd15114927ad83d1")

## License
This project is licensed under the MIT License. See the LICENSE file for details.
