# WAP to reverse word of the given string.
# I/P :- my name is yash kumar
# O/P :- kumar yash is name my

str1 = input("Enter your string : ")

l1 = str1.split()
revList = l1[::-1]
revWord = " ".join(revList)

print(revWord)