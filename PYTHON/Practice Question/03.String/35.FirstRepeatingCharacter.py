'''Find the First Repeating Character
Input: swiss
Output: s   '''


def first_repeating_character(s1):

    d = {}

    for i in s1:
        d[i] = d.get(i,0)+1

    for j in s1:
        if d[j]>1:
            print(j)
            return

    print("-1")


str1 = input("Enter the string : ")
first_repeating_character(str1)