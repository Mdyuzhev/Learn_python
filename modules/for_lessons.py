def even_or_odd():
    number = input("Enter a number, and i'll tell you if it's even or odd: ")
    number = int(number)
    if number % 2 == 0:
        print("\nThe number " + str(number) + " is even.")
    else:
        print("\nThe number " + str(number) + " is odd.")


def counting():
    current_number = 1
    while current_number <= 100:
        print(current_number)
        current_number += 1


def counting_continue():
    current_number = 1
    while current_number <= 100:
        current_number += 1
        if current_number % 2 == 0:
            continue
        print(current_number)


def describe_pets(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


def greeter_while():
    while True:
        print("\nPlease Tell me your name: ")
        print("{enter 'q' at any time to quit")

        first_name = input("First name: ")
        if first_name == 'q':
            break

        last_name = input("Last name: ")
        if last_name == 'q':
            break
        full_name = first_name + ' ' + last_name
        print("Hello, " + full_name.title() + "!")
        break
