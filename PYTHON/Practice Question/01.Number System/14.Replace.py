# Replace All 0s with 1s in a Number


# FIrst Method 
num = int(input("Enter your digit : "))

res = str(num).replace('0','1')

print(int(res))



# Second Method 
num2 = int(input("Enter your number : "))
res = 0
place = 1
while num2>0:
    digit = num2%10
    if digit == 0:
        digit = 1
    res = res+digit*place
    place = place *10
    num2 = num2//10

print(res)





