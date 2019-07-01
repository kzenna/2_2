from diplom_adv import users

"""user.py

Находятся данные интересов пользователя. Результат поиска выводится в виде словаря dict_user_info.

users.py

Находятся данные интересов пользователей, выбранных в заданном диапазоне. Данные выводятся 
в словари {user_id: результат выбранного запроса}.

"""

# print(users.dict_id_books, users.dict_id_music, users.dict_id_movies, users.dict_id_interests,
#       users.dict_groups_users, users.dict_friends_users, sep='\n')


def same_interests(interest):
    return [user_id
            for user_id, user_interest in users.dict_id_interests.items()
            if user_interest == interest]


if __name__ == '__main__':
    same_interests('работа, семья, спорт, книги, интернет')
    # same_interests('работа, спорт, книги')
