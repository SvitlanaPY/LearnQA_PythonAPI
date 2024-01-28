# Ex11: Тест запроса на метод cookie
#
# Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_cookie
# Этот метод возвращает какую-то cookie с каким-то значением.
# Необходимо с помощью функции print() понять что за cookie и с каким значением,
# и зафиксировать это поведение с помощью assert
#
# Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py

import pytest
import requests

class TestCookie:
    def test_check_cookie_passed(self):
        response = requests.get('https://playground.learnqa.ru/api/homework_cookie')
        assert response.status_code == 200, 'Wrong status code'

        print(dict(response.cookies))
        cookies = dict(response.cookies)
        assert 'HomeWork' in cookies, "There is no cookie_name 'Homework' in the cookies"

        actual_cookie_value = cookies['HomeWork']   # actual_cookie_value = response.cookies.get('HomeWork')
        expected_cookie_value = 'hw_value'
        assert actual_cookie_value == expected_cookie_value, 'Actual cookie_value in the cookies is NOT correct'

    def test_check_cookie_fail(self):
        response = requests.get('https://playground.learnqa.ru/api/homework_cookie')
        assert response.status_code == 200, 'Wrong status code'

        print(dict(response.cookies))
        cookies = dict(response.cookies)
        assert 'HomeWork' in cookies, "There is no cookie_name 'HomeWork' in the cookies"

        actual_cookie_value = cookies['HomeWork']   # actual_cookie_value = response.cookies.get('HomeWork')
        expected_cookie_value = 'hw_value1111'
        assert actual_cookie_value == expected_cookie_value, 'Actual cookie_value in the cookies is NOT correct'
        