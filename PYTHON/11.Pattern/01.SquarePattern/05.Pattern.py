'''
Enter the number of rows : 5
E E E E E 
D D D D D 
C C C C C 
B B B B B 
A A A A A '''

def get_pattern(n):

    for i in range(n):
        print((chr(64+n-i)+' ')*n)

num = int(input("Enter the number of rows : "))
get_pattern(num)