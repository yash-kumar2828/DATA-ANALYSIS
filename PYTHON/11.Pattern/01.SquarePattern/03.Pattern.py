'''
Enter the number of rows : 5
5 5 5 5 5 
4 4 4 4 4 
3 3 3 3 3 
2 2 2 2 2 
1 1 1 1 1   '''

def get_pattern(n):

    for i in range(n):
        print((str(n-i)+' ')*n)

num = int(input("Enter the number of rows : "))
get_pattern(num)