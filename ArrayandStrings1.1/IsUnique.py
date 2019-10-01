# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures? 

#Two solutions

def isUnique (entryString):
    # Simplest solution would with sets, since sets hold only unique items
    setString = set(entryString)

    if (len(entryString) == len(setString)):
        return True
    else:
        return False

def is_unique(entry_string):
    # Longer approach with two for loops and previously checked characters list
    seen = []

    for i in entry_string:
        for j in seen:
            if i == j:
                return False
        seen.append(i)
    return True


