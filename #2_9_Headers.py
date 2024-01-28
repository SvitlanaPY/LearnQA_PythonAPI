import requests

headers_ = {"some_header": "123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers_)

print(response.text)
print(response.headers)  # заголовки respons-а
