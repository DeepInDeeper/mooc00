varA=int(raw_input ('varA: '))
varB=int(raw_input ('varB: '))
if type(varA)==str or type(varB)==str:
    print ("string involved")
elif varA>=varB:
    if varA==varB:
        print ("equal")
    else:
        print ("bigger")
else:
    print ("smaller")
