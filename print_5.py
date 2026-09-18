def tokenizer(ezzylan):
    i = 0
    tokens = []
    token = ""
    space_before = False
    period_before = False
    while i < len(ezzylan):
        character = ezzylan[i]
        if character == " ":
            # if there are two or more spaces back to back, skip this part
            if space_before == False:
                if not token == "": 
                    tokens.append(token)  
                space_before = True
            tokens.append(" ")
            token = ""
        elif character == ".":
            # if there are two or more spaces back to back, skip this part
            if period_before == False:
                if not token == "": 
                    tokens.append(token)  
                space_before = True
            tokens.append(".")
            token = ""
        else:
            token += character
            space_before = False
        i += 1
    # if line ends with space it adds "" to the tokens list, so we take into account that possibility
    if not token == "": 
        tokens.append(token)        
    # print(tokens)
    return(tokens)

def convert(tokens):
    instructions = []
    if not tokens:
        return instructions
    for token in tokens:
        if token == "Print":
            instruction = "PRINT"
        elif token == " ":
            instruction = "SPACE"
        elif token == ".":
            instruction = "END"        
        elif token.isdigit():
            instruction = "NUMBER"
        else:
            instruction = token
        instructions.append(instruction)
    return instructions
    
        
                
    
def main():
    file = open("print_5.ezzylan", "r")
    ezzylan_test = file.read()
    file.close()
    
    lines = ezzylan_test.split("\n")
    for line in lines:
        tokens = tokenizer(line)
        # print(tokens)
        instructions = convert(tokens)
        print(instructions)


        

if __name__ == "__main__":
    main()