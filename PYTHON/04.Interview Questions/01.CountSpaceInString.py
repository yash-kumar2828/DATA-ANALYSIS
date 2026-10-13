# WAP to count number of spaces present inside the given string.
# I/P :-My Name is Yash Kumar
# O/P :-4

str1 = input("Enter your string : ")
count = 0
for i in str1:
    if i == " ":
        count+=1
print(f"Number of spaces present inside the given string : {count}")