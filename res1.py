import requests
from bs4 import BeautifulSoup
import json
import csv

class GoogleScraper:
    base_url = 'https://www.google.com/async/lr_sma_tb'

    params = {
        'vet': '12ahUKEwjz9rv-o43xAhXRpYsKHeOfDbQQo-sBegQIARAr..i',
        'ei': 'SSLCYOz8Muj1qwGA67TIBA',
        'yv': 3,
        'q': '',
        'async': 'ct:BY,hl:ru,tz:Europe/Minsk,dtoint:2021-06-03T17:00:00Z,dtointmid:/m/037mp6,emid:/m/037mp6,et:tm,gndr:UNKNOWN_GENDER,lmid:/m/01l10v,rtab:3,sp:2,_fmt:prog,_id:tab-2-3',
    }

    def fetch(self):
        return requests.get(self.base_url, self.params)
        # print(response)

    def store_response(self, response):
        if response.status_code == 200:
            print('Saving')

            with open('res1.html', 'w', encoding="utf-8") as html_file:
                html_file.write(response.text)

            print('Done')
        else:
            print('Bad response')

    def run(self): 
        response = self.fetch()
        self.store_response(response)

if __name__ == '__main__':
    scraper = GoogleScraper()
    scraper.run()

