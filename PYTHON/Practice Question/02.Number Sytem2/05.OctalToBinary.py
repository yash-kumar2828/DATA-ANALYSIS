# Convert Octal to Binary

def get_binary(num):
    place = 1
    binary = 0
    while num>0:
        rem = num%2
        binary = binary+rem*place
        place*=10
        num//=2
    return binary

def get_octal_to_binary(octal):
    octal_str = str(octal)
    for i in octal_str:
        if i in '89':
            print("Please enter the octal number 0-7  ")
            return

    decimal = int(octal_str,8)
    binary = get_binary(decimal)
    print(f"Octal to binary is {binary}")

octal = int(input("Enter the octal value : "))
get_octal_to_binary(octal)
