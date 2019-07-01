from diplom_adv import users

"""user.py

Находятся данные интересов пользователя. Результат поиска выводится в виде словаря dict_user_info.

users.py

Находятся данные интересов пользователей, выбранных в заданном диапазоне. Данные выводятся 
в словари {user_id: результат выбранного запроса}.

"""

if __name__ == '__main__':
    users.__USER_ID__ = '545472010'
    users.__DEBUG_MODE__ = True
    users.__TOKEN__ = '2a3035afb76507e7737b7c80fb53d80d8f1ae404ba12e4418f74a9a918c49ebe2b74b3501c03c5ad3bcea'
    print("Введите id VK\n \
    enter - выход")
    while 1:
        command = input('>>> ')
        if command == '':
            print('bye')
            break
        else:
            users.__USER_ID__ = command
            users.same_interests('работа, семья, спорт, книги, интернет')
            # same_interests('работа, спорт, книги')
