# WAP to calculate the HCF of a given numbers.
                #    OR 
# WAP to calculate the GCD of a given numbers.


num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))

if num1<num2:
    small = num1

else:
    small = num2

for i in range(1,small+1):
    if num1%i==0 and num2%i==0:
        hcf=i

print(f"Calculate the HCF of a given number is : {hcf}")
