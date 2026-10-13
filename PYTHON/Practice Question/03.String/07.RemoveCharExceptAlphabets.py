# Remove Characters Except Alphabets

def remove_char_except_alpha(str):
    res = ""

    for i in str:
        if i.isalpha():
            res+=i
    print(res)

str = input("Enter your string : ")
remove_char_except_alpha(str)