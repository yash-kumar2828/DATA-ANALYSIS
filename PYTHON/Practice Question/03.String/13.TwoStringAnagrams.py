''' Check if Two Strings are Anagrams
Input: CAT, ACT
Output: true'''



def get_two_string_anagrams(str1,str2):

    if sorted(str1) == sorted(str2):
        return True

    else:
        return False


str1 = input("Enter the first string : ")
str2 = input("Enter the second string : ")

print(get_two_string_anagrams(str1,str2))

