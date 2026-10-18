'''Find the Largest Word in a String
Input: Google Doc
Output: Google  '''


def find_largest_word(str1):

    words = str1.split()

    if not words:
        return ""
    
    largest_word = words[0]

    for i in words:
        if len(i) > len(largest_word):
            largest_word = i
    print(largest_word)


str1 = input("Enter the string : ")
find_largest_word(str1)
