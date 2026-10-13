# Convert Decimal to Octal

def get_decimal_to_octal(n):
    if n<0:
        print("Please enter the positive number")
        return
    octal = 0
    place = 1
    while n>0:
        rem = n%8
        octal = octal+rem*place
        place*=10
        n//=8
    print(f"Deimal to octal is : {octal}")

num = int(input("Enter the positive number : "))
get_decimal_to_octal(num)
