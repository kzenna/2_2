import requests
import time


class VKTimeError(Exception):
    pass


user = '171691064'
TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
url_friends_get = 'https://api.vk.com/method/friends.get'
url_group = 'https://api.vk.com/method/groups.get'
params = {
    'v': '5.92',
    'access_token': TOKEN,
    'user_ids': user
}
response = requests.get('https://api.vk.com/method/friends.get', params)
response_group_user = requests.get('https://api.vk.com/method/groups.get', params)
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

for users in list_friends_user:
    params_fr = {
        'v': '5.92',
        'access_token': TOKEN,
        'user_id': users
    }
    response_friends = requests.get('https://api.vk.com/method/groups.get', params_fr)
    try:
        data = response_friends.json()
        time.sleep(1)
        if 'error' in data and 'error_code' in data['error'] and data['error']['error_code'] == 6:
            time.sleep(1)
        if 'error' in data and 'error_code' in data['error'] and data['error']['error_code'] != 6:
            raise VKTimeError("Exception Error!")
        else:
            True
    except VKTimeError:
        print('VKTimeError')
    else:
        # print(data)
        data_groups_list = data["response"]["items"]
        # print(data_groups_list)
        list_friends_groups.extend(data_groups_list)

print('Это список всех групп участников')
print(list_friends_groups)

set_friends_groups = set(list_friends_groups)
group_task = set_groups_user.difference(set_friends_groups)
print('Это группы, в которых состоит только пользователь')
print(group_task)


