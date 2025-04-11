import requests

# заголовки http-запиту - це службова інформація.
# заголовки є як в запита(request headers), так і у відповіді(response headers),
#  тобто клієнт під час запиту пересилає свою службову інформацію, а сервер у відповідь присилає свою службову інформацію.
# у request headers: cookie, scheme, user-agent.
# у response headers: як правило приходить інформація про те, в якому форматі ця відповідь, які cookies і  яким значенням сервер просить клієнта втановити і т.д.
# у бібліотеці requests заголовки передаються за допомогою словників, де КЛЮЧ - назва заголовку(header-a), а ЗНАЧЕННЯ словника - значення даного заколовку(header-a).

headers_ = {"some_header": "123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers_)

print(response.text)  # заголовки request-а (які ми відправили); сервер повідомляє, які заголовки він отримав від клієнта
print(response.headers)  # заголовки response-а (які ми отримали від сервера); відповідь сервера на цей запит
pass

