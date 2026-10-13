# WAP to count number of consonant present inside the given string.

str1 = input("Enter your string:")
count = 0
i = 0

while i<len(str1):
    if str1[i].isalpha():
        if str1[i] not in  'aeiouAEIOU':
            count = count+1
    i=i+1

print(f"Number of consonants are : {count}")
