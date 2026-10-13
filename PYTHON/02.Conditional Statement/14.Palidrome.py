# WAP to check wheather a given string is palidrome or not

str =input("Enter your string:")

reverseStr=str[::-1]

if str==reverseStr:
    print(f"{str} is a palidrome string")

else:
    print(f"{str} is not palidrome string")