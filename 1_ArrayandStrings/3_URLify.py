# 1.3 Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. 

def URLify(givenstring):
    stringlist = list(givenstring)
    for x in range(len(stringlist)):
        if stringlist[x] == " ":
            stringlist[x] = "%20"

    givenstring = ''.join(stringlist)
    print (givenstring)

URLify("Dont go breaking my heart")