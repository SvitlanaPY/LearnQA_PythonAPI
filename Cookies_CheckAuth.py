import requests

payload = {"login": "secret_login", "password": "secret_pass"}
# payload = {"login": "secret_login", "password": "secret_pass12345"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
# print(response1.cookies)
# print(dict(response1.cookies))
cookie_value = response1.cookies.get('auth_cookie')
# print('cookie_value= ', cookie_value)
cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})

response2 = requests.get("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)

print(response2.text)

