# -*- coding: cp936 -*-
from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
   
        
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    score_max = 0
    # Create a new variable to store the best word seen so far (initially None)
    get_word=''
    
    for i in range(len(wordList)):
        word = wordList[i]
    # For each word in the wordList
        if (isValidWord(word, hand, wordList)):
            score = getWordScore(word, n)
            if score > score_max:
                score_max = score
                get_word = word
                #print "the word is "+str(get_word)
                #print "the score is "+str(score_max)
            i += 1
        else:
            i += 1
    if get_word == '':
        return None
    else:
        return get_word
        
            
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth
            
            # If the score for that word is higher than your best score
            
                #Update your best score, and best word accordingly      

    # return the best word you found.
    #return word
    


#
#Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    result_a = 0
    result = 0
    hand_copy = hand.copy()
    words = ' '
    while words != str('') and calculateHandlen(hand_copy) :
        print ("Current Hand:"),
        displayHand(hand_copy)
        words=compChooseWord(hand_copy, wordList, n)
        result_a = getWordScore(words, n)
        result = result_a +result 
        if words != str('') and calculateHandlen(hand_copy):
            print(str('"')+str(words)+str('"')+" earned "+str(result_a)+" points. Total: "+str(result)+" points")
        hand_copy = updateHand(hand_copy,words)
        if calculateHandlen(hand_copy) and words != str(''):
            print ("")
        #print str(hand_copy)
    print "Total score: "+str(result)+" points."
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    HAND_SIZE = 15
    Enter = ''
    mem_Enter = ''
    Enters = ''
    while Enter != str('e'):
        Enter = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if (Enter != str('e') and (Enter ==str('r') or Enter == str('n'))):
            print ("")
        
        mem_Enter = mem_Enter + Enter
        if Enter != str('r') and Enter != str('n') and Enter !=str('e'):
            print "Invalid command."
            print ""
        if Enter == str('r') and mem_Enter.count('n') == 0 :
            print "You have not played a hand yet. Please play a new hand first!"
            print ""
        while (Enters != str ('c') and Enters != str('u') and ((Enter == str('r')and mem_Enter.count('n')) or Enter == str('n'))):
            Enters = raw_input("Enter u to have yourself play, c to have the computer play: ")
            if (Enters == str('c') or Enters == str('u')):
                print ""
            # computer plays it 
            if Enters == str("c") and Enter == str('n'):
                hand =dealHand(HAND_SIZE) 
                compPlayHand(hand, wordList, HAND_SIZE)
                print ""
            if Enters == str("c") and Enter == str('r') and mem_Enter.count('n') > 0 :
                compPlayHand(hand, wordList, HAND_SIZE)
                print ""
            # men plays it    
            if Enters == str("u") and Enter == str('n') :
                hand =dealHand(HAND_SIZE)
                playHand(hand, wordList, HAND_SIZE)
                print ""
            if Enters == str("u") and Enter == str('r') and mem_Enter.count('n') > 0 :
                playHand(hand, wordList, HAND_SIZE)
                print ""
            if Enters  != str ('c') and Enters != str('u'):
                print "Invalid command."
                print ""
           
        Enters = ''
    

        
        
    
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


