def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False


def search2(L, e):
    for i in L:
        if i == e:
            return True
        elif i > e:
            return False
    return False

def search3(L, e):
    # Test if the list is empty - if it is, e cannot be in it!
    # Run this test first - so that we don't throw an error trying
    #  to access L[0].
    if L == []:
        return False

    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)
