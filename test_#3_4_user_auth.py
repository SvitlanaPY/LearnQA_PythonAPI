import requests

class TestUserAuth:
    def test_user_auth(selfs):
        auth_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=auth_data)

        assert "auth_sid" in response1.cookies, "There is no auth cookie in the response1"
        assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response1"
        assert "user_id" in response1.json(), "There is no user id in the response1"

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id_from_auth_method = response1.json().get("user_id")   # user_id_from_auth_method = response1.json()["user_id"]

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        assert "user_id" in response2.json(), "here is no user id in the response2"
        user_id_from_check_method = response2.json()["user_id"]

        assert user_id_from_auth_method == user_id_from_check_method, "User id from auth method is not equal to user id from check method"
