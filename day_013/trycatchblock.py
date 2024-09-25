try:
    age = int(input("How old are you"))
except ValueError:
    print("invalid number, try with a numerical number")

if age > 18:
    print("You are an adult")
else:
    print("You are a kid")