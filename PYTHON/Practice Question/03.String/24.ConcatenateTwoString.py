# Concatenate Two Strings
# Input: s1 = hello, s2 = world
# Output: helloworld


def concatenate_two_string(s1,s2):
    # First Way
    print(s1+s2)

    # second way
    print(f"{s1}{s2}")
    


s1 = input("Enter the first string : ")
s2 = input("Enter the second string : ")

concatenate_two_string(s1,s2)