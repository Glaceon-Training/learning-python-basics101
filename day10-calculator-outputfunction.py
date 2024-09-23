import calculator_art
print(calculator_art.logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num_1 = float(input("What's the first number?: "))
    result = 0
    should_continue = True

    while should_continue:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        num_2 = float(input("What's the next number?: "))

        if operation == "+":
            result = operator["+"](num_1, num_2)
            print(f"{num_1} + {num_2} = {result}")
        elif operation == "-":
            result = operator["-"](num_1, num_2)
            print(f"{num_1} - {num_2} = {result}")
        elif operation == "*":
            result = operator["*"](num_1, num_2)
            print(f"{num_1} * {num_2} = {result}")
        elif operation == "/":
            result = operator["/"](num_1, num_2)
            print(f"{num_1} / {num_2} = {result}")
        else:
            print("Invalid input.")

        ask_continue = input(f"Type 'y' to continue calculating with {result},"
                             f"or type 'n' to start a new calculation: ").lower()

        if ask_continue == "y":
            num_1 = result
        elif ask_continue == "n":
            should_continue = False
            print("\n" * 20)
            calculator()
        else:
            print("Invalid input.")
            break


calculator()
