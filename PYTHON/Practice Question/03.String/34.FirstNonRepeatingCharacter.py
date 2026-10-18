'''Find the First Non-Repeating Character
Input: swiss
Output: w
'''


def first_non_repeating(s1):

    d = {}

    for i in s1:
        d[i] = d.get(i,0)+1


    for j in s1:
        if d[j] == 1:
            print(j)
            return

    print("-1")


str1 = input("Enter the string : ")
first_non_repeating(str1)