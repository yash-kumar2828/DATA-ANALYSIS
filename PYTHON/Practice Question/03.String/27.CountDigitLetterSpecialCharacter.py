'''Count Digits, Letters and Special Characters
Input: Hello123!
Output: Letters: 5, Digits: 3, Special: 1 '''


def get_digit_letter_special_character(s1):

    letter = 0
    digit = 0
    special = 0

    for i in s1:

        if i.isalpha():
            letter+=1

        elif i.isdigit():
            digit+=1

        else:
            special+=1

    print(f"Letters : {letter}, Digits : {digit}, Special Character : {special}")

s1 = input("Enter the string : ")
get_digit_letter_special_character(s1)

