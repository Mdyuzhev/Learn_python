def alien():
    alien_o = {}  # создание пустого словаря
    print(alien_o)
    alien_o['color'] = 'green'  # добавление элементовв словарь
    alien_o['points'] = 5
    print("The Alien is " + alien_o['color'] + ".")
    alien_o['color'] = 'yellow'
    print("The Alien now " + alien_o['color'] + ".")
    print(alien_o['points'])
    alien_o['x_position'] = 0  # добавление элементовв словарь
    alien_o['y_position'] = 25
    alien_o['speed'] = 'medium'
    print("Original x-position: " + str(alien_o['x_position']))
    # пришелец перемещается в право
    # Вычисляем ведичину смещения на основании текущей скорости
    if alien_o['speed'] == 'slow':
        x_increment = 1
    elif alien_o['speed'] == 'medium':
        x_increment = 2
    else:
        # Пришелец двигается быстро
        x_increment = 3
    # Новая позиция равна сумме старой позиции и приращения
    alien_o['x_position'] = alien_o['x_position'] + x_increment
    print("New x-position: " + str(alien_o['x_position']))
    del alien_o['points']
    print(alien_o)


