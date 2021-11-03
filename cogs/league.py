import json
import os
import sys
from random import randint
import datetime

import discord
from discord.ext import commands
from pycoingecko import CoinGeckoAPI

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Add it and try again.")
else:
    with open("config.json", encoding="cp866") as file:
        config = json.load(file)

class Price(commands.Cog, name="price"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="price",
                      description=f"Shows the current price of a token. (Price, 24H Change %, 24H High, 24H Low). Syntax: '<prefix>price <token symbol>'")
    async def price(self, context, symbol: str):
        cg = CoinGeckoAPI()
        coin_list = cg.get_coins_list()
        d = {}
        for coin in coin_list:
            d[coin['symbol']] = coin['id']

        # now use d['btc'] to search
        token_name = d[symbol]
        coin = cg.get_coin_by_id(id=token_name)

        embed = discord.Embed(color=randint(0, 0xffff), description=f"**{coin['name']}**")
        embed.add_field(name='$USD', value=f"${(round(coin['market_data']['current_price']['usd'], 2))}", inline=False)
        embed.add_field(name=':chart_with_upwards_trend: 24h Change Percentage',
                        value=f"{(round(coin['market_data']['price_change_percentage_24h'], 2))}%", inline=False)
        embed.add_field(name=':chart_with_upwards_trend: 24h High', value=f"**$ USD:** {coin['market_data']['high_24h']['usd']}\n")
        embed.add_field(name=':chart_with_downwards_trend: 24h Low', value=f"**$ USD:** {coin['market_data']['low_24h']['usd']}\n")

        embed.timestamp = datetime.datetime.now()
        await context.reply(content=context.message.author.mention, embed=embed)
        return


def setup(bot):
    bot.add_cog(Price(bot))
