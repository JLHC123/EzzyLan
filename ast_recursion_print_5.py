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
    return tokens

def convert(tokens, key_words):
    instructions = []
    # is it even possible for this to be empty? If in main() we just skip empty lines
    if not tokens:
        return instructions # empty line
    for token in tokens:
        if token in key_words:
            instructions.append(key_words[token])
        # this may need to get updated when float numbers are considered
        elif token.isdigit():
            instructions.append("NUMBER")
        else:
            instructions.append("ERROR")
    return instructions



def look_head_what_is_print_expr(instructions, i):
    # out of range index
    if i >= len(instructions):
        print("Error, index range")
        return
    # there's probably a float and string version of this too
    if instructions[i] == "NUMBER":
        print("We are printing a number, expect the end or an addition operator to follow")
        i += 1
        # out of range index
        if i >= len(instructions):
            print("Error, index range")
            return
        if instructions[i] == "END":
            print("We should be done. Check if there are any more tokens")
            i += 1
            # not the end error
            if i < len(instructions):
                print("Error, we have more tokens after the suppossed end of the line of code")
            else:
                print("We are officially done. Passed")
        elif instructions[i] == "ADD":
            print("We are adding something, expect a number to follow")
            i += 1
            look_head_what_is_print_expr(instructions, i)
            # this is the moment we call back to instructions[i] == "NUMBER"
            # thus recursion!
    else:
        print("Expected a number but nothing found")

def look_ahead_index_range(instructions, i):
    if i >= len(instructions):
        print("Error, index range")
        return

def look_ahead(instructions):
    i = 0
    if instructions[i] == "PRINT":
        print("We are printing something, expect a number (or string) to follow")
        i += 1
        # if we think of this as a stand in for expression, this is how the recursive function could work
        look_head_what_is_print_expr(instructions, i)
    else:
        print("Error, expected Print (or other statement) but found nothing")
            
def main():
    file = open("print_5(1).ezzylan", "r")
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
        look_ahead(instructions)

if __name__ == "__main__":
    main()  