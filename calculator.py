# import pyfiglet to change font color and style

import pyfiglet

# Display Operation Menu
print(pyfiglet.figlet_format("Simple Mini Calculator".center(50), font = "digital"))
print("To choose your desire operation: ")
print("\033[31mPress 1 \033[0m: Addition", " " * 35, "\033[32mPress 2 \033[0m: Subtraction \n"
      "\033[33mPress 3 \033[0m: Multiplication ", " " * 28, "\033[34mPress 4 \033[0m: Division")
print ("=" * 90)

def calculator():
    while True:
        try:
# Ask the user for operation
            mode = int(input("Enter Operation: "))

        # Present
        except ValueError:
            print("ERROR! The number that you input is invalid")
            print()
# Press 1 for addition
    # Enter number
    # Enter second number
    # print result
# Press 2 for subtraction
    # Enter number
    # Enter second number
    # print result
# Press 3 for multiplication
    # Enter number
    # Enter second number
    # print result
# Press 4 for divison
    # Enter number
    # Enter second number
    # print result
    # If user input 0 in second number
# start
calculator()
# Ask the user to continue or stop the program
# If n
    # Stop the program
# if y
    # Back to the first part



