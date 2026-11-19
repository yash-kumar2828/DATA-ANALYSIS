'''Find the Shortest Word in a String
Input: code in Java
Output: in  '''


def get_shortest_word(s1):
    if len(s1) == 0:
        return ''
    words = s1.split()

    shortest = words[0]

    for i in words:
        if len(i) < len(shortest) :
            shortest = i

    print(shortest)
    


s1 = input("Enter the string : ")
get_shortest_word(s1)
