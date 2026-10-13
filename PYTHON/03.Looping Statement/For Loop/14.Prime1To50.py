# WAP to print all the prime number between 1 t0 50.

print("Print all the prime number between 01 to 50:")

for i in range(1,51):
    count = 0

    for j in range(1,i+1):
        if i%j==0:
            count+=1

    if count == 2:
        print(i,end=' ')