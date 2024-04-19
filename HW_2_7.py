# Ex7: Запросы и методы
#
# Сегодня задача должна быть попроще.
# У нас есть вот такой URL: https://playground.learnqa.ru/ajax/api/compare_query_type
# Запрашивать его можно четырьмя разными HTTP-методами: POST, GET, PUT, DELETE
#
# При этом в запросе должен быть параметр method.
# Он должен содержать указание метода, с помощью которого вы делаете запрос.
# Например, если вы делаете GET-запрос, параметр method должен равняться строке ‘GET’.
# Если POST-запросом - то параметр method должен равняться ‘POST’. И так далее.
#
# Надо написать скрипт, который делает следующее:
#
# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
# И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра,
# но сервер отвечает так, словно все ок.
# Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
#
# Не забывайте, что для GET-запроса данные надо передавать через params=
# А для всех остальных через data=

import requests

# --- #1 ---
# response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
# print("GET:", response.text)
# print("GET:", response.url)
# print(f"GET: {response.status_code}: {response.reason}")
#
# response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
# print("POST:", response.text)
# print("POST:", response.url)
# print(f"POST: {response.status_code}: {response.reason}")
#
# response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
# print("PUT:", response.text)
# print("PUT:", response.url)
# print(f"PUT: {response.status_code}: {response.reason}")
#
# response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")
# print("DEL:", response.text)
# print("DEL:", response.url)
# print(f"DEL: {response.status_code}: {response.reason}")
#
# --- #2 ---
# response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
# print("HEAD:", response.text)
# print("HEAD:", response.url)
# print(f"HEAD: {response.status_code}: {response.reason}")

# --- #3 ---
# response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
# print("GET:", response.text)
# print("GET:", response.url)
# print(f"GET: {response.status_code}: {response.reason}")
#
# response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "POST"})
# print("GET:", response.text)
# print("GET:", response.url)
# print(f"GET: {response.status_code}: {response.reason}")
#
# response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "PUT"})
# print("GET:", response.text)
# print("GET:", response.url)
# print(f"GET: {response.status_code}: {response.reason}")
#
# response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "DELETE"})
# print("GET:", response.text)
# print("GET:", response.url)
# print(f"GET: {response.status_code}: {response.reason}")

# --- #4 ---
params = ['GET', 'POST', 'PUT', 'DELETE']
for i in params:
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": i})
    print(f"GET: method={i}, {response.text}")
    print(f"GET: method={i}: {response.status_code}: {response.reason}")

for i in params:
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": i})
    print(f"POST: method={i}, {response.text}")
    print(f"POST: method={i}: {response.status_code}: {response.reason}")

for i in params:
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": i})
    print(f"PUT: method={i}, {response.text}")
    print(f"PUT: method={i}: {response.status_code}: {response.reason}")

for i in params:
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": i})
    print(f"DELETE: method={i}, {response.text}")
    print(f"DELETE: method={i}: {response.status_code}: {response.reason}")
