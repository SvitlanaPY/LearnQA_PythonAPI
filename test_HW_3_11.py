# Ex11: Тест запроса на метод cookie
#
# Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_cookie
# Этот метод возвращает какую-то cookie с каким-то значением.
# Необходимо с помощью функции print() понять что за cookie и с каким значением, и зафиксировать это поведение с помощью assert
#
# Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py

import pytest


class TestCookie:
    def test_check_cookie_method(self):