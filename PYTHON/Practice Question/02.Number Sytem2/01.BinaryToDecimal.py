# Convert Binary to Decimal
 
def get_binary_decimal(binary):
    decimal = 0
    power = 0 
    for i in str(binary):
        if i in '23456789':
            print("Please enter the only binary digit")
            return

    while binary>0:
        rem = binary%10
        decimal = decimal+rem*2**power
        power+=1
        binary//=10

    print(f"Binary to decimal is : {decimal}")

binary = int(input("Enter the binary digit : "))
get_binary_decimal(binary)

