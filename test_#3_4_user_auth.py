# У тесті будемо робити одразу два запити:
# перший запит (на https://playground.learnqa.ru/api/user/login) - авторизує нашого користувача,
# а другий запит (на https://playground.learnqa.ru/api/user/auth) - перевірить, що користувач авторизувався успішно.
# Щоб авторизувати користувача, ми повинні передати 'email' та 'password' в метод /api/user/login:
# 'email': 'vinkotov@example.com', 'password': '1234'.
# У випадку коли переданий email та password є вірні, метод поверне нам:
# 1. id-користувача (user_id) під яким ми авторизувались,
# 2. авторизаційне cookie (воно буде називатись auth_sid) і матиме унікальне значення,
# саме із цим унікальним значенням сервер пов'яже нашого користувача.
# До усіх подальших запитів ми повинні прикладати цю авторизаційну cookie (auth_sid), щоб сервер розумів, що наші запити йдуть від користувача і є авторизованими.
# 3. так званий csrf-токен - він буде міститись в header-і/заголовку x-csrf-token і теж матиме якесь унікальне значення.
# він відіграє ключову роль в безпеці користувача, і не дозволяє підробляти запити від імені цього користувача зловмисниками.
# Лише у випадку передачі і вірного значення авторизаційного cookie (auth_sid) і вірного значення header-a/заколовка (x-csrf-token),
# подальші запити будуть вважатись авторизованими.
# Це ми і будемо перевіряти у другому запиті на метод /api/user/auth: передавати отримані із першого запиту cookie та header.
# Цей метод влаштований наступним чином: якщо ми передамо вірні значення, отримані із першого запиту,
# то сервер впізнає нашого користувача і поверне у відповідь його id-користувача (те саме id-користувача, яке ми отримали із першого запиту)
# і це означатиме, що сервер вважає запит авторизованим.
# Інакше сервер поверне id-користувача=0, це повинно означати, що ми передали невірний cookie чи невірний header, або не передали їх взагалі.
#

import requests

class TestUserAuth:
    def test_user_auth(self):
        auth_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=auth_data)
        assert response1.status_code == 200, 'Wrong status code'

        assert "auth_sid" in response1.cookies, "There is no auth cookie in the response1"
        auth_sid = response1.cookies.get("auth_sid")

        assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response1"
        token = response1.headers.get("x-csrf-token")

        assert "user_id" in response1.json(), "There is no user id in the response1"
        user_id_from_auth_method = response1.json().get("user_id")   # або user_id_from_auth_method = response1.json()["user_id"], але
        # якщо такого ключа "user_id" неіснує, то тест впаде у помилку, тоді як при використанні .get("user_id") до response1.json() - повернеться значення None


        response2 = requests.get("https://playground.learnqa.ru/api/user/auth", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        assert response2.status_code == 200, 'Wrong status code'

        assert "user_id" in response2.json(), "There is no user id in the response2"
        user_id_from_check_method = response2.json()["user_id"]    # або response2.json().get("user_id")

        assert user_id_from_auth_method == user_id_from_check_method, "User id from auth method is not equal to user id from check method"

