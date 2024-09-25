

def add(a, b):
    return a + b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def sub(a, b):
    return a - b

operations = {
    "+" : add,
    "*" : mul,
    "/" : div,
    "-" : sub,
}

def calculate(op, a, b):
    return operations[op](a,b)


result= 0
isnew = "n"

while True:
    if isnew == "n":
        result = 0
        firstNum = int(input("First number: "))
        op = input("Operation (* / - +): ")
        secNum = int(input("Second number: "))
        result = calculate(op, firstNum, secNum)
        print(f"{firstNum} {op} {secNum} = {result}")

    elif isnew == "y":
        addNum = int(input("New Number number: "))
        op = input("Operation (* / - +): ")
        oldRes = result
        result = calculate(op, result, addNum)
        print(f"{oldRes} {op} {addNum} = {result}")
    isnew = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")


