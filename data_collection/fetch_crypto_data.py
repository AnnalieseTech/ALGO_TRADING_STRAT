# fetch_coinmarketcap_data.py
import requests
import pandas as pd
from config import COINMARKETCAP_API_KEY, CRYPTOCOMPARE_API_KEY

def fetch_coinmarketcap_data(limit=10):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
    }
    parameters = {
        'start': '1',
        'limit': limit,
        'convert': 'USD'
    }
    response = requests.get(url, headers=headers, params=parameters)
    if response.status_code == 200:
        data = response.json()['data']
        df = pd.json_normalize(data)
        return df
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    data = fetch_coinmarketcap_data()
    if data is not None:
        data.to_csv('data/raw/coinmarketcap_data.csv', index=False)

def fetch_cryptocompare_data(limit=10):
    url = f'https://min-api.cryptocompare.com/data/top/mktcapfull?limit={limit}&tsym=USD'
    headers = {
        'authorization': f'Apikey {CRYPTOCOMPARE_API_KEY}',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['Data']
        df = pd.json_normalize(data)
        return df
    else:
        print(f"Error: {response.status_code}")
        return None
    
if __name__ == "__main__":
    data = fetch_cryptocompare_data()
    if data is not None:
        data.to_csv('data/raw/cryptocompare_data.csv', index=False)