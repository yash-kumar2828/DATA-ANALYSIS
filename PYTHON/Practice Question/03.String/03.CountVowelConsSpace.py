''' Count Vowels, Consonants and Spaces
Input: Take u forward is Awesome
Output: Vowels: 10, Consonants: 11, White spaces: 4'''

def count_vowel_consonant_space(str):
    vowel = 0
    consonant = 0
    space = 0
    for i in str:
        if i in 'aeiouAEIOU':
            vowel+=1

        elif i.isalpha() and i not in 'aeiouAEIOU':
            consonant+=1

        elif i==" ":
            space+=1

    print(f"Vowel : {vowel}, Consonant : {consonant}, Space : {space}")

str1 = input("Enter the string : ")
count_vowel_consonant_space(str1)

        
