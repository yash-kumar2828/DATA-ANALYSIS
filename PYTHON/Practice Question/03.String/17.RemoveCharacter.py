'''Question 17 — Remove Characters from First String Present in Second
Input: abcdef, cefz
Output: abd    '''

def get_remove_character(str1,str2):

    set_s2 = set(str2)

    res = []

    for i in str1:

        if i not in set_s2:
            res.append(i)

    output = ''.join(res)
    print(output)


str1 = input("Enter the first string : ")
str2 = input("Enter the second string : ")
get_remove_character(str1,str2)
