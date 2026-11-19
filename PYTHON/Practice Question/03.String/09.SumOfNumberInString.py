'''Sum of the Numbers in a String
Input: 123xyz
Output: 123  '''

def sum_of_number_in_string(str):
    res = 0
    num = ''
    for i in str:
        if i.isdigit():
            num+=i

        else:
            if num:
                res = res+int(num)
                num = ''
    if num :
        res =res + int(num)
    print(f"Sum of number in string is : {res}")

str = input("Enter the string : ")
sum_of_number_in_string(str)