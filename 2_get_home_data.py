#!venv/bin/python3
''' Data retrieved from Zillow on 27 July 2023 '''

import pickle
import numpy as np
import pandas as pd

with open('home_json_pages.pkl', 'rb') as f:
    json_pages = pickle.load(f)

features = {'zipcode': [],
            'city': [],
            'latitude': [],
            'longitude': [],
            'price': [],
            'bathrooms': [],
            'bedrooms': [],
            'livingArea': [],
            'homeType': [],
            'lotAreaValue': [],
            'lotAreaUnit': [],
            'detailUrl': []}

for json_page in json_pages:
    for home in json_page:
        for feature in features:
            if feature == 'detailUrl':
                features[feature].append(home[feature])
            elif feature in home['hdpData']['homeInfo']:
                features[feature].append(home['hdpData']['homeInfo'][feature])
            else:
                features[feature].append(np.nan)

df = pd.DataFrame(features, columns=features.keys())
df.to_csv('home_data.csv')
print('done')
