import requests

# case#1: when login and password are correct:
# payload = {"login": "secret_login", "password": "secret_pass"}
# response11 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
#
# cookie_value = response1.cookies.get('auth_cookie')
# # print('cookie_value= ', cookie_value)
# cookies = {'auth_cookie': cookie_value}
# response22 = requests.get("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
#
# print(response22.text)

# case#2: when login and password are NOT correct (then cookies are not sent by the server, cookie value in None):
# payload = {"login": "secret_login", "password": "secret_pass"}
payload = {"login": "secret_login", "password": "secret_pass12345"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
# print(response1.cookies)
# print(dict(response1.cookies))
cookie_value = response1.cookies.get('auth_cookie')
# print('cookie_value= ', cookie_value)
cookies_ = {}
if cookie_value is not None:
    cookies_.update({'auth_cookie': cookie_value})

response2 = requests.get("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies_)

print(response2.text)   # You are authorized (when password is correct); You are NOT authorized (when password is incorrect)
