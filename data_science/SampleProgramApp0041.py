print("=========== NETWORK API =================")

import requests

PARAMS = {'bibkeys': 'ISBN:1718500521', 'format': 'json'}
result = requests.get('http://openlibrary.org/api/books', params = PARAMS)
print(result)
print(result.reason)
print(result.request)
print(result.status_code)
print(result.headers)
print(result.raw)

print("1 => ------------------------------------")
print("1 => urllib3 ----------------------------")
import urllib3
http = urllib3.PoolManager()
# r = http.request('GET', 'http://localhost/excerpt.txt')
# https://raw.githubusercontent.com/finxter/FinxterTutorials/main/nlights.txt
r = http.request('GET', 'https://raw.githubusercontent.com/finxter/FinxterTutorials/main/nlights.txt')
for i, line in enumerate(r.data.decode('utf-8').split('\n')):
    if line.strip():
        print("Line %i: " %(i), line.strip())


print("2 => ------------------------------------")
print("2 => - Запросы API через urllib3 --------")
import json
import urllib3
http = urllib3.PoolManager

r = http.request('GET', 'https://newsapi.org/v2/everything?q=Python programming language&apiKey=your_api_here&pageSize=5')
articles = json.loads(r.data.decode('utf-8'))

for article in articles['articles']:
    print(article['title'])
    print(article['publishedAt'])
    print(article['url'])
    print()





















































