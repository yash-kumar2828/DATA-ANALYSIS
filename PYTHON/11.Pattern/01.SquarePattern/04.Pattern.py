'''
Enter the number of rows : 5
A A A A A 
B B B B B 
C C C C C 
D D D D D 
E E E E E '''

def get_pattern(n):

    for i in range(n):
        print((chr(65+i)+' ')*n)


num = int(input("Enter the number of rows : "))
get_pattern(num)