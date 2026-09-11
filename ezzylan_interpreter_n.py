file = open("test_2.ezzylan", "r")
ezzylan = file.read()
file.close()
list_of_tokens = []
tokens = []
token = ""
is_string = False

for char in ezzylan:
    if char == " ":
        if token != "":
            tokens.append(token)
            token = ""
    else:
        token += char
tokens.append(token)

print(tokens)