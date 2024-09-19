#hangman game implementation
import random
words = ['melon', 'artichoke', 'jackfruit', 'rosemary', 'millet', 'blackberry', 'broccoli', 'quinoa',  'elderberry', 'passionfruit', 'plum', 'lettuce', 'pea', 'tangerine', 'sage', 'marjoram',  'cauliflower', 'corn', 'celery', 'honey', 'gooseberry', 'sweetcorn', 'apple', 'apricot',  'garlic', 'vanilla', 'bay', 'strawberry', 'guava', 'date', 'zucchini', 'ginger', 'buckwheat',  'lentil', 'basil', 'potato', 'tomato', 'pineapple', 'oregano', 'lychee', 'eggplant', 'carrot',  'cilantro', 'watermelon', 'saffron', 'cinnamon', 'dragonfruit', 'papaya', 'asparagus', 'pear',  'banana', 'clove', 'rice', 'bean', 'cucumber', 'peach', 'maple', 'radish', 'chives', 'coconut',  'raspberry', 'oats', 'pomegranate', 'cherry', 'spelt', 'turnip', 'mango', 'sorghum', 'thyme',  'grape', 'pumpkin', 'fig', 'yam', 'tarragon', 'spinach', 'barley', 'avocado', 'parsley',  'lavender', 'mint', 'pepper', 'chickpea', 'soybean', 'lemon', 'rye', 'cabbage', 'wheat',  'kiwi', 'nectarine', 'squash', 'blueberry', 'dill', 'chocolate', 'parsnip', 'orange', 'nutmeg',  'persimmon', 'beet', 'onion', 'turmeric']

print ("Welcome to hangman!\n try to guess the following word:\n")
chosenWord = random.choice(words)
hiddenWord = ""
attempts = 5
letters_found = 0
for i in range(len(chosenWord)):
    hiddenWord += "_"

print(chosenWord)
print(hiddenWord)

while(attempts>0):
    print("----- you have " + str(attempts) +"  attempts left ------\n")
    letter = input("Enter a letter: ").lower
    pos = chosenWord.find(letter)
    chosenWord = chosenWord.replace(letter, ".",1)
    print(chosenWord)

    if(pos != -1):
        hiddenWord= hiddenWord[:pos] + letter + hiddenWord[pos+1:]
        letters_found+=1
        if(letters_found == len(chosenWord)):
            print("YOU WIN!")
            exit()
    else:
        attempts-=1    

    print(hiddenWord)

print("YOU LOST =(")
exit()
