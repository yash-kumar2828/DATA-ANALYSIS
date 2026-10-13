# Print the Fibonacci Series

def get_fibonacci_series(num):
    a = 0
    b = 1
    print(a,b,end=" ")
    for i in range(3,num+1):
        c = a+b
        print(c,end=" ")
        a=b
        b=c

num = int(input("Enter your number : "))
get_fibonacci_series(num)