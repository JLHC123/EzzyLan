file = open("Luigi.ezzylan", "r")
ezzylan = file.read()
file.close()

code_end = False
# print(ezzylan)
is_print = ezzylan[0:6]
if is_print == "Print ":
    ezzylan = ezzylan[6:]
    # print(ezzylan)
    if ezzylan.startswith("\""):
        ezzylan = ezzylan[1:]
        # print(ezzylan)
        check_close_quote = ezzylan.find("\"")
        # print(check_close_quote)
        if check_close_quote >= 0:
            string = ezzylan[0:check_close_quote]
            # print(string)
            ezzylan = ezzylan[check_close_quote + 1:]
            # print(ezzylan)
            if ezzylan[0] == ".":
                code_end = True
        else:
            print("No end quote")
    else:
        print("No string")
else:
    print("Invalid")

if code_end:
    print(string)
else:
    print("Code not end")