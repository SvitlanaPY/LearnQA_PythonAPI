# бібліотека requests дозволяє робити всі види запитів
# робимо запити на метод "check_type", який має повернути у текстовому вигляді тип нашого запиту і параметри в тілі відповіді, які ми передали
# разом із запитом ми передаємо параметри
# у будь-якого HTTP-запиту є: URL та заголовки запиту.
# URL вказує адресу, куди робиться запит, а заголовки - несуть додаткову інформацію про клієнт.
# у всіх типів запитів окрім GET є ще тіло запиту і саме через нього передаються параметри які ми хочемо передати
# GET не має тіла запиту і дані передаються прямо в URL після ?


import requests

params_ = ['1', '2', '3', '4']

# response1 = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1": "value1"})
response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
# response2 = requests.put("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
# response3 = requests.delete("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})

print(response.text)
print(response.url)

for i in params_:
    response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1": i})
    print(response.url)
    # print(response.text)

for i in params_:
    response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": i})
    # print(response.url)
    print(response.text)

