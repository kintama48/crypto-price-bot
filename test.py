from pycoingecko import  CoinGeckoAPI

cg = CoinGeckoAPI()
coin_list = cg.get_coins_list()
d = {}
for coin in coin_list:
    d[coin['symbol']] = coin['id']

# now use d['btc'] to search

coin = cg.get_coin_by_id(id=d['algo'])
print(coin)

# id = d['algo']
#
# print(cg.get_price(ids=d['algo'], vs_currencies='usd')[id]['usd'])
# print(cg.get_price(ids=d['eth'], vs_currencies='usd'))
