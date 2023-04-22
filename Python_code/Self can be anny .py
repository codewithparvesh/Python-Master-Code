import requests
from bs4 import BeautifulSoup
import json
import csv

query = 'site:youtube.com openinapp.co'
url = f'https://www.google.com/search?q={query}&num=10000'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

results = []

for g in soup.find_all('div', class_='g'):
    anchors = g.find_all('a')
    if anchors:
        link = anchors[0]['href']
        if 'youtube.com/channel/' in link:
            channel_id = link.split('/channel/')[1]
            results.append({'channel_id': channel_id, 'link': link})

with open('results.json', 'w') as f:
    json.dump(results, f)

with open('results.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['channel_id', 'link'])
    for result in results:
        writer.writerow([result['channel_id'], result['link']])
