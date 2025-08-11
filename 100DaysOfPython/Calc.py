def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def division(n1, n2):
    if n2 == 0:
        return "Error, cant divide by 0!"
    else:
        return n1 / n2
math = {"+": add,
         "-": subtract,
        "/": division,
        "*": multiply,
        }
while True:
    num1 = float(input("What is the first number? "))
    for operator in math:
        print(operator)
    op = str(input("Select operator "))
    num2 = float(input("Whats the second number? "))


    if op in math:
        running_total = math[op](num1, num2)
    else:
        print("Error, invalid operator")
        continue

    if running_total == "Error, cant divide by 0!":
        print("Error, cant divide by 0!")
    else:
        print(f"{num1} {op} {num2} = {running_total}")
    while True:
        more = input("'Y' to continue calculating or 'N' to start a new calculation ").lower()
        if more == "y":
            old_total = running_total
            new_op = str(input("Select operator "))
            new_num = float(input("select number "))
            new_value = math[new_op](running_total, new_num)
            if new_value == "Error, cant divide by 0!":
                print("Error, cant divide by 0!")
            else:
                running_total = new_value
                print(f"{old_total} {new_op} {new_num} = {new_value}")
        elif more == "n":
            break

        else:
            print("Wrong input, please type 'Y' or 'N' ")