import requests
import json

url = ('http://newsapi.org/v2/everything?'
               'q=tesla&'
               'from=2021-02-18&'
               'sortBy=publishedAt&'
               'apiKey=ff669753f7a74ace97b7aabb419655ab')
url_2 = ('https://jsonplaceholder.typicode.com/todos/1')
api_key = "ff669753f7a74ace97b7aabb419655ab"

response = requests.get(url_2)
#print (response.json())

data = response.json()
#print(data['articles']['author'])
#print(data)

with open('blah.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)