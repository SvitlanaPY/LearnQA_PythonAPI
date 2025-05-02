# Cookie - це спеціальні файли, їх створює клієнт(мобільний додаток чи браузер) на основі відповіді від сервера.
# ці файли мають термін дії, після чого вони видаляються клієнтом.
# в кожного Cookie є: імя, значення, домен.
# Щоразу, коли клієнт створює http-запит на сервер, він додає всі cookies, що стосуються домену, на який робиться цей запит
# Cookie використовуються для різних цілей, і сама популярна з них - авторизація.
# Коли користувач приходить на сайт не будучи авторизованим, то сайт просить його ввести login та password.
# Ці дані із http-запитом ідуть на сервер. Сервер їх перевіряє, і якщо вони вірні, то сервер у відповідь присилає cookies, із спеціальним іменем та значенням, які є тільки у цього користувача.
# і наступного разу, коли клієнт користувача буде робити http-запит на сервер, то він додасть значення цього cookie і сервер впізнає користувача.
# Cookie ще використовуються, щоб запам"ятовувати якусь інформацію про користувача: наприклад, відрізняти тих, хто вже був на якійсь сторінці, від тих, хто ще не був,
# відслідковувати дії користувача на сайті і т.д.
# бібліотека requests може як відправляти Cookie так і отримувати Cookie.
# Cookie у змінній response зберігається у вигляді об"єкту. І щоб побачити значення Cookie, спершу треба його привести до вигляду словника.
# header 'Set-Cookie' - у response-і від сервера:
# значення cookie, дата дії cookie, домен, до якого належить cookie, path- це частина url без домену, для яких це cookie треба передавати
# (якщо path=/ то передавати треба для усіх путей), прапорець HttpOnly- щоб cookie була ахощена від XSS та CSRF атак.

import requests

# ex.#1 correct pwd
payload = {"login": "secret_login", "password": "secret_pass"}
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

print('ex.#1')
print(response.text)
print(response.status_code)
print(response.cookies)
print(dict(response.cookies))     # {'auth_cookie': '322410'}
print(response.headers)
# response.headers:
# {
#   'Date': 'Fri, 02 May 2025 13:04:38 GMT',
#   'Content-Type': 'text/html; charset=utf-8',
#   'Content-Length': '0',
#   'Connection': 'keep-alive',
#   'Keep-Alive': 'timeout=10',
#   'Server': 'Apache',
#   'Set-Cookie': 'auth_cookie=509982; expires=Mon, 02-Jun-2025 13:04:38 GMT; Max-Age=2678400; path=/; domain=playground.learnqa.ru; HttpOnly',
#   'Cache-Control': 'max-age=0',
#   'Expires': 'Fri, 02 May 2025 13:04:38 GMT'
# }



# ex.#2 incorrect pwd
payload = {"login": "secret_login", "password": "secret_pass2"}
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

print()
print('ex.#2')
print(response.text)
print(response.status_code)
print(response.cookies)
print(dict(response.cookies))
