# 'switch' case in Python
# As there is no direct support of 'switch' in python, it can be achieved in
# several ways.

# Program demonstrated below is one of the easy ways. It uses the if-else
# ladder for switching. 

# Dummy function_one
def function_one():
    print("You called Function One")

# Dummy function_two
def function_two():
    print("You called Function Two")

# Defining the switch case equivalent in an infinite while loop,
# until the user decides to break
def main():
    while True:
        print("Menu")
        print("--------------")
        print("1-Function_one\n2-Function_two\n3-Exit")
        print("--------------")
        print("Enter your choice\n")
        choice = input()
        
        if choice == '1':
            function_one()
        elif choice == '2':
            function_two()
        else:
            print("Program Terminates")
            break

# Call the main()
main()
