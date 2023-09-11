#!venv/bin/python3

import pickle
import os
import time
import requests
from bs4 import BeautifulSoup
import numpy as np

with open('home_json_pages.pkl', 'rb') as f:
    json_pages = pickle.load(f)

headers = {'Host': 'www.zillow.com',
           'User-Agent': '',
           'Accept': '*/*',
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept-Encoding': 'gzip, deflate, br',
           'Cookie': 'x-amz-continuous-deployment-state=AYABeOLvEMeid32gcCgCXQoYyYEAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADBds7liCqHTCU3M9iAAwqbSobkR6SrL5cZYih2Hvdr6zP6d4JA3NXeBoppKyHwB6+ghBrSdVN7CbIeTP2F9mAgAAAAAMAAQAAAAAAAAAAAAAAAAAADjvrHb+Nrlc1lT4lHHVp8P%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAyXd94aCHkXe2n2cPR%2F9ij%2FQSQm53CSovekf2wi; zguid=24|%245ed46b65-b087-498f-9d42-efdb9a4e42d0; zgsession=1|9df18f94-fd85-4e9e-9c69-94ed44332de8; x-amz-continuous-deployment-state=AYABeFQFzi85Qg611D1xn24HxVwAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADO4Ef30e7XjouG4iZAAwEbVYKxbdWABmisfjuKtcJZ1k06rpTivwV4AP94n6wOzaViv6mc2EA49i50109U0tAgAAAAAMAAQAAAAAAAAAAAAAAAAAALIBA2ORlwbdfYhxRT6QIR7%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAzXk72eSVifLwC3lAAey%2FkYosUz1R7xb0JoU5DF1R7xb0JoU5DF; zjs_anonymous_id=%225ed46b65-b087-498f-9d42-efdb9a4e42d0%22; zjs_user_id=null; zg_anonymous_id=%229df02ebb-96ee-445b-a727-daa99e65b8f3%22; g_state={"i_p":1690495521680,"i_l":1}; AWSALB=4QCYG5ir8UN3G9koFW63m+V6YQT/N4BbjkLN5Kf6B5yw0WwnRjoI4WTSt3pb9tHHlai6dTbMu3Cz92p/TA77wlknveXMXFMq3LhmH4v01c1kbwcyuZX/fuiI/pfk; AWSALBCORS=4QCYG5ir8UN3G9koFW63m+V6YQT/N4BbjkLN5Kf6B5yw0WwnRjoI4WTSt3pb9tHHlai6dTbMu3Cz92p/TA77wlknveXMXFMq3LhmH4v01c1kbwcyuZX/fuiI/pfk; JSESSIONID=889794AF55AEAA587060A490B355C909; search=6|1693080612278%7Crect%3D34.08772558670492%252C-117.75786093798828%252C34.00636725816871%252C-118.06753806201172%26rid%3D14542%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26z%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0914542%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09',
           'Sec-Fetch-Dest': 'empty',
           'Sec-Fetch-Mode': 'cors',
           'Sec-Fetch-Site': 'same-origin'}

user_agents = ['**user-agent1**',
                '**user-agent2**',
                '**user-agent3**']
headers['User-Agent'] = user_agents[0]

networks = ['**list-of-proxy-networks**']

with open('years_built.csv', 'w') as y:
    s = 0
    y.write('years,detailUrl\n')
    for json_page in json_pages:
        for j, home in enumerate(json_page):
            url = home['detailUrl']
            # change user agent every 10 homes
            if j%10 == 0:
                user_agent_idx = user_agents.index(headers['User-Agent'])
                if user_agent_idx == len(user_agents) - 1:
                    headers['User-Agent'] = user_agents[0]
                else:
                    headers['User-Agent'] = user_agents[user_agent_idx + 1]
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            result = soup.find_all('span', class_='Text-c11n-8-84-3__sc-aiai24-0 dpf__sc-2arhs5-3 hrfydd kOlNqB')
            # connect to a new proxy network if nothing is returned
            if len(result) == 0:
                os.system('**disconnect from current proxy network**')
                time.sleep(5)
                os.system(f'**connect to new proxy network**')
                time.sleep(5)
                s += 1
                if s == len(servers):
                    s = 0
                page = requests.get(url, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                result = soup.find_all('span', class_='Text-c11n-8-84-3__sc-aiai24-0 dpf__sc-2arhs5-3 hrfydd kOlNqB')
            print('User agent #' + str(user_agent_idx), end=', ')
            print('Length (' + str(len(result)), end='): ')
            if len(result) == 0:
                y.write('NA')
                print('NA')
            else:
                y.write(str(result[1].text.split()[-1]))
                print(result[1].text.split()[-1])
            y.write(',' + url + '\n')
            time.sleep(np.random.randint(3))
