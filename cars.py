cars = ['bmv', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()  # сортировка списка в алфавитном порядке
print(cars)
cars = ['bmv', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort(reverse=True)  # сортировка списка в обратном алфавитном порядке
print(cars)
cars = ['bmv', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")  # временная сортировка списка, без изменения первоначального
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
print("\nHere is the sorted list:")  # временная сортировка списка, без изменения первоначального
print(sorted(cars, reverse=True))
print("\nHere is the original list again:")  # временная сортировка списка, без изменения первоначального
# в обратном порядке
print(cars)
cars.reverse()      # сортировка списка в обратном порядке постоянное изменение
print(cars)
cars.reverse()
cars = ['bmv', 'audi', 'toyota', 'subaru']
print(len(cars))      # Определение дины списка

