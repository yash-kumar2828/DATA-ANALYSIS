'''Remove Duplicate Words from a String
Input: this is is a test test
Output: this is a test
'''


def remove_duplicate_word(s1):

    list_data = s1.split()

    word = []

    for i in list_data:

        if i not in word:
            word.append(i)

    output = ' '.join(word)

    print(output)


str1 = input('Enter the string : ')
remove_duplicate_word(str1)