# WAP to add all the odd numbers by taking range from the users

start = int(input("Enter your starting number:"))
end = int(input("Enter your ending number:"))
sum = 0

if start<end:
    while start<=end:
        if start%2!=0:
            sum = sum+start
        start=start+1

else:
    while start>=end:
        if start%2!=0:
            sum=sum+start
        start=start-1  


print(f"Sum of all odd numbers is : {sum}") 


