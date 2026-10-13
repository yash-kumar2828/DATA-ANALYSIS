# Find the Sum of All Factors of a Number

def sum_of_factor(n):
    sum = 0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            fact1 = i
            fact2 = n//i
            if fact1!=fact2:
                sum+=fact1+fact2
            else:
                sum+=fact1
    return sum

num = int(input("Enter your number : "))
res = sum_of_factor(num)
print(f"Sum of factor is : {res}")