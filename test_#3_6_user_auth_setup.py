import pytest
import requests

class TestUserAuth:
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self):
        auth_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=auth_data)
        assert response1.status_code == 200, 'Wrong status code'
        assert "auth_sid" in response1.cookies, "There is no auth cookie in the response1"
        assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response1"
        assert "user_id" in response1.json(), "There is no user id in the response1"

        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x-csrf-token")
        self.user_id_from_auth_method = response1.json().get("user_id")  # user_id_from_auth_method = response1.json()["user_id"]

    def test_user_auth(self):
        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )
        assert response2.status_code == 200, 'Wrong status code'
        assert "user_id" in response2.json(), "There is no user id in the response2"
        user_id_from_check_method = response2.json()["user_id"]
        assert self.user_id_from_auth_method == user_id_from_check_method, "User id from auth method is not equal to user id from check method"


    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_user_auth(self, condition):
        if condition == "no_cookie":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token": self.token}
            )
        else:
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )

        assert response2.status_code == 200, 'Wrong status code'
        assert "user_id" in response2.json(), "There is no user id in the response2"
        user_id_from_check_method = response2.json()["user_id"]
        assert user_id_from_check_method == 0, f"User is authorized with {condition}"
