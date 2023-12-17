# API call says hello by name you specify - using parameters;
# params - іменований параметер, в який потрібно передавати параметри запиту

import requests

payload = {"name": "User"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
print(response.text)
print("URL with params:", response.url)
