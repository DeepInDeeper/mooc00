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


