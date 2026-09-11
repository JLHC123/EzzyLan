file = open("test_2.ezzylan", "r")
ezzylan = file.read()
file.close()
tokens = []
token = ""
is_string = False

for char in ezzylan:
    if char == " ":
        if token != "":
            tokens.append(token)
            token = ""
    elif char == "\"":
        if is_string == False:
            is_string = True
            tokens.append(char)
        else:
            is_string = False
            tokens.append(token)
            tokens.append(char)
            token = ""
    elif char == ".":
        if is_string:
            token += char
        else:
            if token != "":
                tokens.append(token)
                token = ""
            tokens.append(char)
    elif char == "\n":
        if token != "":
            tokens.append(token)
            token = ""
        tokens.append(char)
    else:
        token += char
tokens.append(token)

print(tokens)