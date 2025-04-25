# Ex6: Длинный редирект
# Необходимо написать скрипт, который создает GET-запрос на метод: https://playground.learnqa.ru/api/long_redirect
# С помощью конструкции response.history необходимо узнать,
# сколько редиректов происходит от изначальной точки назначения до итоговой.
# И какой URL итоговый.
# Ответ опубликуйте в виде ссылки на коммит со скриптом, а также укажите количество редиректов и конечный URL.

import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

print("Qty. of redirects:", len(response.history))  # __len__ = {int} 3
print("redirect_#1:", response.history[0].url)
print("redirect_#2:", response.history[1].url)
print("redirect_#3:", response.history[2].url)
print("final redirect:", response.url)
# в response.history[-1].url - не є final url, final url завжди лежить в response.url

