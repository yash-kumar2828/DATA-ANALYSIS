'''Remove a Given Character from a String
Input: s1 = banana, remove = a
Output: bnn'''

def remove_character(str1, remove_char):

    res = ''
    for i in str1:
        if i is not remove_char :
            res+=i

    print(res)


str1 = input("Enter the string : ")
remove_char = input('Enter the character you want to remove it :')
remove_character(str1,remove_char)
