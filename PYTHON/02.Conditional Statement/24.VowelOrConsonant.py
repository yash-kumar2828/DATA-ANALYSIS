# WAP to check wheather a given character is vowel or consonant

ch = input("Enter your characeter:")

if ch.isalpha():  
    if ch in 'AEIOUaeiou':
        print(f"{ch} is a vowel")

    else:
        print(f"{ch} is a consonant")

else:
    print(f"{ch} is not an alphabet")