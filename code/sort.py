def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        #print ("minIndx is"+str(minIndx)+" minVal is "+str(minVal))
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp

def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
            

def mySort(L):
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
def sort(L):
    for i in range(len(L)-1):
        for j in range (i,len(L)):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
        
        
