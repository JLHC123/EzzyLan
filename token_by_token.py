# Goal: Create a new tokenenizer that not only creates objects of class Token, but will generate and store error messages
def token_by_tokenizer(ezzylan):
    i = 0
    digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    tokens = []
    while i < len(ezzylan):
        token = Token()
        character = ezzylan[i]
        # comment
        if character == "#":
            return tokens
        # skip spaces
        elif character == " ":
            i += 1
        elif character.isalpha():
            token.value = character
            i += 1
            while i < len(ezzylan):
                character = ezzylan[i]
                if character == " ":
                    i += 1
                    break
                elif character.isalpha():
                    token.value += character
                    i += 1
                else:
                    token.type = "ERROR"
                    token.value += character
                    token.error = "Was adding letters, found something that wasn't a letter"
                    tokens.append(token)
                    return tokens
            if token.value == "Print":
                if i >= len(ezzylan):
                    token.type = "ERROR"
                    token.error = "Expected something to print but line ended early"
                    tokens.append(token)
                    return tokens
                else:
                    token.type = "PRINT"
                    tokens.append(token) 
            else:
                # if we get here that means that the line ended before it should've 
                token.type = "ERROR"
                token.error = "Unknown word"
                tokens.append(token)
                return tokens
        # token is now number
        elif character in digit:
            token.type = "NUMBER"
            token.value = character
            i += 1
            while i < len(ezzylan):           
                character = ezzylan[i]
                # the line ends with the number which can be valid
                if character == ".":
                    token.value = int(token.value)
                    tokens.append(token)
                    i += 1
                    break
                # we reached the end of the number
                elif character == " ":
                    token.value = int(token.value)
                    tokens.append(token)
                    i += 1
                    break
                # still adding digits to the number
                elif character in digit:
                    token.value += character
                    i += 1
                # letter, symbol, not a number character appears instead
                else:
                    token.type = "ERROR"
                    token.value += character
                    token.error = f"Expected number, found something that isn't a digit at character {i}"
                    tokens.append(token)
                    return tokens
            else:
                # if we get here that means that the line ended before it should've 
                token.type = "ERROR"
                token.error = "Expected something but line ended early"
                tokens.append(token)
                return tokens             
        elif character == "+":
            token.type = "ADDITION"
            # for now token.value will equal the + for debugging pruposes
            token.value = "+"
            i += 1
            while i < len(ezzylan):
                character = ezzylan[i]
                # only correct response
                if character == " ":
                    tokens.append(token)
                    i += 1
                    break
                else:
                    token.type = "ERROR"
                    token.value += character
                    token.error = "Expected space, found character that shouldn't be there"
                    tokens.append(token)
                    return tokens
            else:
                # if we get here that means that the line ended before it should've 
                token.type = "ERROR"
                token.error = "Expected something but line ended early"
                tokens.append(token)
                return tokens
        elif character == "-":
            token.type = "SUBTRACTION"
            token.value = "-"
            i += 1
            while i < len(ezzylan):
                character = ezzylan[i]
                if character == " ":
                    tokens.append(token)
                    i += 1
                    break
                else:
                    token.type = "ERROR"
                    token.value += character
                    token.error = "Expected space, found character that shouldn't be there"
                    tokens.append(token)
                    return tokens
            else:
                # if we get here that means that the line ended before it should've 
                token.type = "ERROR"
                token.error = "Expected something but line ended early"
                tokens.append(token)
                return tokens             
        # we're not accepting letters here to be honest, at the moment, so we put error
        else:
            token.type = "ERROR"
            token.error = f"Expected number, found something that isn't a number at character {i}"
            tokens.append(token)
            return tokens    
    return tokens

class Token():
    def __init__(self):
        self.type = None
        self.value = None
        self.error = None
        

def main():
    file = open("token_by_token.ezzylan", "r")
    ezzylan_test = file.read()
    file.close()
    
    # number = Token()
    # tokens = []
    # number.type = "NUMBER"
    # number.value = "123"
    # print(number)
    # print(number.type)
    # print(number.value)
    # tokens.append(number)
    
    lines = ezzylan_test.split("\n")
    for line in lines:
        if not line.strip():
            continue
        print("------------------------------------------------------------------")
        tokens = token_by_tokenizer(line)
        print(line)
        for token in tokens:
            print(f"VALUE: {token.value}")
            print(f"TOKEN TYPE: {token.type}")
            print(f"ERROR: {token.error}")
        
        
if __name__ == "__main__":
    main()