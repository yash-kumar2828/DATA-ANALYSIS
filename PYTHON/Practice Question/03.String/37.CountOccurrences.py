'''Count Occurrences of a Substring
Input: s1 = aaaa, occur = aa
Output: 2
'''

def count_occurrences(str1,occur):

    res = str1.count(occur)

    print(res)


str1 = input("Enter the string : ")
occur = input("Enter the character you want to count the occurrences : ")

count_occurrences(str1,occur)