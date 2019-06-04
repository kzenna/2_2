import requests
import time


class VKTimeError(Exception):
    def __init__(self, message, errors, user_id):
        super().__init__(message)
        self.message = message
        self.errors = errors
        self.user_id = user_id


DEBUG_MODE = False
TOKEN = '2a3035afb76507e7737b7c80fb53d80d8f1ae404ba12e4418f74a9a918c49ebe2b74b3501c03c5ad3bcea'
user_id = '545472010'
params_user = {
        'v': '5.95',
        'access_token': TOKEN,
        'user_id': user_id,
        'fields': 'books, music, movies, interests'
    }
params_search = {
    'v': '5.95',
    'sex': '2',
    'age_from': '50',
    'age_to': '65',
    'count': '20',
    'city': '1',
    'country': '1',
    'sort': '0',
    'access_token': TOKEN,
    'user_id': user_id,
    'fields': 'books, music, movies, interests'
    }

search_user = 'https://api.vk.com/method/users.search'
response_search = requests.get(search_user, params_search)
data_search = response_search.json()
dict_id_books = {}
dict_id_music = {}
dict_id_movies = {}
dict_id_interests = {}
list_id_users = []
dict_groups_users = {}
dict_friends_users = {}
# dict_full_info_users = {}
info_index = 0
while info_index < len(data_search["response"]["items"]):
    search_id = data_search["response"]["items"][info_index]["id"]
    try:
        search_books = data_search["response"]["items"][info_index]["books"]
        search_music = data_search["response"]["items"][info_index]["music"]
        search_movies = data_search["response"]["items"][info_index]["movies"]
        search_interests = data_search["response"]["items"][info_index]["interests"]
    except KeyError:
        pass
    else:
        dict_id_books.update({search_id: search_books})
        dict_id_music.update({search_id: search_music})
        dict_id_movies.update({search_id: search_movies})
        dict_id_interests.update({search_id: search_interests})
        list_id_users.extend([search_id])
    info_index += 1
# data_friends_list = []
for user in list_id_users:
    url_group = 'https://api.vk.com/method/groups.get'
    url_friends_users = 'https://api.vk.com/method/friends.get'
    params_users = {
        'v': '5.95',
        'access_token': TOKEN,
        'user_id': user
    }
    response_group_found_users = requests.get(url_group, params_users)
    response_found_friends_users = requests.get(url_friends_users, params_users)
    data_friends = response_found_friends_users.json()
    data_friends_users = data_friends["response"]["items"]
    # data_friends_list.extend(data_friends_users)
    dict_friends_users.update({user: data_friends_users})
    try:
        data = response_group_found_users.json()
        time.sleep(1)
        if DEBUG_MODE:
            print(data)
        if 'error' in data and 'error_code' in data['error']:
            raise VKTimeError(data['error']['error_code'], data['error']['error_msg'], user)
    except VKTimeError as e:
        if e.message == 6:
            dict_groups_users.update({user: data["response"]["items"]})
            time.sleep(1)
        if e.message == 7:
            pass
        if e.message == 18:
            pass
        if DEBUG_MODE:
            print("\t Код ошибки: {0} | Ошибка: {1} | USER_ID: {2}\n".format(e.message, e.errors, e.user_id))
    else:
        if DEBUG_MODE:
            print(data)
        data_groups_list = data["response"]["items"]
    if DEBUG_MODE:
        print(data_groups_list)
    dict_groups_users.update({user: data_groups_list})


