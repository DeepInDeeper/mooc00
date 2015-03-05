def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    n = len(aStr)
    if n ==0:
        return False
    if n == 1:
        return False
    
    elif str(char) == str(aStr[n/2]):
        return True
    elif str(char) > str(aStr[n/2]):
        return isIn(char,aStr[n/2:n])
    else :
        return isIn(char,aStr[0:n/2])
