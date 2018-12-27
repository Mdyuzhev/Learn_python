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
