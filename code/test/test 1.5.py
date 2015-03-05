def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    y = n
    i = 0
    while (y%3 != 0) and (y>0):
        i += 1
        y = n-20*i
        #print ("the y is"+str(y)+"the i is "+str(i))
    if y<0:
        return False
    else :
        y=y/3
        #print y
        if y%2 == 0 or y%3==0:
            return True
        elif (y-3)%2 == 0:
            return True
        else:
            return False
    
