'''Replace Every Space with a Hyphen
Input: hello world
Output: hello-world
'''


def replace_space_with_hyphen(s1):

    res = s1.replace(' ','-')

    print(res)


s1 = input("Enter the string : ")
replace_space_with_hyphen(s1)