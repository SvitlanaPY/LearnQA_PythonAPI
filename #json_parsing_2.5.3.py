# Не завжди response.text містить строку у форматі json,
# e.g. response.text = {str} 'Hello, world'

# # цей код падає в помилку JSONDecodeError, бо response.text повертає {str} 'Hello, world'
# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)   # text = {str} 'Hello, world'
# parsed_response_text = response.json()
# print(parsed_response_text)

from json.decoder import JSONDecodeError
import requests

# зазвичай парсінг json завжди обертають у конструкцію try...except
response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)   # text = {str} 'Hello, world'
try:
    parsed_response_text = response.json()
    print(parsed_response_text["answer"])
except JSONDecodeError:
    print(f"Response '{response.text}' is not a JSON format")


# плюс перевірка ключа на його наявність: ключ є
response2 = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
print(response2.text)   # text = {str} '{"answer":"Hello, User"}'
try:
    parsed_response_text2 = response2.json()
    key2 = "answer"
    if key2 in parsed_response_text2:
        print('Значення ключа key2: ', parsed_response_text2[key2])
    else:
        print(f"Ключа {key2} в JSON немає")
except JSONDecodeError:
    print(f"Response '{response2.text}' is not a JSON format")


# перевірка ключа на його наявність: ключа НЕмає
response3 = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
print(response3.text)   # text = {str} '{"answer":"Hello, User"}'
try:
    parsed_response_text3 = response3.json()
    key3 = "answer3"
    if key3 in parsed_response_text3:
        print('Значення ключа key3: ', parsed_response_text3[key3])
    else:
        print(f"Ключа {key3} в JSON немає")
except JSONDecodeError:
    print(f"Response '{response3.text}' is not a JSON format")

