#
# Домашнее задание к лекции 2.5
# "Менеджер контекста"
# Кокурникова Лилия Фаритовна, 27.02.19

import datetime
import time

class ExecutionTime:
    def __enter__(self):
        self.startTime = time.time()
        self.start = datetime.datetime.now()
        print('Время запуска кода: ' + str(self.start))

    def __exit__(self, type, value, traceback):
        self.endTime = time.time()
        self.end = datetime.datetime.now()
        self.interval = self.endTime - self.startTime
        print('Время окончания кода: ' + str(self.end))
        print('Время, потраченное на выполнение кода: ' + str(self.interval))

#Вычисление числа Фибоначчи:
def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)


with ExecutionTime() as p:
    fibb(30)
