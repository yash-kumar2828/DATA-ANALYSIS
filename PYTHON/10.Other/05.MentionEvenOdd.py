# WAP to mention all the even and odd number that is present the old list

l = [1,2,3,4,5,6,7,8,9,10]

res = ["Even" if i%2==0 else "Odd" for i in l]

print(res)