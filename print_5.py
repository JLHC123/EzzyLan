file = open("print_5.ezzylan", "r")
ezzylan = file.read()
file.close()

i = 0
tokens = []
token = ""

while i < len(ezzylan):
    print(ezzylan[i])  
    i += 1  
        
print(token)