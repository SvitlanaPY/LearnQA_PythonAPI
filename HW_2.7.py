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
