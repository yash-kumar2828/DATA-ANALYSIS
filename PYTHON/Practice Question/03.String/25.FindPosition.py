'''Find the Position of a Substring
Input: s1 = takeuforward, s2 = forward
Output: 5'''


def find_the_position(s1,s2):
    position = s1.find(s2)

    print(position)


s1 = input("Enter the first string : ")
s2 = input("Enter the second string : ")
find_the_position(s1,s2)
