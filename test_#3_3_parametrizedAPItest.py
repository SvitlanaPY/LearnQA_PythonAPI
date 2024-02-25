import pytest
import requests


class TestFirstAPI:
    names = [
        ("Svitlana"),
        ("JEP"),
        ("")
    ]
    @pytest.mark.parametrize('name_', names)
    def test_hello_call(self, name_):
        url = 'https://playground.learnqa.ru/api/hello'
        data = {'name': name_}

        response = requests.get(url, params=data)
        assert response.status_code == 200, 'Wrong status code'

        response_dict = response.json()
        assert 'answer' in response_dict, "There is no key 'answer' in the response"

        if name_ == "":   # if len(name) == 0:
            expected_response_text = f"Hello, someone"
        else:
            expected_response_text = f"Hello, {name_}"
        actual_response_text = response_dict['answer']
        assert actual_response_text == expected_response_text, "Actual text in the response is NOT correct"
