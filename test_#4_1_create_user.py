# Розглянемо метод створення користувача.
# Для створення користувача потрібно передати дані користувача, такі як:
# username, password, firstName, lastName, email
# спершу створимо негативний тест, який буде передавати вже існуючий email.
#


import pytest
import requests


class TestUserRegister:
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        credentials = {
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'password': '1234',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=credentials)
        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

        # print(response.status_code)
        # print(response.content)

# >python -m pytest -s tests/test_user_register.py
