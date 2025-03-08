import time
from pybit.unified_trading import HTTP

api_key = "85WQVHsc8epCLTLcdm"
api_secret = "9kkbVM8oasMB9mGOgmD4lB7kAVx44YSKGIri"

session = HTTP(testnet=True, api_key=api_key, api_secret=api_secret)

while True:
    account_info = session.get_wallet_balance(accountType="UNIFIED")
    print(account_info)
    time.sleep(60)  # opakuje každou minutu
