# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

# Resolving by creating two lists that maintain counters of ascii based positions in the list
 
def isPermuation(string1, string2):
    string1= string1.lower()
    string2= string2.lower()
    if (len(string1)!=len(string2)):
        return False
    
    string1counter = [0]*200

    for c in string1:
        string1counter[ord(c)]= string1counter[ord(c)]+1

    string2counter = [0]*200

    for c in string2:
        string2counter[ord(c)]= string2counter[ord(c)]+1    

    return string1counter==string2counter

print isPermuation("test", "Test")