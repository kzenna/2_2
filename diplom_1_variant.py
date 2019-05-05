import requests
import time


class VKTimeError(Exception):
    def __init__(self, message, errors, user_id):
        super().__init__(message)
        self.message = message
        self.errors = errors
        self.user_id = user_id


# Флаг отладки
DEBUG_MODE = False
user = '171691064'
TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
url_friends_get = 'https://api.vk.com/method/friends.get'
url_group = 'https://api.vk.com/method/groups.get'
params = {
    'v': '5.92',
    'access_token': TOKEN,
    'user_ids': user
}
response = requests.get(url_friends_get, params)
response_group_user = requests.get(url_group, params)
print(response.json())
friends_user = response.json()
list_friends_user = friends_user["response"]["items"]
print(list_friends_user)
groups_user = response_group_user.json()
list_groups_user = groups_user["response"]["items"]
print('Группы пользователя')
print(list_groups_user)
set_groups_user = set(list_groups_user)

list_friends_groups = []

while len(list_friends_user) > 0:
    users = list_friends_user.pop(0)
    params_fr = {
        'v': '5.92',
        'access_token': TOKEN,
        'user_id': users
    }
    response_friends = requests.get(url_group, params_fr)
    try:
        data = response_friends.json()
        time.sleep(1)
        if DEBUG_MODE:
            print(data)
        if 'error' in data and 'error_code' in data['error']:
            raise VKTimeError(data['error']['error_code'], data['error']['error_msg'], users)
    except VKTimeError as e:
        if e.message == 6:
            # Too many requests per second
            list_friends_user.append(users)
            time.sleep(1)
        if e.message == 7:
            # Permission to perform this action is denied
            None
        if e.message == 18:
            # User was deleted or banned
            None
        if DEBUG_MODE:
            print("\t Код ошибки: {0} | Ошибка: {1} | USER_ID: {2}\n".format(e.message, e.errors, e.user_id))
    else:
        if DEBUG_MODE:
            print(data)
        data_groups_list = data["response"]["items"]
        if DEBUG_MODE:
            print(data_groups_list)
        list_friends_groups.extend(data_groups_list)

print('Это список всех групп участников')
print(list_friends_groups)

set_friends_groups = set(list_friends_groups)
group_task = set_groups_user.difference(set_friends_groups)
print('Это группы, в которых состоит только пользователь')
print(group_task)
