import sys

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
    "money": 0
}

isOn = True
choice = ""

def process_request(choice):
    global machine_details
    if machine_details["coffee"] > coffe_choices[choice]["coffee"] and machine_details["milk"] > coffe_choices[choice]["milk"] and machine_details["water"] > coffe_choices[choice]["water"]:
        machine_details["coffee"] = machine_details["coffee"] - coffe_choices[choice]["coffee"]
        machine_details["milk"] = machine_details["milk"] - coffe_choices[choice]["milk"]
        machine_details["water"] = machine_details["water"] - coffe_choices[choice]["water"]
        return True
    else:
        return False

def count_coins(quarters, dimes, nickles, pennies):
    return (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

def processPayment(choice):
    money = 0
    quarters = int(input("How many quarters"))
    dimes = int(input("How many quarters"))
    nickles = int(input("How many quarters"))
    pennies = int(input("How many quarters"))
    money = count_coins(quarters, dimes, nickles, pennies)
    if money > coffe_choices[choice]["money"]:
        machine_details["money"] = machine_details["money"] + coffe_choices[choice]["money"]
        return True
    else:
        return False


def greet():
    return input("What would you like? (espresso/latte/cappuccino):")





def turn_off():
    exit()

while isOn:
    choice = greet() 
    if choice == "off":
        turn_off()
    elif choice == "report":
        print(machine_details)
    else:
        canProcess = process_request(choice)
        if canProcess == True:
            enoughMoney = processPayment(choice)
            if enoughMoney == True:
                print(f"Here is your {choice}, Enjoy!")
            else:
                print("Not enough Money, returning coins...")
        else:
            print(" Sorry, not enough ingredients to process your order")