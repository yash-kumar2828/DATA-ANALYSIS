# Convert Octal to Decimal

def get_octal_to_decimal(octal):
    decimal = 0
    power = 0
    for i in str(octal):
        if i in '89':
            print("Please enter octal digit 0-7 ")
            return
    while octal>0:
        rem = octal%10
        decimal = decimal+rem*8**power
        power+=1
        octal//=10
    print(f"Octal to decimal is : {decimal}")

octal = int(input("Enter the octal value : "))
get_octal_to_decimal(octal)
