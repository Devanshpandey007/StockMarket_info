import requests
from dotenv import load_dotenv
import os
class stock_data:
    def __init__(self):
        load_dotenv()
        self.alphavantage_API = os.getenv("ALPHAVANTAGE_API")
        self.company_data = None
        # self.start_day = '11'
        # self.end_day = '11'
        # self.month = '08'
        # self.year = '2023'

    def update_company_data(self, data):
        self.company_data = data

    def fetch_stock_data(self):
        srch_INDStock_url = 'https://www.alphavantage.co/query'
        srch_INDStock_para = \
            {
                'function': 'TIME_SERIES_DAILY',
                'symbol': self.company_data,
                'outputsize': 'full',
                'apikey': self.alphavantage_API
            }
        response0 = requests.get(srch_INDStock_url, params=srch_INDStock_para)
        self.report = response0.raise_for_status()
        self.j_data = response0.json()
        self.extract_data = self.j_data['Time Series (Daily)']
        self.extacted_data = list(self.extract_data.items())[:30]




