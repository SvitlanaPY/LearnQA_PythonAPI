# Ex5: Парсинг JSON
#
# Давайте создадим пустой Python-скрипт.
# Внутри него создадим переменную json_text.
# Значение этой переменной должно быть таким, как указано тут:
# https://gist.github.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37
# i.e. "{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}"
#
# Наша задача с помощью библиотеки “json”, которую мы показывали на занятии,
# распарсить нашу переменную json_text и вывести текст второго сообщения с помощью функции print.

import json
import requests

# case 1
response = requests.get("https://gist.githubusercontent.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37/raw/4b1d72e0ac353b36c58b7a3a9e90fa163d57919f/some.json")
# print(response.text[1:-1])   # прибираємо перший і останній символ, яким є "; тобто витягуємо все те, що є між першими " та останнім "
# print(len(response.text))
json_text = response.text[1:-1]
obj = json.loads(json_text)
print(obj['messages'][1]['message'])


# case 2
json_text2 = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj2 = json.loads(json_text2)
print(obj2['messages'][1]['message'])


# case 3   !!!
response = requests.get("https://gist.githubusercontent.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37/raw/4b1d72e0ac353b36c58b7a3a9e90fa163d57919f/some.json")
j_t = response.text
j_t_dict = json.loads(j_t[1:-1])
print(j_t_dict['messages'][1]['message'])

