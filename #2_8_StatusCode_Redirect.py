import requests

# # статус-код 500:
# response1 = requests.get("https://playground.learnqa.ru/api/get_500")
#print(response1.status_code)  # status_code = {int} 500
# print(response1.text)   # text = {str} ''


# # статус-код 404:
# # щоб отримати status_code=404 ми можемо зробити запит на якийсь неіснуючий метод/endpoint. Для клієнтських помилок text-відповіді може приходити
# response2 = requests.get("https://playground.learnqa.ru/api/something")
#print(response2.status_code)  # status_code = {int} 404
# print(response2.text)  # text = {str} '"int(2)\nThis is 404 error!\n<a href="/">Home</a>"'


# # статус-коди 301 та 302:
# # обидва коди означають майже те ж саме - перенаправлення по даному запиту, але все ж є різниця...
# # Code 301: moved permanently (сервер завжди буде редіректати запити на новий url);
# # Code 302: moved temporarily (redirect по даному url є тимчасовим і в будь-який момент може зникнути)
# # це потрібно для того, щоб клієнт міг закешувати, тобто запамятати постійние redirect при 301, і при спробі відправити запит на старий url одразу робити запит на новий url, не витрачаючи часу спершу на запит по старому url.
# # додатковй параметер allow_redirects:
# # allow_redirects=True (по дефолту) означає наступне: якщо сервер намагається нас перенаправити на новий url, то ми слідуємо за ним, поки не досягнемо кінцевої точки.
# # allow_redirects=False означає, що ми не підемо на redirect і у відповіді будуть дані лише першого запиту

# response3 = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
# print(response3.status_code)
# response4 = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# print(response4.status_code)


# # response.history - поверне масив усіх відповідей, які ми отримали перш ніж опинились на кінцевому url.
response = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
print("Qty. of redirects: ", len(response.history))
first_response = response.history[0]
second_response = response
print(first_response.url)   # print(response.history[0].url)
print(second_response.url)   # print(response.url)
print(second_response.status_code)

