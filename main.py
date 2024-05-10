import random 

hangman_words = ['whizzing', 'fishhook', 'beekeeper', 'rhythm', 'stronghold']

def get_random_word():
    #Choose a random from the list
    word = random.choice(hangman_words)
    return word
#print(get_random_word())
    
def display_word(word):
    #Create a list of dashes for each letter in the word to be guessed.
    
    word_display =['_'] * len(word)
    return word_display
#print(' '.join(word_display))  #'single space' joined by the elements of word_display



