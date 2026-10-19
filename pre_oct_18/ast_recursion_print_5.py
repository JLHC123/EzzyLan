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

def look_ahead_number_expression_loop(is_valid, instructions, i, number_expression):
    print("We are printing a number, expect the end or an addition operator to follow")
    i += 1
    # out of range index
    if i >= len(instructions):
        print("Error, index range")
        is_valid = False
        return is_valid, number_expression
    if instructions[i] == "END":
        print("We should be done. Check if there are any more tokens")
        number_expression.append("END")
        i += 1
        # not the end error
        if i < len(instructions):
            print("Error, we have more tokens after the suppossed end of the line of code")
            is_valid = False
            return is_valid, number_expression
        # end
        else:
            print("We are officially done. Passed")
            is_valid = True
            return is_valid, number_expression
    elif instructions[i] == "ADD":
        print("We are adding something, expect a number to follow")
        i += 1
        number_expression.append("ADD")
        if i >= len(instructions):
            print("Error, index range")
            is_valid = False
            return is_valid, number_expression
        if instructions[i] == "NUMBER":
            additional_expression = []
            additional_expression.append("NUMBER")
            is_valid, additional_expression = look_ahead_number_expression_loop(is_valid, instructions, i, additional_expression)
            number_expression.append(additional_expression)
            return is_valid, number_expression
        else:
            print("Expected a number but nothing found")
            is_valid = False
            return is_valid, number_expression
    # forgot to add this lol
    else:
        print("Error, expected end or addition operator but found nothing")
        is_valid = False
        return is_valid, number_expression

def look_ahead_what_is_being_printed(is_valid, instructions, i, print_statement):
    # out of range index
    if i >= len(instructions):
        print("Error, index range")
        is_valid = False
        return is_valid, print_statement
    # there's probably a float and string version of this too
    if instructions[i] == "NUMBER":
        number_expression = []
        number_expression.append("NUMBER")
        is_valid, number_expression = look_ahead_number_expression_loop(is_valid, instructions, i, number_expression)
        print_statement.append(number_expression)
        return is_valid, print_statement
    else:
        print("Expected a number but nothing found")
        is_valid = False
    return is_valid, print_statement

def look_ahead_what_is_first_statement(is_valid, instructions, code):
    i = 0
    if instructions[i] == "PRINT":
        print("We are printing something, expect a number (or string) to follow")
        i += 1
        print_statement = []
        print_statement.append("PRINT")
        # if we think of this as a stand in for expression, this is how the recursive function could work
        is_valid, print_statement = look_ahead_what_is_being_printed(is_valid, instructions, i, print_statement)
        code.append(print_statement)
    else:
        print("Error, expected Print (or other statement) but found nothing")
        is_valid = False
    return is_valid, code
            
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
        is_valid = None
        # what I'm doing is I'm trying to replicate what it could be like for a program to have a statement and then expression as part of the statment
        # and then the expression has a sub statement too
        code = []
        is_valid, code = look_ahead_what_is_first_statement(is_valid, instructions, code)
        print(is_valid)
        print(code)

if __name__ == "__main__":
    main()  