#
# Домашнее задание к лекции 2.4
# «Открытие и чтение файла, запись в файл»
# Кокурникова Лилия Фаритовна, 23.02.19
#


def read_file_to_list_recipe(file_name, list_recipe):
    with open(file_name, "r", encoding="utf-8") as file:
        i = 1  # признак первой строки
        j = 0  # колличество ингридиентов
        tmp = {}  # временная переменная для записи в словаре
        for line in file:
            line = line.strip()
            if line == "":
                continue
            if i == 1:
                title = line
                i = i + 1
                continue
            if j != 0:
                tmp1 = line.split(' | ')
                tmp[title].append({'ingridient_name': tmp1[0], 'quantity': int(tmp1[1]), 'measure': tmp1[2]})
                j = j - 1
            if line.isdigit():
                j = int(line)
                tmp[title] = []
            if j == 0:  # line == "":
                list_recipe.update(tmp)
                i = 1
                j = 0
                tmp = {}

    print(list_recipe)


def get_shop_list_by_dishes(dishes, person_count):
    # Переменная для хранения рецептов
    recipies = {}
    # Переменная с результатами
    result = {}

    read_file_to_list_recipe("recipes.txt", recipies)

    for recipe_key in recipies:  # Цикл по рецептам
        if recipe_key in dishes:  # проверяем есть ли рецепт в списке выбранных
            for i in recipies[recipe_key]:  # цикл по ингридиентам в выбранном рецепте
                if i['ingridient_name'] in result:  # если ингридиент уже есть в списке продуктов для покупки
                    # result[name].append('')  # дополняем список покупок
                    result[i['ingridient_name']] = {'measure': result[i['ingridient_name']]['measure'],
                                                    'quantity': result[i['ingridient_name']]['quantity'] + (i['quantity'] * person_count)}
                else:
                    result[i['ingridient_name']] = {'measure': i['measure'], 'quantity': i['quantity'] * person_count}
    return result


def main():
    # Список покупок
    try:
        print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
    except FileNotFoundError:
        print('Проверьте существование файла')
    except:
        print('Произошла ошибка')


if __name__ == "__main__":
    main()


