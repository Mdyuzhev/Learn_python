message = "Hello World"
print(message)
message = "Hello Python World"
print(message)
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

print("\tPython")
print("languages:\n\tPython\n\tC\n\tJavascript")

favorite_language = 'Python '
print(favorite_language)
print(favorite_language.rstrip())  # временное удаление пропусков справа
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)  # постоянное удаление пропусков справа

favorite_language = ' Python'
print(favorite_language)
print(favorite_language.lstrip())  # временное удаление пропусков слева

favorite_language = ' Python '
print(favorite_language)
print(favorite_language.strip())  # временное удаление пропусков слева и справа
