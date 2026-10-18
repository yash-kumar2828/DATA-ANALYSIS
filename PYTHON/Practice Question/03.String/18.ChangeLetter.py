'''Change Every Letter to the Next Alphabet
Input: abcdxyz
Output: bcdeyza'''


def get_every_letter_to_next(str1):

    res = []

    for i in str1:

        if "A"<=i<="Z":

            if i == "Z":
                res.append("A")

            else:
                res.append(chr(ord(i)+1))

        elif "a"<=i<="z":
            if i == "z":
                res.append("a")

            else:
                res.append(chr(ord(i)+1))

        else:
            res.append(i)

    output = ''.join(res)
    print(output)


str1 = input("Enter the string : ")
get_every_letter_to_next(str1)

