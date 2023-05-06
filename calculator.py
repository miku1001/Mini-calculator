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
            # Press 1 for addition
            if mode == 1:
                print("You choose, \033[31mADDITION\033[0m!".center(45))
                while True:
                    try:
                        # Enter number
                        first = int(input("Enter the first number: "))
                        # Enter second number
                        second = int(input("Enter the second number: "))
                        sum = first + second
                        # print result
                        print(f'\033[42mThe sum is {sum}\033[0m')
                        print()
                        choice()
                    # If user input non-integer character
                    except ValueError:
                        print()
                        print("\033[31mERROR!, you entered invalid character!\033[0m")
                        print()
                        continue
                    
            # Press 2 for subtraction
            elif mode == 2:
                print("You choose, \033[32mSUBTRACTION\033[0m!".center(45))
                while True:
                    try:
                        # Enter number
                        first = int(input("Enter the first number: "))
                        # Enter second number
                        second = int(input("Enter the second number: "))
                        difference = first - second
                        # print result
                        print(f'\033[42mThe difference is {difference}\033[0m')
                        print()
                        choice()
                    # If user input non-integer character
                    except ValueError:
                        print()
                        print("\033[31mERROR!, you entered invalid character!\033[0m")
                        print()
                        continue

            # Press 3 for multiplication
            elif mode == 3:
                print("You choose, \033[33mMULTIPLICATION\033[0m!".center(45))
                while True:
                    try:
                # Enter number
                        first = int(input("Enter the first number: "))
                        # Enter second number
                        second = int(input("Enter the second number: "))
                        product = first * second
                        # print result
                        print(f'\033[42mThe product is {product}\033[0m')
                        print()
                        choice()
                    # If user non-integer character
                    except ValueError:
                        print()
                        print("\033[31mERROR!, you entered invalid character!\033[0m")
                        print()
                        continue

            # Press 4 for divison
            elif mode == 4:
                print("You choose, \033[34mDIVISION\033[0m!".center(45))
                while True:
                    try:
                        # Enter first number
                        first = int(input("Enter the first number: "))
                        # Enter second number
                        second = int(input("Enter the second number: "))
                        quotient = first / second
                        # print result
                        print(f'\033[42mThe quotient is {quotient}\033[0m')
                        print()
                        choice()
                    # If user input 0 in second number
                    except ZeroDivisionError:
                        print()
                        print("\033[31mERROR! Divided by zero\033[0m")
                        print()
                        continue
                    # If user non-integer character
                    except ValueError:
                        print()
                        print("\033[31mERROR!, you entered invalid character!\033[0m")
                        print()
                        continue
            else:
                print()
                print("\033[31mInvalid choice\033[0m")
                print()
                continue
        except ValueError:
            print()
            print("\033[31mERROR!, you entered invalid character!\033[0m")
            print()
            continue

# Ask the user to continue or stop the program
def choice():
    while True:
        choose = input("Type \033[32mY\033[0m if yes or \033[31mN\033[0m if no: ")
        # If n
        if choose.lower() == 'n':
            # Stop the program
            print("Closing Program... Thank you! \U0001F64B")
            quit()
        # If y
        elif choose.lower() == 'y':
            # Back to the first part
            calculator()
            print()
        # If invalid character
        else:
            print()
            print("\033[31mInvalid character!\033[0m")
            print()
            continue

# start
calculator()
choice()
