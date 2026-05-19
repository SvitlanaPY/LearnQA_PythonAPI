# API call says hello by default name (someone);

import requests

response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)
 