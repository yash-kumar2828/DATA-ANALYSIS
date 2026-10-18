'''Count the Number of Words
Input: Hello
Output: 1
'''

def count_words(str1):
    list1 = str1.split()

    print(f"Number of count is : {len(list1)}")


str1 = input("Enter the string : ")
count_words(str1)

