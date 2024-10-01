from json.decoder import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)   # {str} 'Hello, world'

try:
    parsed_response_text = response.json()
    print(parsed_response_text["answer"])
except JSONDecodeError:
    print("Response is not a JSON format")
# зазвичай парсінг json завжди обертають у конструкцію try...except


# try:
#     parsed_response_text = response.json()
#     key = "answer"
#     if key in parsed_response_text:
#         print(parsed_response_text[key])
#     else:
#         print(f"Ключа {key} в JSON немає")
# except JSONDecodeError:
#     print("Response is not a JSON format")
