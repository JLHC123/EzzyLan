file = open("print_5.ezzylan", "r")
ezzylan = file.read()
file.close()

i = 0
tokens = []
token = ""
space_before = False


while i < len(ezzylan):
    character = ezzylan[i]
    if character == " ":
        # if there are two or more spaces back to back, skip this part
        if space_before == False:
            tokens.append(token)
            space_before = True
        tokens.append(" ")
        token = ""
    else:
        token += character
        space_before = False
    i += 1 
tokens.append(token)
        
print(tokens)