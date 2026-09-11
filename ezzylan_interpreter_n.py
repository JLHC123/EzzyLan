file = open("test_1.ezzylan", "r")
ezzylan = file.read()
file.close()
list_of_tokens = []
tokens = []
token = ""
is_string = False
for line in ezzylan.splitlines():
    # debugging reasons
    # print(line)
    for char in line:
        if char == " ":
            # Before and after "Print", "Let", "x", "equals"...    
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
            if is_string:
                token += char
            # add the period to the tokens list
            else:
                tokens.append(token)
                tokens.append(".") 
                token = "" 
        else:
            token += char
    list_of_tokens.append(tokens)
    tokens = []

# debugging reasons
for tokens in list_of_tokens:
    print(tokens)
    
print(len(list_of_tokens))

printing = 0
while len(list_of_tokens) > 0:
    tokens = list_of_tokens.pop(0)
    while len(tokens) > 0:
        token = tokens.pop(0)
        if token == "Print":
            printing += 1
            try: 
                if printing > 1:
                    raise Exception("Unexpected 'Print' after 'Print'.")
            except SyntaxError:
                print(Exception("Unexpected 'Print' after 'Print'."))
            print_value = ""
            token = tokens.pop(0)
            if token == "\"":
                print_value_type = "STRING"
                print_value = tokens.pop(0)
                try: 
                    token = tokens.pop(0)
                    if token != "\"":
                        raise Exception("Expected closing quote for string.")
                except SyntaxError:
                    print(Exception("Expected closing quote for string."))
        elif token == ".":
            if printing:
                print(print_value)
                printing = False