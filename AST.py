class Program():
    def __init__(self):
        self.statements = []
    def visualize(self):
        print("Program:")
        for statement in self.statements:
            statement.visualize(4)

class PrintStatement():
    def __init__(self):
        self.expressions = []
    def visualize(self, indent):
        print(" " * indent + "Print:")
        for expression in self.expressions:
            expression.visualize(indent + 4)

class Number():
    def __init__(self, value):
        self.value = value 
    def visualize(self, indent):
        print(" " * indent + f"Number: {self.value}")

class Addition():
    def __init__(self):
        self.left_value = None
        self.right_value = None
    def visualize(self, indent):
        print(" " * indent + "Addition:")
        self.left_value.visualize(indent + 4)
        self.right_value.visualize(indent + 4)

def main():
    print("Hi")
    # how they would pop up
    program = Program()
    print_statement = PrintStatement()
    number = Number(5)
    addition = Addition()
    number_1 = Number(7)
    addition_1 = Addition()
    number_2 = Number(3)
    # then END just tells the system to end, idk if that should be its own class
    # maybe one that returns the is_valid code. Maybe useful for debugging????
    
    # how they would connect
    # once the end is reached we return number_2. At the point in the code where addition_1 is made
    # we have number_1 already passed as a parameter and the return value of number_2
    # so addition_1 adds their value and it is returned 
    addition_1.left_value = number_1
    addition_1.right_value = number_2
    
    # with addition_1 being returned as the right_value we do the same logic for addition (the first call)
    addition.left_value = number
    addition.right_value = addition_1
    
    # and then we pass that to print_statement
    print_statement.expressions.append(addition)
    
    # and we then append that to program
    program.statements.append(print_statement)
    
    # since each recursion creates its own addition expression and own number, then this should be able to repeat itself as many time as we need
    # so long as it's implemented correctly

    program.visualize()    

if __name__ == "__main__":
    main()