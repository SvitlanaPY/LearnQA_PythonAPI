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
        data = {'name': name_}    # де 'name' - є параметром даного методу(endpoint-а), а 'name_' - змінна, через яку пропихаються дані, які зберігаються в змінній 'names'

        response = requests.get(url, params=data)   # response = requests.get(url, params={'name': name_})
        assert response.status_code == 200, 'Wrong status code'

        response_dict = response.json()
        assert 'answer' in response_dict, "There is no key 'answer' in the response"

# для тесту з порожнім іменем формується строка з порожнім іменем ('Hello, '), а насправді нам приходить строка з дефолтним значеням someone, тобто нам приходить 'Hello, someone'
# тому в наш код потрібно додати перевірку:
        if name_ == "":   # if len(name_) == 0:
            expected_response_text = f"Hello, someone"
        else:
            expected_response_text = f"Hello, {name_}"
        actual_response_text = response_dict['answer']
        assert actual_response_text == expected_response_text, "Actual text in the response is NOT correct"


# параметризація тестів - механізм, що дозволяє запускати один і той самий тест з різними параметрами
# параметри тесту задаються за межами функції але всередині класу. На саму функцію навішується декоратор @pytest.mark.parametrize;
# в @pytest.mark.parametrize ми вказуємо ім"я змінної ('name_'), в яку pytest буде передавати дані,
# а через кому вказуємо змінну, в якій зараз ці дані зберігаються('names').
# після self в назві тесту ми вказуємо саме ту змінну ('name_'), в яку pytest передавав дані

