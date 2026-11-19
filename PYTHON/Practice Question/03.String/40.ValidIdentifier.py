'''Check if a String is a Valid Identifier
Input: student_name
Output: Valid  '''



def check_identifier(s1):

    if s1.isidentifier():
        print("valid")

    else: 
        print("Invalid")


def check_identifier_without_built_in(s1):
    if len(s1) == 0:
        print("Invalid")
        return

    firstChar = s1[0]
    if not(('a'<=firstChar<='z') or ('A'<=firstChar<='Z') or (firstChar == '_')):
        print("Invalid")
        return

    for i in s1:
        if not(('a'<=i<='z') or ('A'<=i<='Z') or ('0'<=i<='9') or (i == '_')):
            print("Invalid")
            return

    print("Valid")

s1 = input("Enter the vaiable name : ")
check_identifier(s1)
check_identifier_without_built_in(s1)
