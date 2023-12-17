# API call says hello by name you specify;

import requests

response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)
 