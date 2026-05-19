# API call says hello by name you specify - using parameters;
# params - іменований параметер, в який потрібно передавати параметри запиту

import requests

payload = {"name": "Anna"}
response1 = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response1.text)
print("URL with params:", response1.url)

response2 = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
print(response2.text)
print("URL with params:", response2.url)
