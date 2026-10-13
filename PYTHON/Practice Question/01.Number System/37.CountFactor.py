# Count the Number of Factors of a Number

def count_factor(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count

num = int(input("Enter your number : "))
res = count_factor(num)
print(f"Number of factors are : {res}")   
