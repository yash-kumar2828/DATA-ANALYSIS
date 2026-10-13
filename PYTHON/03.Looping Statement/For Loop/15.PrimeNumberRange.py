# WAP  to display all the prime numbers between given range.

start = int(input("Enter your starting value:"))
end = int (input("Enter your ending value:"))

print(f"Display all the prime numbers between {start} to {end} : ")
for i in range(start,end+1):
    count = 0
    for j in range(1,i+1):
        if i%j==0:
            count+=1

    if count==2:
        print(i,end=" ")