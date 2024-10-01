import requests

#  як правило параметри кладуть в окрему змінну, яку називають payload; в неї ми передаємо словник;
#  в змінну payload кладемо одну пару "ключ":"значеня"
payload = {"name": "USER"}

response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# іменований параметр params
print(response.text)
# response.text - Тіло відповіді, що містить строку у форматі json(але не завжди у форматі json);
# str '{"answer":"Hello, USER"}'

# відповідь у форматі json це такий же текст, як і будь-який інший, а форматування робить зручним витягувати з нього будь-які його частини.
# працюючи з текстом як зі строкою, неможливо звернутись до окремого її поля, бо в ній немає пари "ключ":"значення"
# для того, щоб можна було це робити, нам потрібно перетворити цю строку в обєкт
# тоді ми розберемо цей об"єкт і з нього будемо витягувати необхідне нам значення.
# в python-і є функція json(), яка перетворює строку у форматі json в об"єкт
#