import requests

# api_key = '23ed3384fe2c65cb1e088e8fbb87a6f1'

# url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=23ed3384fe2c65cb1e088e8fbb87a6f1"

# response = requests.get(url)

# print(response.status_code)
# print(response.json())

from pprint import pprint

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&appid=23ed3384fe2c65cb1e088e8fbb87a6f1')
pprint(r.json())