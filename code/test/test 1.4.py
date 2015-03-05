def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            out = out + s2
            return out
        if s2 == '':
            out=out+s1
            return out
        else:
            out = out +s1[0]+s2[0]
            s1=s1[1:]
            s2=s2[1:]
    return helpLaceStrings(s1, s2, '')








