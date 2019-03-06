with open("ES.txt", "r", encoding='utf-8') as datafile:
    ES_file = datafile.read()
    ES_list = ES_file.split()


import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

payload = {'text': ES_list}

def translate_it(text, to_lang):
    params = {
        'key': API_KEY,
        'text': text,
        'lang': 'ru-{}'.format(to_lang),
        'id': '3d1836cd.5c7fb7fd.06c29bdd-1-0',
        'reason': 'auto',
        'srv': 'tr-text'
    }

    response = requests.get(URL, params = params)
    json_ = response.json()
    return ''.join(json_['text'])
print(translate_it(payload, 'es-ru'))




# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))
#
#
# requests.post('http://requestb.in/10vc0zh1', json=dict(a='goo', b='foo'))



