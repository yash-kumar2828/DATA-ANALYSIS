# WAP to check wheather a given number is armstrong number
num = int(input("Enter your number:"))
temp = num
temp2 = num

count = 0
arm = 0

while num>0:
    count = count+1
    num = num//10


while temp>0:
    rem = temp%10
    arm = arm+rem**count
    temp=temp//10

if temp2==arm:
    print(f"{temp2} is an armstrong number")

else:
    print(f"{temp2} is not an armstrong number")
