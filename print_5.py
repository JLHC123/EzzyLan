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

def convert(tokens, key_words):
    instructions = []
    if not tokens:
        return instructions
    for token in tokens:
        if token in key_words:
            instructions.append(key_words[token])
        elif token.isdigit():
            instructions.append("NUMBER")
    return instructions

# will refine this (when I have more "valid statements")
def execute(instructions, tokens):
    if instructions == ['PRINT', 'SPACE', 'NUMBER', 'END']:
        for token in tokens:
            if token.isdigit():
                number = int(token)
                print(number)
                return
    else:
        print("Not a valid line")             
    
def main():
    file = open("print_5.ezzylan", "r")
    ezzylan_test = file.read()
    file.close()
    
    key_words = {
        "Print": "PRINT",
        ".": "END",
        " ": "SPACE",
    }
    
    lines = ezzylan_test.split("\n")
    for line in lines:
        tokens = tokenizer(line)
        # print(tokens)
        instructions = convert(tokens, key_words)
        # print(instructions)
        execute(instructions, tokens)


        

if __name__ == "__main__":
    main()