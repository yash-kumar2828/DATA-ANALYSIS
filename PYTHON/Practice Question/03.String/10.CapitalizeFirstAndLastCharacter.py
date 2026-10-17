''' Capitalize First and Last Character of Each Word
Input: take u forward is awesome
Output: TakE U ForwarD IS AwesomE'''



def get_capitalize_first_last(str1):

    l1 = str.split()
    res = []

    for i in l1:
        if len(i) == 1:
            res.append(i.upper())

        else:

            res.append(i[0].upper()+i[1:-1]+i[-1].upper())

    output = ' '.join(res)

    

    print(output)


str = input("Enter the string : ")
get_capitalize_first_last(str)