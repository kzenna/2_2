import requests
from urllib.parse import urlencode


def get_token_user(user_get):
    oauth_url = 'https://oauth.vk.com/authorize'
    auth_data = {
        'client_id': user_get,
        'display': 'page',
        'redirect_uri': 'https://oauth.vk.com/blank.html',
        'scope': 'friends,photos ,audio,video,docs,notes,pages,status,wall,groups,notifications,offline',
        'response_type': 'token',
        'v': 5.95
    }
    print('?'.join((oauth_url, urlencode(auth_data))))


user_id = '171691064'
TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
params_user = {
        'v': '5.95',
        'access_token': TOKEN,
        'user_id': user_id,
        'fields': 'books, music, movies, interests'
    }

url_user_info = 'https://api.vk.com/method/users.get'
url_user_groups = 'https://api.vk.com/method/groups.get'
response_info_user = requests.get(url_user_info, params_user)
response_user_groups = requests.get(url_user_groups, params_user)
data_user_info = response_info_user.json()
data_user_groups = response_user_groups.json()
user_music = data_user_info["response"][0]["music"]
user_books = data_user_info["response"][0]["books"]
user_movies = data_user_info["response"][0]["movies"]
user_interests = data_user_info["response"][0]["interests"]
user_groups = data_user_groups["response"]["items"]
dict_user_info = {user_id: [user_music, user_books, user_movies, user_interests, user_groups]}
print(dict_user_info)