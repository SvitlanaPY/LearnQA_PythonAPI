import json

string_as_json_format = '{"answer": "Hello, User"}'
# змінна типу string, так виглядає json-формат ДО парсінгу
obj = json.loads(string_as_json_format)   # строка перетворюється в об"єкт, що нагадує по своїх властивостях словник
print(obj)   # {dict: 1} {'answer':'Hello, User}
print(obj['answer'])  # звертаємось до ключа "answer" у словнику obj і повертаємо/друкуємо його значення:
# Hello, User

# якщо ми звернемось до ключа, якого немає, то отримаємо т.зв. key-error.
# тому перед тим, як використовувати будь-який ключ, потрібно перевіряти його наявність
key = "answer2"
if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON немає")
# Ключа answer2 в JSON немає

key = "answer"
if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON немає")
# Hello, User
