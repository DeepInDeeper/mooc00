s = 'zyxwvutsrqponmlkjihgfedcba' 
j = 0
k = 0
m = 0

for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        j += 1
        if j > k:
            k = j
            m = i            
    else:
        j = 0
print "Longest substring in alphabetical order is: "+str(s[m-k+1:m+2])
