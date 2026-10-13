# WAP to print all the numbers between the given range 

start = int(input("Enter a starting value:"))
end = int(input("Enter a ending value:"))

if start<=end:
    print(f"print all the numbers {start} to {end}:")
    while start<=end:
        print(start,end=" ")
        start=start+1

else:
    print(f"print all the numbers {start} to {end}:")
    while start>=end:
        print(start,end=" ")
        start=start-1