file = open("test_1.ezzylan", "r")
ezzylan = file.read()
file.close()
tokens = []
token = ""
is_string = False
for char in ezzylan:
    if char == " ":
        # at the end of "Print", "Let", "x", "equals"...    
        if not is_string and token != "":      
            tokens.append(token)
            token = ""
        # we're inside a string so we add the space to the token
        elif is_string: 
            token += char
    elif char == "\"":
        # the first parenthesis of a string
        if not is_string:
            # add the first parenthesis to the tokens list
            tokens.append("\"") 
            # reset the token (might not be necessary)
            token = "" 
            # we're now in the string
            is_string = True 
        # last parenthesis of a string
        else: 
            # add what's inside
            tokens.append(token)
            # add the last parenthesis to the tokens list
            tokens.append("\"") 
            # we're now out of the string
            is_string = False  
            # reset the token (might not be necessary)
            token = ""  
    # end of the statement
    elif char == ".": 
        # add the period to the tokens list
        tokens.append(token)
        tokens.append(".") 
        token = "" 
    else:
        token += char

print(tokens)

printing = 0
while len(tokens) > 0:
    token = tokens.pop(0)
    if token == "Print":
        printing += 1
        try: 
            if printing > 1:
                raise Exception("Unexpected 'Print' after 'Print'.")
        except Exception as e:
            print(e)
        print_value = ""
        token = tokens.pop(0)
        if token == "\"":
            print_value_type = "STRING"
            print_value = tokens.pop(0)
            try: 
                token = tokens.pop(0)
                if token != "\"":
                    raise Exception("Expected closing quote for string.")
            except IndexError:
                print(Exception("Expected closing quote for string."))
    elif token == ".":
        if printing:
            print(print_value)
            printing = False
        
    

    