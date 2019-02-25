#
# Домашнее задание к лекции 2.3
# "Исключения"
# Задача №3
# Кокурникова Лилия Фаритовна, 25.02.19

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "123"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def people_search():
    print('Поиск человека по документу')
    number_doc = input('Введите номер документа: ')
    search = 0
    for i in documents:
        if i['number'] == number_doc:
            search = 1
            try:
              print(i['name'])
            except KeyError:
              print('Не найдено поле name у документа')
    if search == 0:
      print('Не найдено')


def list_doc():
    print('Печать всех документов в формате "Паспорт" "ФИО"')
    for i in documents:
        print('"{0}" "{1}"'.format(i['number'], i['name']))


def shelf_doc():
    print('Поиск полки по номеру документа')
    number_doc = input('Введите номер документа: ')
    search = 0
    for number, document_dic in directories.items():
        for i in document_dic:
            if i == number_doc:
                print('Номер полки: {}'.format(number))
                search = 1
    if search == 0:
      print('Не найдено')


def add_doc():
    print('Добавление нового документа в каталог и в перечень полок, '
          'спросив его номер, '
          'тип, '
          'имя владельца и '
          'номер полки, на котором он будет храниться.')
    number_doc = input('Введите номер документа: ')
    type_doc = input('Введите тип документа: ')
    fio_doc = input('Введите имя владельца документа: ')
    directory_doc = input('Введите номер полки для документа: ')

    if directory_doc in directories:
        directories[directory_doc].append(number_doc)
    else:
        directories[directory_doc] = [number_doc]

    documents.append({"type": type_doc, "number": number_doc, "name": fio_doc})


def main():
    print("База данных:\n p - поиск человека по номера документа\n \
l - список всех документов\n \
s - поиск полки  по номеру документа\n \
a - добавление новых документов\n \
e - выход")

    while 1:
        command = input('Введите комманду >>> ')
        if command == 'p':
            people_search();
        if command == 'l':
            list_doc();
        if command == 's':
            shelf_doc();
        if command == 'a':
            add_doc();
        if command == 'e':
            print('bye')
            break


if __name__ == "__main__":
    main()
