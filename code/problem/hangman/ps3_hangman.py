# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    add = True
    for i in range(len(secretWord)):
        add &= secretWord[i] in lettersGuessed
    return add



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    new_string = ''
    
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            letter = secretWord[i]
            new_string = new_string + letter
        else:
            new_string = new_string + ' _'
    return new_string



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    length = len(lettersGuessed)
    import string
    y = string.ascii_lowercase
    
    for i in range(length):
         y = string.replace(y,lettersGuessed[i],'',1)
        
    return y
        
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    chance = 8
    lettersGuessed = ''
    restore = ''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is "+str(len(secretWord))+" letters long."
    
    while chance != 0 and not(isWordGuessed(secretWord, restore)) :
        
        print "-------------"
        print "You have "+str(chance)+" guesses left."
        restore_history = restore
        #print str(restore)
        y = getAvailableLetters(restore)
        print "Available letters: "+str(y)
        lettersGuessed = str(raw_input("Please guess a letter: "))
        lettersGuessed = lettersGuessed.lower()
        length = len(lettersGuessed)
        restore = lettersGuessed + restore_history
        #print str(restore)
        if length != 1:
            print ("please enter a letter!!!")
            restore = restore_history
        elif ord(lettersGuessed) < ord('a') or ord(lettersGuessed) > ord('z'):
            print("Please enter the characters rather than the other")
        elif lettersGuessed in restore_history:
            print "Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord, restore_history))
        elif lettersGuessed in secretWord:
            print "Good guess: "+str(getGuessedWord(secretWord, restore))
            
        else :
            print "Oops! That letter is not in my word: "+str(getGuessedWord(secretWord, restore))
            chance -= 1
            
    if chance == 0:
        print "-----------"
        print "Sorry, you ran out of guesses. The word was "+str(secretWord)+"."
    else:
        print "------------"
        print "Congratulations, you won!"
        
        
    
    return None






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
