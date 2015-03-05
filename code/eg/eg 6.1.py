def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    new = ()
    n = 0

    while n < len(aTup):
        new += (aTup[n],)
        n += 2
    return new
    
