''' Remove Brackets from an Algebraic
Input: a+((b-c)+d)
Output: a+b-c+d'''


def remove_bracket(str):
    res = ""

    for i in str:
        if i not in "()[]{}":
            res+=i

    print(f"Result of without bracket : {res}")

str = input("Enter the string : ")
remove_bracket(str)