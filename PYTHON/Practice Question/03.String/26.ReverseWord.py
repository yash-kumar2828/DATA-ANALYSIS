'''Reverse Words in a String
Input: welcome to the jungle
Output: jungle the to welcome
'''


def reverse_word(s1):
    list1 = s1.split()

    # First Way 
    res = list1[::-1]
    output = ' '.join(res)
    print(output)

    # second way 
    res2 = []
    for i in range(len(list1)-1 , -1 , -1):
        res2.append(list1[i])

    output2 = ' '.join(res2)
    print(output2)




s1 = input("Enter the string : ")
reverse_word(s1)
