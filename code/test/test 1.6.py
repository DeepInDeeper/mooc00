def judge_word (getword):
    value = True
    hand_copy = hand.copy()
    get_word = wordList[j]
    for i in range(len(get_word)):
        value = value and (get_word[i] in hand_copy)
        if value == False:
            return False
            hand_copy[get_word[i]] =hand_copy[get_word[i]]-1
            if hand_copy[get_word[i]] < 0:
                return False
            if (get_word in wordList):
                return True
            else:
                return False
if lo(get_word):
    print "right"
else:
    print "error"
