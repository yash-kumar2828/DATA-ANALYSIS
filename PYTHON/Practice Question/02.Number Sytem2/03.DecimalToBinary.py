# Convert Decimal to Binary

def get_decimal_to_binary(n):
    place = 1
    binary = 0
    if n<0:
        print("please enter the positive number")
        return
    while n>0:
        rem = n%2
        binary = binary+rem*place
        place*=10
        n//=2
    print(f"Decimal to binary is : {binary}")

num = int(input("Enter a positive number : "))
get_decimal_to_binary(num)


