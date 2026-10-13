# Find the Sum of a Geometric Progression

def get_sum_of_geometric_progression(first_term,ratio,number_of_term):
    sum = 0
    power = 0
    for i in range(1,number_of_term+1):
        sum = sum+first_term*ratio**power
        power+=1
    return sum


first_term = int(input("Enter your first term : "))
ratio = int(input("Enter your ratio : "))
number_of_term = int(input("Enter your number of term : "))
res = get_sum_of_geometric_progression(first_term,ratio,number_of_term)

print(f"Sum of geometric progression is : {res}")
