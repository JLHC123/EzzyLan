# converts line of ezzylan code into tokens
def tokenizer(ezzylan, key_characters):
    i = 0
    tokens = []
    token = ""
    while i < len(ezzylan):
        character = ezzylan[i]
        if character == " ":
            if not token == "": 
                tokens.append(token)  
            token = ""
        # simplifies tokenizer, I can later add more characters to key_characters and this logic will apply
        # though I imagine things might get more dicey with parenthesis? Will handle it when we get to that point
        elif character in key_characters:
            if not token == "": 
                tokens.append(token)  
            tokens.append(character)
            token = ""
        else:
            token += character
        i += 1
    if not token == "": 
        tokens.append(token)        
    return(tokens)

def convert(tokens, key_words):
    instructions = []
    if not tokens:
        return instructions
    for token in tokens:
        if token in key_words:
            instructions.append(key_words[token])
        # this may need to get updated when float numbers are considered
        elif token.isdigit():
            instructions.append("NUMBER")
        else:
            instructions.append("ERROR")
    return instructions

def main():
    file = open("print_5.ezzylan", "r")
    ezzylan_test = file.read()
    file.close()
    
    key_words = {
        "Print": "PRINT",
        ".": "END",
        "+": "ADD"
    }
    
    key_characters = {
        ".",
        "+",
    }
    
    lines = ezzylan_test.split("\n")
    for line in lines:
        if not line.strip():
            continue
        tokens = tokenizer(line, key_characters)
        print(tokens)
        instructions = convert(tokens, key_words)
        print(instructions)

if __name__ == "__main__":
    main()  