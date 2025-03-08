import pybit
from pybit.unified_trading import HTTP

api_key = "85WQVHsc8epCLTLcdm"      # tvůj API klíč v uvozovkách
api_secret = "9kkbVM8oasMB9mGOgmD4lB7kAVx44YSKGIri"          # tvůj API Secret v uvozovkách

session = HTTP(api_key=api_key, api_secret=api_secret, testnet=True)

account_info = session.get_wallet_balance(accountType="UNIFIED")
print(account_info)
