# Find the GCD of an Array of Numbers

def get_fcd_of_array(numbers):
    res = numbers[0]
    for i in range(1,len(numbers)):
        current_number = numbers[i]
        while current_number!=0:
            rem = res%current_number
            res = current_number
            current_number = rem

    return res


l = eval(input("Enter your list : "))
res = get_fcd_of_array(l)
print(f"GCD of array is : {res}")