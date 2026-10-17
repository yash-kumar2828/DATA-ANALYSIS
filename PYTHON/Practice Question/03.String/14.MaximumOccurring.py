''' Find the Maximum Occurring Character
Input: takeuforward
Output: a    '''



def get_maximum_occurring(str1):

    d = {}

    for i in str1:
        d[i] = d.get(i,0)+1

    list1 = []

    for i in d:
        list1.append(d[i])


    sorted_list = sorted(list1)  
    largest = sorted_list[-1]

    for i in d:
        if largest == d[i]:
            largest = i
            break

    print(f"Largest character is : {largest}") 



str1 = input("Enter the string : ")
get_maximum_occurring(str1)