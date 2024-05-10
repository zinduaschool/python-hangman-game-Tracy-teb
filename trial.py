import random 

hangman_words = ['whizzing', 'fishhook', 'beekeeper', 'rhythm', 'stronghold']

#def get_random_word():
    #Choose a random from the list
word = random.choice(hangman_words)
   # return word
#print(word)

#def display_word(word):
    #Create a list of dashes for each letter in the word to be guessed.
    
word_display =['_'] * len(word)
print(' '.join(word_display))  #'single space' joined by the elements of word_display

