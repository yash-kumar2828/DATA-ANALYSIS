# WAP to check wheather given character is consonant or not

ch = input("Enter your character:")

if ch.isalpha() and ch not in 'AEIOUaeiou':
    print(f"{ch} is consonant")

else:
    print(f"{ch} is not consonant")