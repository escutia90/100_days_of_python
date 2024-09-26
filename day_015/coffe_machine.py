coffe_choices = {
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 25,
        "money": 2.5
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 25,
        "money": 2.5
    },
    "capuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 25,
        "money": 3
    },
    "espresso": {
        "water": 150,
        "milk": 0,
        "coffee": 50,
        "money": 2
    },
}

machine_details = {
    "water": 10000,
    "milk": 5000,
    "coffee": 1000,
    "money": {
        "quarters": 100,
        "dimes": 100,
        "nickles" : 50,
        "pennies": 50
    }
}

isOn = True
choice = ""

def greet():
    return input("What would you like? (espresso/latte/cappuccino):")

def count_coins(quarters, dimes, nickles, pennies):
    return (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)



def turn_off():
    exit()

while isOn:
    choice = greet() 
    if choice == "off":
        turn_off()
    else:
