import requests
from bs4 import BeautifulSoup
import json
import csv

class GoogleScraper:
    base_url = 'https://www.google.com/search'

    params = {
        'q': '',
        'cp': 0,
        'client': 'desktop-gws-wiz-on-focus-serp',
        'xssi': 't',
        'gs_ri': 'gws-wiz',
        'hl': 'ru-BY',
        'authuser': 0,
        'pq': 'turkey national football team',
        'psi': 'uwXCYPTnN8T9rgTQ0InYAg.1623328190963',
        'ofp': 'EAE',
        'dpr': 1,
    }

    def fetch(self, query):
        self.params['q'] = query
        return requests.get(self.base_url, self.params)
        # print(response)

    def store_response(self, response):
        if response.status_code == 200:
            print('Saving')

            with open('res.html', 'w', encoding="utf-8") as html_file:
                html_file.write(response.text)

            print('Done')
        else:
            print('Bad response')

    def run(self): 
        response = self.fetch('turkey national football team')
        self.store_response(response)

if __name__ == '__main__':
    scraper = GoogleScraper()
    scraper.run()

