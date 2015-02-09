def iterPower(base, exp):
    result = base
    if exp == 0:
        return 1
    while exp >1:
        exp -= 1
        result = result * base      
    return result
