'''Find the Word with Highest Repeated-Letter Frequency
Input: abcdefghij google microsoft
Output: google
'''

def get_highest_repeated_letter(str1):

    list1 = str1.split()

    max_count = 1
    res_word = "-1"

    for i in list1:
        d = {}

        for j in i:
            d[j] = d.get(j,0)+1

            if d[j]>max_count:
                max_count =d[j]
                res_word = i
                
    print(res_word)

str1 = input("Enter the string : ")
get_highest_repeated_letter(str1)