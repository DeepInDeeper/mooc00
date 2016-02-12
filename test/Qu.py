params1 = (8, 9)
params2 = {"a": 4, "b": 5}

def minus(a, b): 
    return a - b 

print "%d,%d" % (minus(*params1), minus(**params2))
