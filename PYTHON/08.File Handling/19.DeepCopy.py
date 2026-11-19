import copy

x = [1,2,[3,4]]

y = copy.deepcopy(x)

print(x)
print(y)

x[2][0] = 'Mango'

print(x)
print(y)