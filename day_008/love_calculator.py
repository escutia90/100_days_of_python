#You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

#1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

#2. Then check for the number of times the letters in the word LOVE occurs.   

#3. Then combine these numbers to make a 2 digit number and print it out. 

#def calculate_love_score(name1, name2):

def calculate_love_score(name1, name2):

    first_letter_count_name1=0
    first_letter_ccount_name2=0
    second_letter_count_name1=0
    second_letter_ccount_name2=0
    for letter in "true":
        first_letter_count_name1 += name1.count(letter)
        first_letter_ccount_name2 += name2.count(letter)
    for letter in "love":
        second_letter_count_name1 += name1.count(letter)
        second_letter_ccount_name2 += name2.count(letter)
    print(f"{first_letter_count_name1 + first_letter_ccount_name2}{second_letter_count_name1 + second_letter_ccount_name2}")
