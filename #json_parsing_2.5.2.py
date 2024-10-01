import requests
import json

response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
print(response.text)   # text = {str} '{"answer":"Hello, User"}'
obj = json.loads(response.text)   # obj = {dict: 1} {"answer":"Hello, User"}
print(obj)

# бібліотека json вбудована в бібліотеку requests і функцію парсінга .json() можна викликати одразу в змінній response
# функція парсінга .json() буде застосовуватись до поля/аргументу text
parsed_response_text = response.json()   # parsed_response_text = {dict: 1} {'answer': 'Hello, User'}
print(parsed_response_text["answer"])
# Hello, User
