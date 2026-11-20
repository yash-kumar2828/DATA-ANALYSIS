# WAP to filter all the even numbers from the given list 

l = [2,5,3,12,11,1,10,11,12,21]

res = list(filter(lambda n1 : n1%2==0,l))

print(f"Even number is : {res}")
