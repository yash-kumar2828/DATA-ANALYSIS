# WAP that prints first and last 3 characters of the string as a single string if the string has less than six characters then print an empty string.

s = input("Enter your string : ")

if len(s)<6:
    print('Empty string')
else:
    print(s[:3]+s[-3:])