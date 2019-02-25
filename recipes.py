#
# Домашнее задание к лекции 2.4
# «Открытие и чтение файла, запись в файл»
# Кокурникова Лилия Фаритовна, 23.02.19
#


def main():
    d = {}
    with open("recipes.txt") as file:
        for line in file:
            key, *value = line.split()
            d[key] = value

"""
    cook_book = [
        ['салат',
         [
             ['картофель', 100, 'гр.'],
             ['морковь', 50, 'гр.'],
             ['огурцы', 50, 'гр.'],
             ['горошек', 30, 'гр.'],
             ['майонез', 70, 'мл.'],
         ]
         ],
        ['пицца',
         [
             ['сыр', 50, 'гр.'],
             ['томаты', 50, 'гр.'],
             ['тесто', 100, 'гр.'],
             ['бекон', 30, 'гр.'],
             ['колбаса', 30, 'гр.'],
             ['грибы', 20, 'гр.'],
         ],
         ],
        ['фруктовый десерт',
         [
             ['хурма', 60, 'гр.'],
             ['киви', 60, 'гр.'],
             ['творог', 60, 'гр.'],
             ['сахар', 10, 'гр.'],
             ['мед', 50, 'мл.'],
         ]
         ]
    ]
    print('Количество персон')
    person = int(input())
    print('СПИСОК ПОКУПОК')
    number_dishes = len(cook_book)
    composition = len(cook_book[2][1])
    x = 0
    while x < number_dishes:
        print(cook_book[x][0].capitalize() + str(':'))
        y = 0
        while y < composition:
            print(cook_book[x][1][y][0] + str(', ') + str((cook_book[x][1][y][1]) * person) + cook_book[x][1][y][2])
            y += 1
        x += 1
        
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
"""

if __name__ == "__main__":
    main()


