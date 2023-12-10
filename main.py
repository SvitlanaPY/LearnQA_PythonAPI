import requests

response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)

response2 = requests.get("https://playground.learnqa.ru/api/get_text")
print(response2.text)

print("Hello from Svitlana")
