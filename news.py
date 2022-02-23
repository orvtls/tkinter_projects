import requests
import json

response_api = requests.get("https://newsapi.org/v2/everything?q=Covid-19&from=2022-02-20&sortBy=popularity&apiKey=fb358baaf0a349cea5135ebf84961e87")
data = response_api.text
parse_json = json.loads(data)
print(parse_json['articles'][0]['title'],"By - ",parse_json['articles'][0]['author'])
print(parse_json['articles'][0]['description'])
print(parse_json['articles'][0]['url'])
