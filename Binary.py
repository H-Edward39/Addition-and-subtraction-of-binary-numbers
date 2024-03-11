def validate_binary_number(number):
    # Check if the number is a valid binary number
    for digit in number:
        if digit != '0' and digit != '1':
            return False
    return True

def ones_complement(binary_number):
    # Compute the one's complement of a binary number
    ones_comp = ''
    for digit in binary_number:
        if digit == '0':
            ones_comp += '1'
        else:
            ones_comp += '0'
    return ones_comp

def twos_complement(binary_number):
    # Compute the two's complement of a binary number
    ones_comp = ones_complement(binary_number)
    twos_comp = bin(int(ones_comp, 2) + 1)[2:]
    twos_comp = twos_comp.zfill(len(binary_number))
    return twos_comp

def binary_addition(binary_number1, binary_number2):
    # Perform binary addition of two binary numbers
    result = bin(int(binary_number1, 2) + int(binary_number2, 2))[2:]
    result = result.zfill(max(len(binary_number1), len(binary_number2)))
    return result

def binary_subtraction(binary_number1, binary_number2):
    # Perform binary subtraction of two binary numbers
    result = bin(int(binary_number1, 2) - int(binary_number2, 2))[2:]
    result = result.zfill(max(len(binary_number1), len(binary_number2)))
    return result

def display_menu_1():
    print("** binary calculator **")
    print("A) Insert new numbers")
    print("B) Exit")

def display_menu_2():
    print("** please select the operation **")
    print("A) Compute one's complement")
    print("B) Compute two's complement")
    print("C) Addition")
    print("D) Subtraction")

def binary_calculator():
    while True:
        display_menu_1()
        choice_menu_1 = input("Select an option (A/B): ")

        if choice_menu_1 == 'A':
            number1 = input("Insert the first number: ")

            while not validate_binary_number(number1):
                print("Error: Please insert a valid binary number.")
                number1 = input("Insert the first number: ")

            display_menu_2()
            choice_menu_2 = input("Select an operation (A/B/C/D): ")

            if choice_menu_2 == 'A':
                ones_comp = ones_complement(number1)
                print("One's complement: ", ones_comp)
            elif choice_menu_2 == 'B':
                twos_comp = twos_complement(number1)
                print("Two's complement: ", twos_comp)
            elif choice_menu_2 == 'C':
                number2 = input("Insert the second number: ")

                while not validate_binary_number(number2):
                    print("Error: Please insert a valid binary number.")
                    number2 = input("Insert the second number: ")

                result = binary_addition(number1, number2)
                print("Addition result: ", result)
            elif choice_menu_2 == 'D':
                number2 = input("Insert the second number: ")

                while not validate_binary_number(number2):
                    print("Error: Please insert a valid binary number.")
                    number2 = input("Insert the second number: ")

                result = binary_subtraction(number1, number2)
                print("Subtraction result: ", result)
            else:
                print("Error: Please select a valid choice.")

        elif choice_menu_1 == 'B':
            print("Exiting the program...")
            break
        else:
            print("Error: Please select a valid choice.")


# Run the binary calculator program
binary_calculator()