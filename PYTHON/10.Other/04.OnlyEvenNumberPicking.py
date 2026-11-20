# WAP to generate a new list from the old list by picking only even numbers

l = [1,2,3,4,5,6,7,8,9,10]

res = [i for i in l if i%2==0]

print(f"Only Even number is : {res}")