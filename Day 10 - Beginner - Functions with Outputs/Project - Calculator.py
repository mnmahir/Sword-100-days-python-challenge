from art import logo

print(logo)


# Calculator
# Add
def add(n1, n2):
    return n1 + n2


# Substract
def substract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


continue_calculator = True
while continue_calculator:
    operations = {"+": add, "-": substract, "*": multiply, "/": divide}
    num1 = float(input("What's the first number?: "))
    for sym in operations:
        print(sym)
    continue_operation = True

    while continue_operation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        # calculation_function = operations[operation_symbol]
        # answer = calculation_function(num1, num2)
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        opt = input(
            f"Type 'y' to continue with {answer}, or type 'r' to start a new calculation or type 'q' to quit: "
        )
        if opt == "y":
            num1 = answer
        elif opt == "r":
            continue_operation = False
        else:
            continue_operation = False
            continue_calculator = False
