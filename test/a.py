'''
verb = 1

def do_all(action):
    return {"sum": sum, "max": max, "min": min}[action]

print do_all("max")([5, 6])
'''
for i in range(3):
    print i
    break
else:
    print "end"
