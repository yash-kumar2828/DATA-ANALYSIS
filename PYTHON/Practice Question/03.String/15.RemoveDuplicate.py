'''Remove All Duplicate Characters
Input: bcabc
Output: bca    '''


def get_remove_duplicate(str1):

    d = {}

    for i in str1:
        d[i] = d.get(i,0)+1

    res = ''

    for i in d:
        res = res+i

    print(f"The result is : {res}")


str1 = input("Enter the string : ")
get_remove_duplicate(str1)
