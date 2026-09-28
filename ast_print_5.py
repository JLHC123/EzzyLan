def tokenizer(ezzylan):
    i = 0
    tokens = []
    token = ""
    space_before = False
    # period_before = False
    # plus_before = False
    while i < len(ezzylan):
        character = ezzylan[i]
        if character == " ":
            # if there are two or more spaces back to back, skip this part
            if space_before == False:
                if not token == "": 
                    tokens.append(token)  
                space_before = True
            token = ""
        # temporarily will disable periods to simplify things to just Print 5
        # elif character == ".":
        #     # if there are two or more spaces back to back, skip this part
        #     if period_before == False:
        #         if not token == "": 
        #             tokens.append(token)  
        #         period_before = True
        #     tokens.append(".")
        #     token = ""
        # same with addition
        # elif character == "+":
        #     # should i++ / some form of this exist in the code?
        #     if plus_before == False:
        #         if not token == "":
        #             tokens.append(token)
        #         plus_before = True
        #     tokens.append("+")
        #     token = ""
        else:
            token += character
            space_before = False
            # plus_before = False
            # period_before = False
        i += 1
    # if line ends with space it adds "" to the tokens list, so we take into account that possibility
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

class Print():
    # a Print statement has an expression to print
    def __init__(self, expression):
        self.expression = expression
    # in the visual tree we print "Print" with indentation and then call to print the value / expression within Print    
    def print_tree(self, indent):
        print(" " * indent + "Print")
        self.expression.print_tree(indent + 4)
    # we call the value of the Print expression to print    
    def execute(self):
        print(self.expression.execute())

class Number():
    # if Number(5), then self.value = 5
    def __init__(self, value):
        self.value = value
    # in the visual tree we indent further and display "Number: " followed by its value, say "Number: 5"    
    def print_tree(self, indent):
        print(" " * indent + f"Number: {self.value}")
    # We just simply return the value     
    def execute(self):
        return self.value
        
class Program():
    # a program is made of statements
    def __init__(self):
        self.statements = []
    # way to visually see our Program    
    def print_tree(self):
        print("Program")
        for statement in self.statements:
            statement.print_tree(4) # for indentation purposes
    # we execute every statement in the program        
    def execute(self):
        for statement in self.statements:
            statement.execute()

def abstract_tree(instructions, tokens):
    tree = Program()
    # probably will become a while or for loop when we bring in addition for example
    if instructions[0] == "PRINT":
        if instructions[1] == "NUMBER":
            number = int(tokens[1])
            value = Number(number)
            tree.statements.append(Print(value))
        else:
            print("Error, expected number")
    else:
        print("Error, expected print")
    return tree

def main():
    file = open("print_5.ezzylan", "r")
    ezzylan_test = file.read()
    file.close()
    
    key_words = {
        "Print": "PRINT",
        ".": "END",
        " ": "SPACE",
        "+": "ADD"
    }
    
    lines = ezzylan_test.split("\n")
    for line in lines:
        tokens = tokenizer(line)
        print(tokens)
        instructions = convert(tokens, key_words)
        print(instructions)
        tree = abstract_tree(instructions, tokens)
        tree.print_tree()
        tree.execute()

if __name__ == "__main__":
    main()  