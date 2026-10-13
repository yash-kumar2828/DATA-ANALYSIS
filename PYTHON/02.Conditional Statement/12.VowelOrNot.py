# WAP to check wheather a given character is vowel or not

ch = input("Enter your character:")

if ch in 'AEIOU' or ch in 'aeiou':
    print(f"{ch} is vowel ")

else:
    print(f"{ch} is not vowel")