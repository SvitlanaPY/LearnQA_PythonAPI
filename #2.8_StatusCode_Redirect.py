import requests

# response = requests.get("https://playground.learnqa.ru/api/get_500")
#
# print(response.status_code)
# print(response.text)
#
# response = requests.get("https://playground.learnqa.ru/api/something")
#
# print(response.status_code)
# print(response.text)
#
# # Code 301: moved permanently (сервер завжди буде редіректати запити на новий url); Code 302: moved temporarily (redirect є тимчасовим і в будь-який момент може зникнути)
# response = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
# print(response.status_code)

response1 = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response1.history[0]
second_response = response1
print(first_response.url)
print(second_response.url)
print(response1.status_code)
