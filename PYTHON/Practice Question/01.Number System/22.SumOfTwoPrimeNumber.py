# Express a Number as the Sum of Two Prime Numbers

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def sum_of_two_prime(num):
    if num<=2:
        return False

    if num%2==0:
        return True
    
    return is_prime(num-2)

num = int(input("Enter your number : "))
print(sum_of_two_prime(num))