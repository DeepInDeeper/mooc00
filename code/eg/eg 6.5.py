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
        
