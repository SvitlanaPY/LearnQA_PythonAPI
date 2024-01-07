import requests

# ex.#1
payload = {"login": "secret_login", "password": "secret_pass"}
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

print('ex.#1')
print(response.text)
print(response.status_code)
print(response.cookies)
print(dict(response.cookies))
print(response.headers)


# ex.#2
payload = {"login": "secret_login", "password": "secret_pass2"}
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data= payload)

print()
print('ex.#2')
print(response.text)
print(response.status_code)
print(response.cookies)
print(dict(response.cookies))