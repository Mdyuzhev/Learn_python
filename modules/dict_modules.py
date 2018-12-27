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


def lang():
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
    print("Sarah's favorite language is " +
          favorite_languages['sarah'].title() +
          ".")
    for key, value in favorite_languages.items():
        print(key.title() + "'s favorite language is " + value.title() + ".")
    friends = ['phil', 'sarah']
    for name in favorite_languages.keys():
        print(name.title())
        if name in friends:
            print("Hi " + name.title() + ", I see your favorite languages is " + favorite_languages[name].title() + "!")


def mariya():
    mariya_credentials = {
        'first_name': 'mariya',
        'last_name': 'dyuzheva',
        'city': 'moscow',
        'district': 'teplak',
    }
    for key, value in mariya_credentials.items():
        print("\nKey: " + key)
        print("Value: " + value)


def lang_sorted():
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
    for name in sorted(favorite_languages.keys()):
        print(name.title() + "thank you for taking the poll!")
    print("")
    print("The following languages have been mentioned:")  # список языков в словаре
    for language in favorite_languages.values():
        print(language.title())
    print("")
    print("The following languages have been mentioned:")  # список уникальных значений языков в словаре
    for language in set(favorite_languages.values()):
        print(language.title())


def lang_many():
    favorite_languages = {
        'jen': ['python', 'c'],
        'sarah': ['c'],
        'edward': ['ruby', 'python', 'java'],
        'phil': ['python'],
    }
    for name, languages in favorite_languages.items():
        if len(languages) == 1:
            print("\n" + name.title() + "'s favorite languages are:")
        else:
            print("\n" + name.title() + "'s favorites languages are:")

        for language in languages:
            print("\t" + language.title())


def aliens():
    alien_0 = {'color': 'green', 'points': "5"}
    alien_1 = {'color': 'yellow', 'points': "15"}
    alien_2 = {'color': 'red', 'points': "10"}
    alien_3 = {'color': 'blue', 'points': "15"}
    alien_4 = {'color': 'purple', 'points': "5"}
    aliens = [alien_0, alien_1, alien_2, alien_3, alien_4]
    for alien in aliens:
        print(alien)


def aliens_gen():
    aliens = []
    for alien_number in range(30):
        new_alien = {'color': 'green', 'points': "5", 'speed': 'slow'}
        aliens.append(new_alien)
    for alien in aliens[:10]:
        print(alien)
    print("")
    print("---------------------------------------")
    print("Total number of aliens: " + str(len(aliens)))
    print("---------------------------------------")
    for alien in aliens[0:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 10
    for alien in aliens[0:5]:
        print(alien)
    print("---------------------------------------")


def pizza():
    pizza = {
        'crust': 'thik',
        'toppings': ['mushrooms', 'extra cheese'],
    }
    print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
    for topping in pizza['toppings']:
        print("\t" + topping)


def many_users():
    users = {
        'Эйнштейн': {
            'first': 'albert',
            'last': 'einsteint',
            'location': 'princeton'
        },
        'Кюри': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris'
        }
    }
    for username, user_info in users.items():
        print("\nUsername: " + username)
        full_name = user_info['first'] + " " + user_info['last']
        location = user_info['location']
        print("\tFull name: " + full_name.title())
        print("\tLocation: " + location.title())
