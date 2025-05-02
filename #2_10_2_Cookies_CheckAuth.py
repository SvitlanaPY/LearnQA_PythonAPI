import requests

# case#1: when login and password are CORRECT:
payload_correct = {"login": "secret_login", "password": "secret_pass"}
response11 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload_correct)
print(dict(response11.cookies))
cookie_value_correct = response11.cookies.get('auth_cookie')    # за назвою cookie (а саме 'auth_cookie') отримуємо значення cookie і кладемо це значення у змінну cookie_value_correct
print('cookie_value_correct= ', cookie_value_correct)
cookie_correct = {'auth_cookie': cookie_value_correct}
# отримане значення cookie передаємо в get-запиті у cookies=
response22 = requests.get("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookie_correct)
print(response22.text)    # You are authorized (when password is correct)


# case#2: when login and password are INCORRECT (тоді сервер не присилає cookie(маємо {}), і cookie value буде None в цьому випадку)
# коли значення cookie є None, то передавати таке значення(None) дальше немає сенсу
payload_incorrect = {"login": "secret_login", "password": "secret_pass12345"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload_incorrect)
print(dict(response1.cookies))
cookie_value_ = response1.cookies.get('auth_cookie')   # якщо викликати метод get з ключем, якого неіснує(i.e. 'auth_cookie'), то повернеться значення None
print('cookie_value_= ', cookie_value_)   # cookie_value_=  None
cookie_ = {}
if cookie_value_ is not None:
    cookie_.update({'auth_cookie': cookie_value_})

response2 = requests.get("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookie_)
print(response2.text)   # You are NOT authorized (when password is incorrect)

