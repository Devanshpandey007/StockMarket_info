import requests
from dotenv import load_dotenv
import os
class News:
    def __init__(self,com,dat):
        load_dotenv()
        self.com = com
        self.dat = dat
        news_API = os.getenv("NEWS_API")
        self.url_top_headlines = 'https://newsapi.org/v2/top-headlines'
        self.url_allabout ='https://newsapi.org/v2/everything'
        self.choosen_url = self.url_top_headlines
        self.company = self.com
        self.date = self.dat
        self.country = 'india'

        parameters1 = {'q':self.company,
                       'from':self.date,
                       'sortBy':'publishAt',
                       'apiKey':news_API
        }
        response = requests.get(self.choosen_url,params=parameters1)
        self.r_json = response.json()
