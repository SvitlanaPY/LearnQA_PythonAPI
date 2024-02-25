# Ex13: User Agent
#
# User Agent - это один из заголовков, позволяющий серверу узнавать, с какого девайса и браузера пришел запрос.
# Он формируется автоматически клиентом, например браузером.
# Определив, с какого девайса или браузера пришел к нам пользователь мы сможем отдать ему только тот контент, который ему нужен.
#
# Наш разработчик написал метод: https://playground.learnqa.ru/ajax/api/user_agent_check
# Метод определяет по строке заголовка User Agent следующие параметры:
# device - iOS или Android
# browser - Chrome, Firefox или другой браузер
# platform - мобильное приложение или веб
#
# Если метод не может определить какой-то из параметров, он выставляет значение Unknown.
# Наша задача написать параметризированный тест.
# Этот тест должен брать из дата-провайдера User Agent и ожидаемые значения,
# GET-делать запрос с этим User Agent и убеждаться, что результат работы нашего метода правильный -
# т.е. в ответе ожидаемое значение всех трех полей.
#
# Список User Agent и ожидаемых значений можно найти по этой ссылке:
# https://gist.github.com/KotovVitaliy/138894aa5b6fa442163561b5db6e2e26
#
# Пример того, как должен выглядеть запрос с указанным User Agent:
# requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
#     headers={"User-Agent": "Some value here"})
#
# ============================================================
# На самом деле метод не всегда работает правильно.
# Ответом к задаче должен быть список из тех User Agent, которые вернули неправильным хотя бы один параметр,
# с указанием того, какой именно параметр неправильный.
#
#
import pytest
import requests

class TestUserAgent:
    headers_ = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]
    @pytest.mark.parametrize('user_agent', headers_)
    def test_user_agent(self, headers_):
        url = 'https://playground.learnqa.ru/ajax/api/user_agent_check'
        response = requests.get(url, headers={"User-Agent": headers_})
        assert response.status_code == 200, 'Wrong status code'
