def range1(i):
    for value in range(1, i):
        print(value)


def list_range(i):
    numbers = list(range(1, i))  # создание числового списка от 1 до 5
    print(numbers)


def list_range_ex():
    numbers = list(range(3, 31, 3))  # создание числового списка от 2 до 10 с приращением 2
    print(numbers)


def squares(end):
    squares = []
    for value in range(1, end):
        squares.append(value ** 2)  # возведение в степень и внесение в список
    print(squares)
    print(min(squares))  # минимум из списка чисел
    print(max(squares))  # максимум из списка чисел
    print(sum(squares))  # сумма элементов списка


def list_gen():
    squares1 = [value ** 3 for value in range(1, 11)]  # генератор списка чисел с квадратом
    print(squares1)


def list_players():
    players = []
    number = 0

    for value in range(1, 12, 1):
        players.append("Ivan" + str(number))
        number = int(number) + 1

    print(players)  # вывести весь список игроков
    print(players[0:3])  # вывести первых троих -- срезы списка
    print(players[1:4])
    print(players[:5])
    print(players[2:])
    print(players[-3:])


def print_list_of_players():  # перебор первых трех элементов списка
    players = []
    number = 0
    print("Here are the first three players on my team: ")
    for value in range(1, 120, 1):
        players.append("Mikhail_" + str(number))
        number = int(number) + 1
    for player in players[:39]:
        print(player.title())


def list_generator(member=str(), len_list=int(), step_in_list=int(), first_number=int()):
    list_name = []
    number = 0
    for value in range(first_number, len_list, step_in_list):
        list_name.append(member + str(number))
        number = int(number) + 1
    return list_name


def foods():
    my_foods = list_generator("Pizzzza", 5, 1, 0)[:]
    friend_food = my_foods[:]
    print("My favorite foods are: ")
    my_foods.append("element")
    for food in my_foods:
        print(food.title())
    print("\nMy friend's favorite foods are: ")
    friend_food.append("element_another")
    for food in friend_food:
        print(food.title())
    return my_foods


def swed_table():
    table = tuple(list_generator("plate", 5, 1, 0)[:])  # приведение списка к кортежу
    print(table)


def cars_if():
    cars = ["audi", "bmw", "toyota", "subaru"]
    for car in cars:
        if car.lower() == "bmw":  # перед сравнением всегда приводить к нижнему регистру
            print(car.upper())
        else:
            print(car.title())


def check_age(age=int()):
    age = age
    if age != 18:
        print("gohome")
    elif age == 18:
        print("you are welcome")


def check_list(topping_number=str()):  # проверка на вхождение значения в список
    toppings = list_generator("topping", 5, 1, 0)[:]
    adding_toping = "topping%s" % topping_number

    if adding_toping in toppings:  # входит в список
        print(toppings)
        print("gotohell")
    elif adding_toping not in toppings:  # не входит в список
        toppings.append(adding_toping)
        print("you are welcome")
        print(toppings)


def car_subaru():
    car = 'subaru'
    print("Is car == 'subaru'? True")
    print(car == 'subaru')
    print("Is car == 'audi'? False")
    print(car == 'audi')


def available_list():  # множественные списки, проверка наличия элементов одного писка в другом списке
    available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
    requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
    for reguested_topping in requested_toppings:
        if reguested_topping in available_toppings:
            print("Adding " + reguested_topping + ".")
        else:
            print("Sorry, we don't have " + reguested_topping + ".")

    print("\nFinished making your pizza!")
