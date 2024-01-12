import requests

params = ['1', '2', '3', '4']

response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1": "value1"})
# response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
# response = requests.put("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
# response = requests.delete("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})

print(response.text)
print(response.url)

for i in params:
    response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1": i})
    print(response.url)
