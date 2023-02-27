"""
Прежде, чем мы с вами начнем изучать API предоставляемый, нам телеграмм, нам потребуется немного познакомиться с
библиотекой requests. Она позволяет нам делать запросы через интернет, на нужные нам “адреса”.
Нам потребуется метод get данной библиотеки, который позволяет послать запрос, на получение каких то данных.
"""

import requests

r = requests.get('https://www.google.com')
print(type(r))

"""
В результате мы видим, что возвращается объект класса Response
Мы можем передавать этому классу и другие атрибуты помимо url
    url - передает ссылку, куда будет отправлен запрос(обязательный)
    params - словарь, который будет отправлен в строке запроса(необязательный)
    headers - словарь HTTP-заголовков отправляемых запросом(необязательный)
    cookies - объект Dict или CookieJar для отправки с запросом(необязательный)
    auth - AuthObject для включения базовой аутентификации HTTP(необязательный)
    timeout - число с плавающей точкой, описывающее тайм-аут запроса(необязательный)
    allow-redirects - логическое значение разрешения перенаправления(необязательный)
    proxies - протокол сопоставления словаря с URL-адресом прокси(необязательный)
    stream - удержание соединения открытым, пока не получен весь контент

Код ответа (состояния) HTTP показывает, был ли успешно выполнен определённый HTTP запрос. Коды сгруппированы в 5 классов:
    Информационные 100 - 199
    Успешные 200 - 299
    Перенаправления 300 - 399
    Клиентские ошибки 400 - 499
    Серверные ошибки 500 - 599
"""