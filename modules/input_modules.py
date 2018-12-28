def parrot():
    message = input("Tell me something, and i will repeat it back to you: ")
    print(message)


def greeter():
    name = input("Please enter your name: ")
    print("Hello, " + name + "!")


def greeter_prompt():
    prompt = "If you tell us who you are, we can personalize the messages you see"
    prompt += "\nWhat is your first name? "
    name = input(prompt)
    print("Hello, " + name + "!")
    age = input("How old are you? ")
    age = int(age)


def parrot_while():
    prompt = "Tell me something, and i will repeat it back to you: "
    prompt += "\nEnter 'quit' to end the program.\n"
    active = True
    while active:
        message = input(prompt)
        if message == 'quit':
            active = False
        else:
            print(message)


def parrot_breake():
    prompt = "Tell me something, and i will repeat it back to you: "
    prompt += "\nEnter 'quit' to end the program.\n"
    while True:
        message = input(prompt)
        if message == 'quit':
            break
        else:
            print(message)


def confirmed_users():
    unconfirmed_users = ['alice', 'brian', 'candace']
    confirmed_users = []
    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print("Verifying user: " + current_user.title())
        confirmed_users.append(current_user)
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())


def pets():
    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print(pets)
    while 'cat' in pets:
        pets.remove('cat')
    print(pets)


def mountain_poll():
    responses = {}
    polling_active = True
    while polling_active:
        name = input("\nWhat's your name? ")
        response = input("Which mountain would you like to climb someday? ")
        responses[name] = response
        repeat = input("Would you like to let another person respond? (yes/no)")
        if repeat == 'no':
            polling_active = False
            print("\n---Poll Results---")
            for name, response in responses.items():
                print(name + " would like to climb " + response + ".")




