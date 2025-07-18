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
# Если метод не может определить какой-то из параметров, он выставляет значение Unknown.
#
# Наша задача написать параметризированный тест.
# Этот тест должен брать из дата-провайдера User Agent и ожидаемые значения,
# делать GET-запрос с этим User Agent и убеждаться, что результат работы нашего метода правильный -
# т.е. в ответе ожидаемое значение всех трех полей.
#
# Список User Agent и ожидаемых значений можно найти по этой ссылке:
# https://gist.github.com/KotovVitaliy/138894aa5b6fa442163561b5db6e2e26
#
# Пример того, как должен выглядеть запрос с указанным User Agent:
# requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
#     headers={"User-Agent": "Some value here"})
#
# На самом деле метод не всегда работает правильно.
# Ответом к задаче должен быть список из тех User Agent, которые вернули неправильным хотя бы один параметр,
# с указанием того, какой именно параметр неправильный.
#
#
import pytest
import requests

class TestUserAgent:
    ParametersList = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Mobile","No","Android"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1","Mobile","Chrome","iOS"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)","Googlebot","Unknown","Unknown"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0","Web","Chrome","No"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1","Mobile","No","iPhone")
    ]
    @pytest.mark.parametrize('prm_user_agent, expected_platform, expected_browser, expected_device', ParametersList)
    def test_user_agent(self, prm_user_agent, expected_platform, expected_browser, expected_device):
        url = 'https://playground.learnqa.ru/ajax/api/user_agent_check'

        response = requests.get(url, headers={"User-Agent": prm_user_agent})
        assert response.status_code == 200, 'Wrong status code'

        response_dict = response.json()
        assert 'platform' in response_dict, "There is no key 'platform' in the response"
        assert 'browser' in response_dict, "There is no key 'browser' in the response"
        assert 'device' in response_dict, "There is no key 'device' in the response"

        actual_platform = response_dict.get('platform')
        assert actual_platform == expected_platform, "Actual platform in the response is NOT correct"
        actual_browser = response_dict.get('browser')
        assert actual_browser == expected_browser, "Actual browser in the response is NOT correct"
        actual_device = response_dict.get('device')
        assert actual_device == expected_device, "Actual device in the response is NOT correct"

