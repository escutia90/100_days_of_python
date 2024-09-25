import random
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|
"""
diff_settings = {
    "easy" : 10,
    "hard" : 5,
}

difficulty = "easy"
guess = 0
number_to_guess = random.randint(1, 100)

print(logo)
print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100\n")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
lives = diff_settings[difficulty]

while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number\n")
    guess = int(input("Make a guess: "))
    if guess == number_to_guess:
        print(f"You got it! The answer is {number_to_guess}")
        break
    elif guess < number_to_guess:
        lives -=1
        print("Too Low. \n")
        if(lives == 0):
            print("you lost")
            break
        print("Guess again. \n")
    elif guess > number_to_guess:
        lives -=1
        print("Too High")
        if(lives == 0):
            print("you lost")
            break
        print("Guess again. \n")
