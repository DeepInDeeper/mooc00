def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    elif exp/2 == 0:
        return base*base*recurPowerNew(base,exp/2)
    else:
        return base * recurPowerNew(base,exp-1)
