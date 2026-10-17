''' Find the ASCII Value of a Character
Input: A
Output: 65'''

def find_ascii(character):
    print(f"The ASCII value of character {character} is : {ord(character)}")

character = input("Enter your single character : ")
find_ascii(character)
