''' Remove Spaces from a String
Input: take U forward
Output: takeUforward'''

def remove_space(str):
    res = ""
    for i in str:
        if i not in ' ':
            res+=i

    print(f"Print string without vowel : {res}")

str = input("Enter your string : ")
remove_space(str)