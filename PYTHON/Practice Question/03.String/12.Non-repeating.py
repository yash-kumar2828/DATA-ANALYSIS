''' Find Non-Repeating Characters
Input: google
Output: l e'''



def get_non_repeating(str1):

    d = {}

    for i in str1:
        d[i] = d.get(i,0)+1

    res = ""

    for i in d:

        if d[i] == 1:
            res = res + i + " "

    print(res.strip())


str1 = input('Enter the string : ')
get_non_repeating(str1)