import requests


class CoinMarketCapAPI:
    def __init__(self, api_key):
        # Replace with your CoinMarketCap API key
        self.url = (
            'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        )
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': api_key,  # CMC API Key
        }

    def get_project_data(self, project_name):
        parameters = {
            'start': '1',
            'limit': '10',
            'convert': 'USD'
        }
        try:
            response = requests.get(self.url,
                                    headers=self.headers,
                                    params=parameters)
            data = response.json()

            for coin in data['data']:
                if coin['name'].lower() == project_name.lower():
                    return {
                        "name": coin['name'],
                        "symbol": coin['symbol'],
                        "price": coin['quote']['USD']['price'],
                        "market_cap": coin['quote']['USD']['market_cap'],
                        "total_supply": coin['total_supply']
                    }
            return None
        except Exception as e:
            print(f"Error fetching CoinMarketCap data: {e}")
            return None
