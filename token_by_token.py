# Goal: Create a new tokenenizer that not only creates objects of class Token, but will generate and store error messages
def token_by_tokenizer_statements(ezzylan):
    i = 0
    tokens = []
    while i < len(ezzylan):
        token = Token()
        character = ezzylan[i]
        # comment
        if character == "#":
            while i < len(ezzylan) and ezzylan[i] != "\n":
                i += 1
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
                elif character == "#":
                    while i < len(ezzylan) and ezzylan[i] != "\n":
                        i += 1
                elif character == "\n":
                    i += 1
                    continue
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
                    tokens, i = token_by_tokenizer_expression(i, ezzylan, tokens)
                    if tokens and tokens[-1].type == "ERROR":
                        return tokens
            else:
                # if we get here that means that the line ended before it should've 
                token.type = "ERROR"
                token.error = "Unknown word"
                tokens.append(token)
                return tokens
        elif character == "\n":
            i += 1
        # we're not accepting letters here to be honest, at the moment, so we put error
        else:
            token.value = character
            token.type = "ERROR"
            token.error = f"Expected statement, found something that isn't valid at character {i}"
            tokens.append(token)
            return tokens    
    return tokens

def token_by_tokenizer_expression(i, ezzylan, tokens):
    digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while i < len(ezzylan):
        token = Token()
        character = ezzylan[i]
        # comment
        if character == "#":
            return tokens, i
        # skip spaces
        elif character == " ":
            i += 1
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
                    token = Token()
                    token.type = "END"
                    token.value = "."
                    tokens.append(token)
                    i += 1
                    return tokens, i
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
                elif character == "\n":
                    i += 1
                # letter, symbol, not a number character appears instead
                else:
                    token.type = "ERROR"
                    token.value += character
                    token.error = f"Expected number, found something that isn't a digit at character {i}"
                    tokens.append(token)
                    return tokens, i
            else:
                # if we get here that means that the line ended before it should've 
                token.type = "ERROR"
                token.error = "Expected something but line ended early"
                tokens.append(token)
                return tokens, i             
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
                    return tokens, i
            else:
                # if we get here that means that the line ended before it should've 
                token.type = "ERROR"
                token.error = "Expected something but line ended early"
                tokens.append(token)
                return tokens, i
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
                    return tokens, i
            else:
                # if we get here that means that the line ended before it should've 
                token.type = "ERROR"
                token.error = "Expected something but line ended early"
                tokens.append(token)
                return tokens, i            
        elif character == "\n":
            i += 1
        # we're not accepting letters here to be honest, at the moment, so we put error
        else:
            token.value = character
            token.type = "ERROR"
            token.error = f"Expected valid character, found something that isn't at character {i}"
            tokens.append(token)
            return tokens, i    
    return tokens, i

class Token():
    def __init__(self):
        self.type = None
        self.value = None
        self.error = None

class Program():
    def __init__(self):
        self.statements = []
        self.errors = []
        self.valid = True
    def display(self):
        print("Program:")
        for statement in self.statements:
            statement.display(4)
        # if self.errors:
        #     print("Errors:")
        #     for error in self.errors:
        #         print(f"    {error}")
        # else:
        #     for statement in self.statements:
        #         statement.display(4)
    def evaluate(self):
        if self.errors:
            for i in range(len(self.statements) - 1):
                self.statements[i].evaluate()
            for error in self.errors:
                print(f"Error: {error}")
        else:
            for statement in self.statements:
                statement.evaluate()

class PrintStatement():
    def __init__(self):
        self.expression = None
    def display(self, indent):
        print(" " * indent + "PrintStatement:")
        self.expression.display(indent + 4)
    def evaluate(self):
        print(self.expression.evaluate())

class Number():
    def __init__(self, value):
        self.value = value
    def display(self, indent):
        print(" " * indent + f"Number: {self.value}")
    def evaluate(self):
        return self.value
        
class Addition():
    def __init__(self):
        self.left = None
        self.right = None
    def display(self, indent):
        print(" " * indent + "Addition:")
        self.left.display(indent + 4)
        self.right.display(indent + 4)
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

class Subtraction():
    def __init__(self):
        self.left = None
        self.right = None
    def display(self, indent):
        print(" " * indent + "Subtraction:")
        self.left.display(indent + 4)
        self.right.display(indent + 4)
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()

def parser_statement(tokens):
    i = 0
    program = Program()
    if i >= len(tokens):
        return program
    while i < len(tokens) and program.errors == []:
        if tokens[i].type == "PRINT":
            i += 1
            print_statement = PrintStatement()
            i, print_statement.expression = parser_expression(i, tokens, program)
            program.statements.append(print_statement)
    return program

def parser_expression(i, tokens, program):
    if i >= len(tokens):
        program.errors.append("Expected expression, found end of line")
        return i, None
    if tokens[i].type == "NUMBER":
        expression = Number(tokens[i].value)
        i += 1
        while i < len(tokens):
            if tokens[i].type == "ADDITION":
                addition = Addition()
                addition.left = expression            
                i += 1
                if i >= len(tokens):
                    program.errors.append("Expected number after addition operator, found end of line")
                    return i, expression
                if tokens[i].type == "NUMBER":
                    addition.right = Number(tokens[i].value)
                    expression = addition
                else:
                    program.errors.append(f"Expected number after addition operator, found {tokens[i].type}")
                    return i, expression
            elif tokens[i].type == "SUBTRACTION":
                subtraction = Subtraction()
                subtraction.left = expression            
                i += 1
                if i >= len(tokens):
                    program.errors.append("Expected number after subtraction operator, found end of line")
                    return i, expression
                if tokens[i].type == "NUMBER":
                    subtraction.right = Number(tokens[i].value)
                    expression = subtraction
                else:
                    program.errors.append(f"Expected number after subtraction operator, found {tokens[i].type}")
                    return i, expression
            elif tokens[i].type == "END":
                i += 1
                return i, expression
            # lack of operator in between numbers is an error. 
            else:
                program.errors.append(f"Expected operator after number, found {tokens[i].type}")
                return i, expression
            i += 1
        return i, expression

def main():
    # file = open("token_by_token.ezzylan", "r")
    file = open("test_1.ezzylan", "r")
    ezzylan_test = file.read()
    file.close()
    
    print("------------------------------------------------------------------")
    tokens = token_by_tokenizer_statements(ezzylan_test)
    for token in tokens:
        print(f"VALUE: {token.value}")
        print(f"TOKEN TYPE: {token.type}")
        print(f"ERROR: {token.error}")
    program = parser_statement(tokens)
    # Now the program refuses to evaluate if there are errors
    # Goal, make it display up to the errors
    program.display()
    program.evaluate()
    
    # lines = ezzylan_test.split("\n")
    # for line in lines:
    #     if not line.strip():
    #         continue
    #     print("------------------------------------------------------------------")
    #     tokens = token_by_tokenizer_statements(line)
    #     print(line)
    #     for token in tokens:
    #         print(f"VALUE: {token.value}")
    #         print(f"TOKEN TYPE: {token.type}")
    #         print(f"ERROR: {token.error}")
    #     if tokens and tokens[-1].type != "ERROR":
    #         program = parser_statement(tokens)
    #         program.display()
    #         if not program.errors:
    #             program.evaluate()
      
if __name__ == "__main__":
    main()