def tokenizer(ezzylan):
    i = 0
    tokens = []
    token = ""
    space_before = False
    period_before = False
    plus_before = False
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
                period_before = True
            tokens.append(".")
            token = ""
        # will incorporate back into the code after this version
        # elif character == "+":
        #     if plus_before == False:
        #         if not token == "":
        #             tokens.append(token)
        #         plus_before = True
        #     tokens.append("+")
        #     token = ""
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
        else:
            # turns anything that hasn't been accounted for into errors.
            # this will temporarily include + signs for example
            instructions.append("ERROR")
    return instructions

class PrintObject:
    def __init__(self):
        # for the print statement to work, self.printing must remain true
        # self.value must not be empty, and self.end must be True
        self.printing = True
        self.value = None
        self.end = None
    # this might need to become a general function when it comes to other types of statements
    def printing_error(self):
            print("Error in the print statement!")
            self.printing = False
    def add_value(self, value):
        # first time
        if self.value == None:
            self.value = value
        # plan is only situations like "Print 5 10." don't result in 10 being printed
        else:
            self.printing_error()
    def ending(self):
        # checks for situations like ".." or ".5."
        # will (currently) only set self.end to True if there is only one period
        if self.end == None:
            self.end = True
        elif self.end == True:
            self.end = False
            self.printing_error()
              
def execute(instructions, tokens):
    if not instructions:
        return
    # tokens and instructions should be perfectly aligned such that we can grab the number value
    # from tokens if it appears as a "NUMBER" instruction
    i = 0
    if instructions[i] == "PRINT":
        i += 1
        printing = PrintObject()
        # will stop if we end up with an error
        while i < len(instructions) and printing.printing == True:
            if instructions[i] == "NUMBER":
                value = tokens[i]
                printing.add_value(value)
            if instructions[i] == "END":
                printing.ending()
            # for now multiple spaces will not affect the running of the code
            if instructions[i] == "SPACE":
                pass
            if instructions[i] == "ERROR":
                printing.printing_error()
            i += 1
        if printing.printing == True:
            print(printing.value)
    else:
        # if multiple lines of logic can exist in one line, this will need to change
        # ['SPACE', 'PRINT',...] is currently an error 
        print("Error! Invalid line of code!")
             
    
def main():
    file = open("print_5.ezzylan", "r")
    ezzylan_test = file.read()
    file.close()
    
    key_words = {
        "Print": "PRINT",
        ".": "END",
        " ": "SPACE",
        # "+": "ADD"
    }
    
    lines = ezzylan_test.split("\n")
    for line in lines:
        tokens = tokenizer(line)
        print(tokens)
        instructions = convert(tokens, key_words)
        print(instructions)
        execute(instructions, tokens)


        

if __name__ == "__main__":
    main()