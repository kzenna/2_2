with open("ES.txt", "r", encoding='utf-8') as datafile:
  ES_file = datafile.read()
  ES_list = ES_file.split()

import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
payload = {'text': ES_list}
params = {
    'key': API_KEY,
    'text': payload,
    'lang': 'es-ru',
    'id': '3d1836cd.5c7fb7fd.06c29bdd-1-0',
    'reason': 'auto',
    'srv': 'tr-text'
}

res = requests.post(URL, params = params, data = payload)
json_ = res.json()

print(json_['text'])







