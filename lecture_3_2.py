# Домашнее задание к лекции 3.2
# «Работа с библиотекой requests, http-запросы»
# Кокурникова Лилия Фаритовна, 18.03.19

with open("ES.txt", "r", encoding='utf-8') as datafile:
    ES_file = datafile.read()
    ES_list = ES_file.split()

with open("DE.txt", "r", encoding='utf-8') as datafile:
    DE_file = datafile.read()
    DE_list = DE_file.split()

with open("FR.txt", "r", encoding='utf-8') as datafile:
    FR_file = datafile.read()
    FR_list = FR_file.split()


import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

payload = {'text': {}}

def translate_it(text, to_lang):
    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-ru'.format(to_lang),
        'id': '3d1836cd.5c7fb7fd.06c29bdd-1-0',
        'reason': 'auto',
        'srv': 'tr-text'
    }
    response = requests.get(URL, params = params, data = payload)
    json_ = response.json()
    return ' '.join(json_['text'])


print(translate_it(ES_list, 'es'), file = open("ES_translate.txt", "w", encoding='utf-8'))
print(translate_it(DE_list, 'de'), file = open("DE_translate.txt", "w", encoding='utf-8'))
print(translate_it(FR_list, 'fr'), file = open("FR_translate.txt", "w", encoding='utf-8'))


