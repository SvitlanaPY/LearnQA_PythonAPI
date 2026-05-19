# API call says hello by default name;

import requests

response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)
 