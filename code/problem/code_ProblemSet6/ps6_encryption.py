# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO
    
    import string
    # create a empty dictionary to store data
    dic ={}
    # through all ascii and store it in s
    s = string.ascii_lowercase + string.ascii_uppercase
    #print s
    for i in range(52):
        if (ord(s[i])>=ord('a') and ord(s[i])<=ord('z')):
            k = ord(s[i]) + shift
            if k > 122:
                k = k -26
            dic[s[i]]=chr(k)
        elif (ord(s[i])>=ord('A') and ord(s[i])<=ord('Z')):
            k = ord(s[i]) +  shift
            if k > ord('Z'):
                k = k -26
            dic[s[i]]=chr(k)
    return dic
    

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    reverse = ''
    s = text
    dic = coder
    for i in range(len(text)):
        if (ord(s[i])>=ord('a') and ord(s[i])<=ord('z')) or (ord(s[i])>=ord('A') and ord(s[i])<=ord('Z')):
            reverse = reverse + dic[s[i]]
        else:
            reverse = reverse + s[i]
    return reverse
        
        
    

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    show =applyCoder(text,buildCoder(shift))
    return show
    
#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    #Set the maximum number of real words found to 0
    max_num = 0
    #Set the best shift to 0
    for shift in range(26):
        num = 0
        # shift the words in every shift
        words=applyShift(text, shift)
        words = words.split(' ')
        #record the number of the right in every shift
        for i in range(len(words)):
            if (isWord(wordList, words[0])):
                num += 1
        # record the max number in every shift and shift
        if num > max_num:
            max_num = num
            x = shift
        # if no found ,let it return 0
        if max_num == 0:
            x = 0

    return x

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.
    text = getStoryString()
    wordList =loadWords()
    shift = findBestShift(wordList, text)
    return applyShift(text, shift)
    

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    #wordList = loadWords()
    #s = applyShift('Hello, world!', 8)
    #bestShift = findBestShift(wordList, s)
    #assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    decryptStory()
