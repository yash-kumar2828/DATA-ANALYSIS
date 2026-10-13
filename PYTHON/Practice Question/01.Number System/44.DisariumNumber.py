# Check Whether a Number is a Disarium Number

def get_count_digit(n):
    count = 0
    while n>0:
        count+=1
        n//=10
    return count

def is_disarium_number(n):
    digit = get_count_digit(n)
    res = 0
    temp = n
    while n>0:
        rem = n%10
        res = res+rem**digit
        digit-=1
        n//=10
    return temp == res


num = int(input("Enter your number : "))

if is_disarium_number(num):
    print(f"{num} is disarium number")
else:
    print(f"{num} is not disarium number")