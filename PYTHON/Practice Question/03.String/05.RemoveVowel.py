''' Remove All Vowels from a String
Input: take u forward
Output: tk frwrd'''


def remove_vowel(str):
    res = ""
    for i in str:
        if i not in 'aeiouAEIOU':
            res+=i

    print(f"Print string without vowel : {res}")

str = input("Enter your string : ")
remove_vowel(str)