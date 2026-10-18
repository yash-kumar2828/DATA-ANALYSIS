'''Count Occurrences of a Given Character
Input: s1 = banana, occur = a
Output: 3 '''


def count_occurrence(str1,occur):

    count = 0

    for i in str1:

        if occur is i:
            count+=1


    print(count)

str1 = input("Enter the string : ")
occur = input("Enter the character you want to count : ")
count_occurrence(str1,occur)
