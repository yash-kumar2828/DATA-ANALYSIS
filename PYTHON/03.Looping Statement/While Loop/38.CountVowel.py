# WAP to count how many numbers of vowels do we have inside a string.

str1 = input("Enter your string:")

count = 0
i = 0

while i<len(str1):
    if str1[i] in 'aeiouAEIOU':
        count = count+1
    i=i+1

print(f"Numbers of vowels are : {count}") 