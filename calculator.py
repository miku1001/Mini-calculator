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
# Ask the user for operation
            mode = int(input("Enter Operation: ")) 
            # Press 1 for addition
            if mode == 1:
                print("You choose, ADDITION!".center(45))
                while True:
                    try:
                        # Enter number
                        first = int(input("Enter the first number: "))
                        # Enter second number
                        second = int(input("Enter the second number: "))
                        sum = first + second
                        # print result
                        print(f'The sum is {sum}')
                    # If user input non-integer character
                    except ValueError:
                        print("ERROR!, you entered invalid character!")
                        continue
                    
            # Press 2 for subtraction
            elif mode == 2:
                print("You choose, SUBTRACTION!".center(45))
                while True:
                    try:
                        # Enter number
                        first = int(input("Enter the first number: "))
                        # Enter second number
                        second = int(input("Enter the second number: "))
                        difference = first - second
                        # print result
                        print(f'The difference is {difference}')
                    # If user input 0 in second number
                    except ValueError:
                        print("ERROR!, you entered invalid character!")
                        continue

            # Press 3 for multiplication
            elif mode == 3:
                print("You choose, MULTIPLICATION!".center(45))
                while True:
                    try:
                # Enter number
                        first = int(input("Enter the first number: "))
                        # Enter second number
                        second = int(input("Enter the second number: "))
                        product = first * second
                        # print result
                        print(f'The product is {product}')
                    # If user input 0 in second number
                    except ValueError:
                        print("ERROR!, you entered invalid character!")
                        continue

            # Press 4 for divison
            elif mode == 4:
                print("You choose, DIVISION!".center(45))
                while True:
                    try:
                        # Enter first number
                        first = int(input("Enter the first number: "))
                        # Enter second number
                        second = int(input("Enter the second number: "))
                        quotient = first / second
                        # print result
                        print(f'The quotient is {quotient}')
                    # If user input 0 in second number
                    except ZeroDivisionError:
                        print("ERROR! Divided by zero")
                        continue
            else:
                print("Invalid choice")
                continue
# start
calculator()
# Ask the user to continue or stop the program
# If n
    # Stop the program
# if y
    # Back to the first part



