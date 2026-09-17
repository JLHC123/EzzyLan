file = open("Luigi.ezzylan", "r")
ezzylan = file.read()
file.close()
token = ""
tokens = []
is_string = False

# activte Luigi Assist Mode
for char in ezzylan:
    if char == " ":
        if is_string == True:
            token += char
        else:
            if token != "":
                tokens.append(token)
                tokens.append(char)
                token = ""
            else:
                tokens.append(char)
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
    else:
        token += char
        
print(tokens)

first_token = tokens.pop(0)
try:
    if first_token == "Print":
        try:
            is_space = tokens.pop(0)
            if is_space != " ":
                raise SyntaxError("Expected space after Print")
            else:
                token = tokens.pop(0)
                if token == "\"":
                    string = tokens.pop(0)
                    try:
                        is_end_quote = tokens.pop(0)
                        if is_end_quote != "\"":
                            raise SyntaxError("Expected closing quote after string")
                        else:
                            valid_string = string
                            try:
                                is_end = tokens.pop(0)
                                if is_end != ".":
                                    raise SyntaxError("Expected period after string")
                                else:
                                    print(valid_string)
                            except SyntaxError as e:
                                print("Syntax Error: " + str(e))
                    except SyntaxError as e:
                        print("Syntax Error: " + str(e))
                else:
                    raise SyntaxError("Expected string after Print")
        except SyntaxError as e:
            print("Syntax Error: " + str(e))
    else:
        raise Exception("Invalid first token")
except SyntaxError as e:
    print("Syntax Error: " + str(e))
    