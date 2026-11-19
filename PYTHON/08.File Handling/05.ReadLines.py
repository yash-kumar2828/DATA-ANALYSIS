f = open("Sample2.txt",'r')

data = f.readlines()

print(data[1])

for i in data:
    print(i)

f.close()