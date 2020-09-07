№ ьн_зукыщтфд_ещлут
# my_personal_token
# AgAAAAAVu-5jAAaWtecLmGg59E5mkW5GQXAZM7o

# Скрипт работы с api yandex-метрики
# Цель: посчитать количество пользовательских действий на сайте (или других меток)


'''
Словарь ids содержит идентификаторы приложений, созданных в интерфейсе яндекс метрики
Метрики взяты с https://yandex.ru/dev/metrika/doc/api2/api_v1/metrics/visits/basic-docpage/
Цикл генерирует запрос в https://api-metrika.yandex.ru/stat/v1/data
прописываем данные в формате json и выводим их на экран

Мой тестовый счетчик дает 0, потому что к сайту скорее всего не подключен)
!!!!
Обязательно в настройках доступа счётчика включить Публичный доступ к статистике, (а то 403)
'''


import requests
import sys


header = {'Authorization: OAuth AgAAAAAVu-5jAAaWtgINcOYJKkkvnTOf9Kiegxs'}
ids = {
    'Count_1' : 67110799
}


payload = {
    'metrics' : 'ym:s:visits, ym:s:users',
    'date1': '2018-09-01',
    'date2': '2018-11-30',
    # 'filters': "ym:s:deviceCategory=='mobile'",
    'ids':  67110799,
    'accuracy': 'full',
    'pretty': True,
    'oauth_token': 'AgAAAAAVu-5jAAaWtgINcOYJKkkvnTOf9Kiegxs'
}

i = 1

for key, value in ids.items():
    payload['ids'] = value
    r = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params=payload)
    data = str(r.json()['max'])[1:-1].split(',')
    i += 1
    payload['ids']=value
    print('total', key, data)


import xlsxwriter
