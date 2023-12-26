import requests
import json

response = requests.get("https://playground.learnqa.ru/api/hello", params={"name":"User"})
print(response.text)   # {str} '{"answer":"Hello, User"}'
obj = json.loads(response.text)   # {dict: 1} {"answer":"Hello, User"}
print(obj)

parsed_response_text = response.json()   # parsed_response_text: {dict: 1} {'answer': 'Hello, User'}
print(parsed_response_text["answer"])
