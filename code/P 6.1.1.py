def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    sum = 0
    i=int((stop-start)/step)
    for j in range(i):
        x=start+j*step
        sum += f(x)*step
    return sum

