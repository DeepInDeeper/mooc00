def gcdRecur(a, b):

    n= max(a,b)
    m= min(a,b)
    
    if a == 0:
        return b
    else:
        r = n%m
        a = r
        b = m
    return gcdRecur(a,b)
    
