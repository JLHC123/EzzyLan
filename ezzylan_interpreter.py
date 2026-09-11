file = open("test_1.ezzylan", "r")
ezzylan = file.read()
file.close()

tokens = []
token = ""
for char in ezzylan:
    if char == " ":
        tokens.append(token)
        token = ""
    if char == "\"":
        tokens.append("\"")
        token = ""
    if char == ".":
        tokens.append(".")
        token = ""
    token += char
for token in tokens:
    print(token)
