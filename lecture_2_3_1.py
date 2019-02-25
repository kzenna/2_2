#
# Домашнее задание к лекции 2.3
# "Исключения"
# Задача №1 и №2
# Кокурникова Лилия Фаритовна, 25.02.19

def solve(lst):
    st = []
    doit = ''

    for w in lst:
        if w.isdigit():
            st.append(int(w))
            continue
        assert w in ('+', '-', '*', '/'), 'Неверная комманда!'
        if w in ('+', '-', '*', '/'):
            st.append(w)
            continue
    y = st.pop()
    x = st.pop()
    doit = st.pop()
    z = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y
    }[doit](x, y)
    return z


lst = input('Введите строку:').split()
try:
    print(solve(lst))
except ZeroDivisionError:
    print('Деление на ноль!')
except IndexError:
    print('Неверное колличество параметров!')
except KeyboardInterrupt:
    print('Исключение пользователя!')
except:
    print('Необработанное исключение')



