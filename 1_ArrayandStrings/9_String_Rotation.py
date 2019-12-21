
#1.9 String Rotation: Assume you have a method isSubstring which checks if one word 
# is a substring of another. Given two strings, s1 and s2, 
# write code to check if s2 is a rotation of s1 using only one call to isSubstring 
# (e.g "waterbottle" is a rotation of "erbottlewat")

def isSubstring(s1, s2):
    return s2 in s1

def isRotation(s1, s2):
    length = len(s1)
    if (length == len(s2)) and (length > 0):
        s1s1 = s1 + s1
        return isSubstring(s1s1, s2)
    return False

print isRotation("waterbottle", "erbottlewat")