'''Sort Characters in a String
Input: zxcbg
Output: bcgxz   '''


def get_sort_character(str1):

    list1 = sorted(str1)

    res = ''.join(list1)

    print(res)



str1 = input("Enter the string : ")
get_sort_character(str1)