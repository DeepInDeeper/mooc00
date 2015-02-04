print ("Please think of a number between 0 to 100!")

lo=0
hi=100
guessed = False

while not guessed:
    ans =(lo+hi)/2
    print ("Is your secret number "+ str(ans)+"?")
    usr_choose = raw_input ("Enter 'h' to indicate the guess is too high.Enter 'l' to indicate the guess is too low.Enter 'c' to indicate the guess is correct")
    
    if usr_choose == 'c':
        guessed = True
    elif usr_choose == 'h':
        hi = ans
    elif usr_choose == 'l':
        lo = ans
    else:
        print ("No answer.")
print ("Your secret answer is :" +str(ans))
    
