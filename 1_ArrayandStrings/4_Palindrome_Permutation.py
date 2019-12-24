# 1.4 Given a string, write a function to check if it is a permutation of a palindrome. 
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.


# if there are at lease two odd numbers, then it is not a palindrome permutation
# it can only be a palindrome permutation with 1 or less odd numbers
def isAtleastTwoOdds(array):
    oddcount = 0
    for i in array:
        if (i%2 != 0):
            oddcount += 1

        if (oddcount > 1):
            return True
    
    return False

def isPalindromePermutation(string):
    string = string.lower()
    letters = [0]*200

    for c in string:
        if (c != " "):
            letters[ord(c)] += 1

    if (isAtleastTwoOdds(letters)):
        return False
    else:
        return True
