import random
import os
data = [
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 198,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 225,
        'description': 'Actor, Former Wrestler',
        'country': 'USA'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 170,
        'description': 'Singer, Actress',
        'country': 'USA'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 175,
        'description': 'Businesswoman, Media Personality',
        'country': 'USA'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 165,
        'description': 'Media Personality, Businesswoman',
        'country': 'USA'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 190,
        'description': 'Singer, Actress',
        'country': 'USA'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 160,
        'description': 'Singer, Actress',
        'country': 'USA'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 150,
        'description': 'Singer',
        'country': 'Canada'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 140,
        'description': 'Singer, Songwriter',
        'country': 'USA'
    },
    {
        'name': 'LeBron James',
        'follower_count': 125,
        'description': 'Basketball Player',
        'country': 'USA'
    },
    {
        'name': 'Neymar Jr.',
        'follower_count': 170,
        'description': 'Footballer',
        'country': 'Brazil'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 110,
        'description': 'Model, Media Personality',
        'country': 'USA'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 105,
        'description': 'Singer, Songwriter',
        'country': 'USA'
    },
    {
        'name': 'Zendaya',
        'follower_count': 115,
        'description': 'Actress, Singer',
        'country': 'USA'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 135,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Shakira',
        'follower_count': 100,
        'description': 'Singer, Songwriter',
        'country': 'Colombia'
    },
    {
        'name': 'David Beckham',
        'follower_count': 75,
        'description': 'Former Footballer',
        'country': 'UK'
    },
    {
        'name': 'Rihanna',
        'follower_count': 120,
        'description': 'Singer, Businesswoman',
        'country': 'Barbados'
    },
    {
        'name': 'Gigi Hadid',
        'follower_count': 85,
        'description': 'Model',
        'country': 'USA'
    }
]

start_logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/ 
"""
logo_vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

counter_wins = 0
keep_playing = True

compare_a = random.choice(data)
compare_b = random.choice(data)
while compare_a == compare_b:
    compare_b = random.choice(data)

def print_exit_screen(count):
        os.system('clear')
        print(start_logo)
        print("Sorry you lost :(")
        print(f"Total Score: {count}")  


while keep_playing == True:
    os.system('clear')
    print(start_logo)
    print(f"Current Score: {counter_wins}")
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
    print(logo_vs)
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")
    selection = input(("Who has more followers? Type 'A' or 'B': ")).lower()
    if selection == 'a':
        if compare_a['follower_count'] > compare_b['follower_count']:
            counter_wins += 1
            keep_playing = True
            compare_b = random.choice(data)
            while compare_a == compare_b:
                compare_b = random.choice(data)
        else:
            keep_playing = False
    elif selection == 'b':
        if compare_a['follower_count'] < compare_b['follower_count']:
            counter_wins += 1
            keep_playing = True
            compare_a = compare_b
            compare_b = random.choice(data)
            while compare_a == compare_b:
                compare_a = random.choice(data)
        else:
            keep_playing = False

    if keep_playing == False:
        print_exit_screen(counter_wins)


