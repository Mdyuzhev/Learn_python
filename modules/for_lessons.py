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
