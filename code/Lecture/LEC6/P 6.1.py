def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    sum = 0
    x = start
    j = 0
    while x <(stop-step):
        x = start+j*step
        j += 1
        sum += f(x)*step
    return sum
