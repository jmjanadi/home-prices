#!venv/bin/python3
''' Data retrieved from Zillow on 27 July 2023 '''

import requests
import pickle

wc_pages = ['**west-covina-urls**']
cv_pages = ['**covina-urls**']
gl_pages = ['**glendora-urls**']
az_pages = ['**azusa-urls**']
sd_pages = ['**san-dimas-urls**']
lv_pages = ['**la-verne-urls**']
cl_pages = ['**claremont-urls**']
bp_pages = ['**baldwin-park-urls**']

pages = wc_pages + cv_pages + gl_pages + az_pages + sd_pages + lv_pages + cl_pages + bp_pages

headers = {'Host': 'www.zillow.com',
           'User-Agent': '**user-agent**',
           'Accept': '*/*',
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept-Encoding': 'gzip, deflate, br',
           'Cookie': '**cookie**',
           'Sec-Fetch-Dest': 'empty',
           'Sec-Fetch-Mode': 'cors',
           'Sec-Fetch-Site': 'same-origin'}

responses = [requests.get(page, headers=headers) for page in pages]
json_pages = [response.json()['cat1']['searchResults']['listResults'] for response in responses]

with open('home_json_pages.pkl', 'wb') as f:
    pickle.dump(json_pages, f)
