# Ex10: Тест на короткую фразу
#
# В рамках этой задачи с помощью pytest необходимо написать тест, который просит ввести в консоли любую фразу короче 15 символов.
# А затем с помощью assert проверяет, что фраза действительно короче 15 символов.
#
# Чтобы в переменную получить значение, введенное из консоли, необходимо написать вот такой код:
# phrase = input("Set a phrase: ")
#
# Внимание, чтобы pytest не игнорировал команду ввода с клавиатуры, запускать тест нужно с ключиком "-s":
# python -m pytest -s test_HW_3_10.py


import pytest


class TestPhrase:
    def test_check_phrase_length(self):
        phrase = input("SET A PHRASE: ")
        assert len(phrase) < 15, f"Length of the phrase is more than 15 symbols"

