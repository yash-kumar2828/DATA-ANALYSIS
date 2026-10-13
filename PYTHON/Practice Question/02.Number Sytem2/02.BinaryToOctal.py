# Convert Binary to Octal

def get_binary_to_octal(binary):
    binary_str = str(binary)
    for i in binary_str:
        if i in '23456789':
            print("Please enter the only binary digit")
            return
    decimal_value = int(binary_str,2)
    octal = oct(decimal_value)
    print(f"Octal value is : {octal[2:]}")


binary = int(input("Enter the binary digit : "))
get_binary_to_octal(binary)