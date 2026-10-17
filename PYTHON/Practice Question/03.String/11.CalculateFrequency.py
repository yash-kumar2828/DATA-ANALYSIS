'''Calculate Frequency of Characters
Input: takeuforward
Output: a2 d1 e1 f1 k1 o1 r2 t1 u1 w1  '''


def get_calculate_frequency(str1):

    d = {}

    for i in str1:

        d[i] = d.get(i,0)+1

    res = ''

    for i in sorted(d):
        res = res + i + str(d[i]) + " "

    print(res.strip())

str1 = input("Enter the string : ")
get_calculate_frequency(str1)