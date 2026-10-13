# Remove Brackets from an Algebraic

def remove_bracket(str):
    res = ""

    for i in str:
        if i not in "()[]{}":
            res+=i

    print(f"Result of without bracket : {res}")

str = input("Enter the string : ")
remove_bracket(str)