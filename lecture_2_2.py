# Домашнее задание к лекции 2.2
# «Классы и их применение в Python»
#
# Кокурникова Лилия Фаритовна, 10.03.19
#


class Animal:
    max_weight = 0
    max_animal = None

    def __init__(self, name, nickname, feeding, weight):
        self.name = name
        self.feeding = feeding
        self.weight = weight
        self.nickname = nickname

    def makeNoise(self):
        pass


class Birds(Animal):
    def info(self):
        print(self.name + " ест " + self.feeding)

    def bird_weight(self):
        print(self.name + " по кличке " + self.nickname + " весит " + self.weight + " кг. ")


class Cattle(Animal):
    def cut(self):
        print(self.name + " дает шерсть")

    def milk(self):
        print(self.name + " дает молоко")

    def cuttle_weight(self):
        print(self.name + " по кличке " + self.nickname + " весит " + self.weight + " кг. ")

    def info(self):
        print(self.name + " ест " + self.feeding)


class hen(Birds):
    def makeNoise1(self):
        print(self.name + " говорит: ко-ко и дает яйца")

    def makeNoise2(self):
        print(self.name + " говорит: кукареку")


class goose(Birds):
    def makeNoise(self):
        print(self.name + " говорит: га-га")


class duck(Birds):
    def makeNoise(self):
        print(self.name + " говорит: кря-кря")


class cow(Cattle):
    def makeNoise(self):
        print(self.name + " говорит: му-му")


class sheep(Cattle):
    def makeNoise(self):
        print(self.name + " говорит: бе-бе")


class goat(Cattle):
    def makeNoise(self):
        print(self.name + " говорит: ме-ме")


hen1 = hen("Курица", "Коко", "зерно", "2")
if hen.max_weight < int(getattr(hen1, 'weight')):
    hen.max_weight = int(getattr(hen1, 'weight'))
    hen.max_animal = getattr(hen1, 'name')
hen1.info()
hen1.makeNoise1()
hen1.bird_weight()

hen2 = hen("Петух", "Кукареку", "зерно", "3")
if hen.max_weight < int(getattr(hen2, 'weight')):
    hen.max_weight = int(getattr(hen2, 'weight'))
    hen.max_animal = getattr(hen2, 'name')
hen2.info()
hen2.makeNoise2()
hen2.bird_weight()

duck1 = duck("Утка", "Кряква", "зерно", "3")
if hen.max_weight < int(getattr(duck1, 'weight')):
    hen.max_weight = int(getattr(duck1, 'weight'))
    hen.max_animal = getattr(duck1, 'name')
duck1.info()
duck1.makeNoise()
duck1.bird_weight()

goose1 = goose("Гусь", "Белый", "зерно", "5")
if hen.max_weight < int(getattr(goose1, 'weight')):
    hen.max_weight = int(getattr(goose1, 'weight'))
    hen.max_animal = getattr(goose1, 'name')
goose1.info()
goose1.makeNoise()
goose1.bird_weight()

goose2 = goose("Гусь", "Серый", "зерно", "7")
if hen.max_weight < int(getattr(goose2, 'weight')):
    hen.max_weight = int(getattr(goose2, 'weight'))
    hen.max_animal = getattr(goose2, 'name')
goose2.bird_weight()

cow1 = cow("Корова", "Манька", "сено", "300")
if hen.max_weight < int(getattr(cow1, 'weight')):
    hen.max_weight = int(getattr(cow1, 'weight'))
    hen.max_animal = getattr(cow1, 'name')
cow1.milk()
cow1.makeNoise()
cow1.cuttle_weight()

sheep1 = sheep("Овца", "Барашек", "сено", "50")
if hen.max_weight < int(getattr(sheep1, 'weight')):
    hen.max_weight = int(getattr(sheep1, 'weight'))
    hen.max_animal = getattr(sheep1, 'name')
sheep1.cut()
sheep1.makeNoise()
sheep1.cuttle_weight()

sheep2 = sheep("Овца", "Кудрявый", "сено", "60")
if hen.max_weight < int(getattr(sheep2, 'weight')):
    hen.max_weight = int(getattr(sheep2, 'weight'))
    hen.max_animal = getattr(sheep2, 'name')
sheep2.cuttle_weight()

goat1 = goat("Коза", "Рога", "сено", "50")
if hen.max_weight < int(getattr(goat1, 'weight')):
    hen.max_weight = int(getattr(goat1, 'weight'))
    hen.max_animal = getattr(goat1, 'name')
goat1.milk()
goat1.makeNoise()
goat1.cuttle_weight()

goat2 = goat("Коза", "Копыта", "сено", "60")
if hen.max_weight < int(getattr(goat2, 'weight')):
    hen.max_weight = int(getattr(goat2, 'weight'))
    hen.max_animal = getattr(goat2, 'name')
goat2.cuttle_weight()

weight_list = (int(getattr(hen1, 'weight')), int(getattr(hen2, 'weight')), int(getattr(duck1, 'weight')), int(
        getattr(goose1, 'weight')), int(getattr(goose2, 'weight')), int(getattr(cow1, 'weight')), int(
        getattr(sheep1, 'weight')), int(getattr(sheep2, 'weight')), int(getattr(goat1, 'weight')), int(
        getattr(goat2, 'weight')))
weight_list_sort = sorted((weight_list), reverse = True)
heaviest = weight_list_sort[0]
sum_weight = sum(weight_list)

print("Общий вес животных: " + str(sum_weight) + " кг.")
# print("Самое тяжелое животное: " + str(heaviest) + " кг.")
print("Самое тяжелое животное: {} {} кг.".format(hen.max_animal, str(hen.max_weight)))
