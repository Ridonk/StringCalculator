#!/bin/python3
# TODO: Implement string sanity checks and offer feedback to the user
# TODO: Implement variable handling
# TODO: Implement multi-step calculations and linking calculations to run

# StringCalc Description
# The math_ subset of functions allows various operations to be performed on a
# list of numbers. The functions return the calculated value and print the math
# expression to the string in a correctly formatted manner.
#
# Input is parsed as in list form and then verified to be a correct mathematical
# expression before being calculated according to the symbols it contains. If there
# are any problems with the string, then the program tells the user and starts over.


def math_add(x: list) -> int:
    y = 0
    for i in x:
        y += x[i-1]
    expression_print(x, y, "+")
    return y


def math_sub(x: list) -> int:
    y = 0
    for i in x:
        y -= x[i-1]
    expression_print(x, y, "-")
    return y


def math_div(x: list) -> int:
    y = 0
    for i in x:
        y /= x[i - 1]
    expression_print(x, y, "/")
    return y


def math_mult(x: list) -> int:
    y = 0
    for i in x:
        y *= x[i - 1]
    expression_print(x, y, "*")
    return y


def math_expo(x, y) -> int:
    if y == 0:
        return 1
    else:
        return x * math_expo(x, y - 1)


def math_modulo(x: list) -> int:
    y = 0
    for i in x:
        y %= x[i - 1]
    expression_print(x, y, "%")
    return y


def expression_print(x: list, y: int, operation: str):
    expression = ""
    for j in range(0, len(x)):
        if j > 0:
            expression += operation
        expression += str(x[j])
    expression += "=" + str(y)
    print(expression)


def main():
    print('''
    Main Menu
    
    1. Enter a string to calculate
    2. Exit
    
    ''')
    choice = int(input(">>> "))
    if choice == 1:
        choice = input("Enter an expression to calculate: \n>>> ")
        math_add(eval(choice))  # TODO: Split string and determine what math operations to perform
    elif choice == 2:
        quit(0)
    main()


print("Welcome to String Calculator!")

main()


