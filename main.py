import requests
import json
import os


def get_crypto_price(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd,eur"
    print(url)
    response = requests.get(url)
    data = response.json()
    if crypto in data:
        usd_price = data[crypto]['usd']
        eur_price = data[crypto]['eur']
        print(f"{crypto} price in USD: {data[crypto]['usd']}")
        print(f"{crypto} price in EUR: {data[crypto]['eur']}")

        if usd_price > eur_price:
           print(f"{crypto} is more expensive in USD: {usd_price}")
        else:
           print(f"{crypto} is more expensive in EUR: {eur_price}")
crypto = input("Enter Crypto name: ")
get_crypto_price(crypto)

