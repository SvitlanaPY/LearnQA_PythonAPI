import requests
import json
# бібліотека json вбудована в бібліотеку requests і функцію парсінга .json() можна викликати одразу зі змінної response
# функція парсінга .json() буде застосовуватись до аргументу text в об"єкті response

# парсінг за допомогою бібліотеки requests, застосовуючи ф-ію парсінга json() до змінної response:
response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
parsed_response_text = response.json()   # parsed_response_text = {dict: 1} {'answer': 'Hello, User'}
print(parsed_response_text["answer"])    # Hello, User


# парсінг за допомогою бібліотеки json:
response2 = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
print(response2.text)   # text = {str} '{"answer":"Hello, User"}'
obj = json.loads(response2.text)
print(obj)    # obj = {dict: 1} {'answer':'Hello, User'}

