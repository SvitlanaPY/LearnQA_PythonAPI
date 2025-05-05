import requests


class TestFirstAPI:
    def test_hello_call_pass(self):
        url = "https://playground.learnqa.ru/api/hello"
        name_ = "Svitlana"
        data = {'name': name_}    # де 'name' - є параметром даного методу(endpoint-а),

        response = requests.get(url, params=data)
        assert response.status_code == 200, "Wrong status code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is no key 'answer' in the response"

        expected_response_text = f"Hello, {name_}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "Actual text in the response is NOT correct"

    def test_hello_call_fail(self):
        url = "https://playground.learnqa.ru/api/hello"
        name_ = "Svitlana"

        response = requests.get(url)
        assert response.status_code == 200, "Wrong status code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is no key 'answer' in the response"

        expected_response_text = f"Hello, {name_}"
        actual_response_text = response_dict['answer']
        assert actual_response_text == expected_response_text, "Actual text in the response is NOT correct"

#        AssertionError: Actual text in the response is NOT correct
#        assert 'Hello, someone' == 'Hello, Svitlana'
#          - Hello, Svitlana   (те, що ми очікуємо)
#          + Hello, someone    (те, що на нам насправді прийшло)

