'''Check if One String is a Rotation of Another
Input: s1 = ABCD, s2 = CDAB
Output: True'''


def check_rotation_string(s1,s2):

    if len(s1) != len(s2):
        return False

    temp = s1+s1

    if s2 in temp:
        return True
    else:
        return False


s1 = input("Enter the first string : ")
s2 = input("Enter the second string : ")

res = check_rotation_string(s1,s2)

print(res)