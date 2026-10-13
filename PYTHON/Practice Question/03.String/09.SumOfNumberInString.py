# Sum of the Numbers in a String

def sum_of_number_in_string(str):
    res = ''
    for i in str:
        if i.isdigit():
            res+=i
    print(f"Sum of number in string is : {res}")

str = input("Enter the string : ")
sum_of_number_in_string(str)