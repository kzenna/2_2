import requests
import time
from tqdm import tqdm


class VKTimeError(Exception):
    def __init__(self, message, errors, user_id):
        super().__init__(message)
        self.message = message
        self.errors = errors
        self.user_id = user_id


def get_users_friends_groups(param, url_friends_get, url_group):
    response = requests.get(url_friends_get, param)
    response_group_user = requests.get(url_group, param)
    friends_user = response.json()
    list_friends_user = friends_user["response"]["items"]
    groups_user = response_group_user.json()
    list_groups_user = groups_user["response"]["items"]
    group_task = set(list_groups_user)
    if DEBUG_MODE:
        print("Друзья пользователя {0}".format(list_friends_user))
        print("Группы пользователя {0}".format(list_groups_user))
    else:
        n = 0
        p_bar = tqdm(list_friends_user)
    while len(list_friends_user) > 0:
        users = list_friends_user.pop(0)
        params_fr = {
            'v': params['v'],
            'access_token': params['access_token'],
            'user_id': users
        }
        response_friends = requests.get(url_group, params_fr)
        try:
            data = response_friends.json()
            time.sleep(1)
            if DEBUG_MODE:
                print("Группы пользователя {0}: {1}".format(users, data))
            if 'error' in data and 'error_code' in data['error']:
                raise VKTimeError(data['error']['error_code'], data['error']['error_msg'], users)
        except VKTimeError as e:
            if DEBUG_MODE:
                print("\t Код ошибки: {0} | Ошибка: {1} | USER_ID: {2}\n".format(e.message, e.errors, e.user_id))
            if e.message == 6:
                list_friends_user.append(users)
                time.sleep(1)
        else:
            data_groups_list = data["response"]["items"]
            group_task = group_task.difference(data_groups_list)
            if DEBUG_MODE:
                print("Изменения итогового списка: {1} \t Данные: {0}".format(data, data_groups_list, sep='\n'))
                print("Измененый итоговый список: {0}".format(group_task, sep='\n'))
            else:
                n += 1
                p_bar.update(n)
                p_bar.set_description("Processing user [%s]" % users)
    if not DEBUG_MODE:
        p_bar.close()
        time.sleep(1)
    print('\nЭто группы, в которых состоит только этот пользователь, а не его друзья: {}'.
          format(','.join(map(str, group_task))))


if __name__ == '__main__':
    DEBUG_MODE = False
    user = '78028538'  # 78028538 171691064
    TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
    url_friends_gets = 'https://api.vk.com/method/friends.get'
    url_groups = 'https://api.vk.com/method/groups.get'
    params = {
        'v': '5.92',
        'access_token': TOKEN,
        'user_id': user
    }
    get_users_friends_groups(params, url_friends_gets, url_groups)
