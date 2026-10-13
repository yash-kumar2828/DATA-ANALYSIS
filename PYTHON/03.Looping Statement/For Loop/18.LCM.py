# WAP to calculate the LCM at a given numbers.
# Formula:-    LCM= (num1*num2)/HCF

num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))

if num1<num2:
    small = num1

else:
    small = num2

for i in range(1,small+1):
    if num1%i==0 and num2%i==0:
        hcf = i

lcm = (num1*num2)/hcf
print(f"Calculate the LCM at a given numbers : {lcm}")
