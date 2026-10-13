# WAP to print all those number which are divisible by both 3 & 5 starting from 1 t0 100

i = 1

print("Print divisible by both 3 & 5 starting from 1 t0 100:")
while i<=100:
    if i%3==0 and i%5==0:
        print(i,end=" ")
    i=i+1