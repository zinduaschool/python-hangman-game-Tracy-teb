import random 

hangman_words = ['whizzing', 'fishhook', 'beekeeper', 'rhythm', 'stronghold']

def get_random_word():
    #Choose a random from the list
    word = random.choice(hangman_words)
    return word
print(get_random_word())
    


