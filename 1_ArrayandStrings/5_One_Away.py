# 1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale , pi e - > tru e
# pales , pal e - > tru e
# pale , bal e - > tru e
# pale , bak e - > fals e 

def OneEditReplace(s1, s2):
    found_difference = False
    for i in range(0, len(s1)):
        if (s1[i] != s2[i]):
            if (found_difference):
                return False
            found_difference = True
    return True

def OneEditInsert(s1, s2):
    index1 = 0
    index2 = 0
    while index2 < len(s2) and index1 < len(s1):
        if s1[index1] != s2[index2]:
            if (index1 != index2):
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

def OneAway(s1, s2):
    if len(s1) == len(s2):
        return OneEditReplace(s1, s2)
    elif (len(s1)+1) == len(s2):
        return OneEditInsert(s1, s2)
    elif (len(s1)-1) == len(s2):
        return OneEditInsert(s2, s1)
    return False

print (OneAway("pales", "paled"))