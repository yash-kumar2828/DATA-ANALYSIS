# Find the Sum of an Arithmetic Progression (AP)

def get_arithmetic_progression(first_term, difference, number_of_term):
    sum = 0
    for i in range(1,number_of_term+1):
        sum+=first_term
        first_term+=difference
    return sum

first_term = int(input("Enter your first term : "))
differnce = int(input("Enter your difference : "))
number_of_term = int(input("Enter your number of term : "))

res = get_arithmetic_progression(first_term,differnce,number_of_term)

print(f"Sum of an arithmetic progression : {res}")



