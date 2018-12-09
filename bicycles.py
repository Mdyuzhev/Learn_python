bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1].title())
print(bicycles[-2].title())
message = "My first bicycle was a " + bicycles[0].title()
print(message)
bicycles[1] = 'kama'  # изменение элемента списка
print(bicycles)
bicycles.append('salyut')  # добавление элемента в конец списка
print(bicycles)
bicycles.insert(1, 'shkolnik')  # добавление элемента в произвольное место списка
print(bicycles)
del bicycles[1]  # удаление элемента из списка
print(bicycles)
popped_bicycle = bicycles.pop()  # удаление последнего элемента списка с возможностью его использования
print(bicycles)
print(popped_bicycle)
first_owned = bicycles.pop(0)   # удаление произвольного элемента списка с возможностью его использования
print('The first bicycles I owned was a ' + first_owned.title() + '.')
bicycles.remove('kama')     # удаление элемента и списка по значению
print(bicycles)
too_expensive = 'specialized'
bicycles.remove(too_expensive)
print(bicycles)
bicycles.append('trek')  # добавление элемента в конец списка
bicycles.append('kama')  # добавление элемента в конец списка
bicycles.append('salyut')  # добавление элемента в конец списка
bicycles.append('specialized')  # добавление элемента в конец списка
print(bicycles)


