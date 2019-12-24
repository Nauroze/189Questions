# 1.6 String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3, If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z). 

def compressString(my_str):
    new_str = ""
    count = 0
    previous_letter = ''
    letter_changed = False
    first_time = True

    for letter in my_str:
        letter_changed = False
        if (letter != previous_letter and first_time != True):
            letter_changed = True 

        if (letter_changed):
            new_str = new_str + previous_letter
            new_str = new_str + str(count)
            count = 0

        count += 1
        
        previous_letter = letter
        first_time = False

    new_str = new_str + previous_letter
    new_str = new_str + str(count)
    return new_str

print (compressString("aabbbcccdee"))