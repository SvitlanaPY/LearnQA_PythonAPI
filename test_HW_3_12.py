# Ex12: Тест запроса на метод header
#
# Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_header
# Этот метод возвращает headers с каким-то значением.
# Необходимо с помощью функции print() понять что за headers и с каким значением,
# и зафиксировать это поведение с помощью assert
#
# Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py

import requests

class TestHeaders:

    def test_check_headers_pass(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.text)
        assert response.status_code == 200, 'Wrong status code'

        # У бібліотеці requests заголовки (headers) передаються у вигляді словників, тому, щоб побачити значення headers нам не потрібно перетворювати його у словник:
        # headers_ = dict(response.headers)
        # print(headers_)
        print(response.headers)
        assert 'Connection' in response.headers, "There is no header_name 'Connection' in the headers"

        actual_ConnectionHeader_value = response.headers.get('Connection')    # або actual_ConnectionHeader_value = response.headers['Connection']
        expected_ConnectionHeader_value = 'keep-alive'
        assert actual_ConnectionHeader_value == expected_ConnectionHeader_value, 'Actual ConnectionHeader_value in the headers is NOT correct'

